"""First-run setup wizard for last30days.

Detects first run, reports AISA-first setup readiness, and writes configuration.
The actual wizard UI is SKILL.md-driven (the LLM presents it), but this module
provides the detection and setup actions.
"""

import json
import logging
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)


def is_first_run(config: Dict[str, Any]) -> bool:
    """Return True if the setup wizard has not been completed.

    Checks for SETUP_COMPLETE in the config dict. If it's not set
    (None or empty string), the user hasn't gone through setup yet.
    """
    return not config.get("SETUP_COMPLETE")


def run_auto_setup(config: Dict[str, Any]) -> Dict[str, Any]:
    """Perform the auto-setup actions.

    - Detects whether AISA is configured

    Returns:
        Dict with keys:
          cookies_found: {}
          aisa_configured: bool
          env_written: bool (always False here — caller writes config separately)
    """
    results: Dict[str, Any] = {
        "cookies_found": {},
        "aisa_configured": bool(config.get("AISA_API_KEY")),
        "env_written": False,
    }
    return results


def write_setup_config(env_path: Path, from_browser: str = "off") -> bool:
    """Write SETUP_COMPLETE and FROM_BROWSER to the .env file.

    Creates the file and parent directories if needed.
    Appends to existing file without overwriting existing keys.

    Args:
        env_path: Path to the .env file (e.g. ~/.config/last30days/.env)
        from_browser: Browser extraction mode to write (default: "off")

    Returns:
        True if config was written successfully, False on error.
    """
    try:
        env_path = Path(env_path)
        env_path.parent.mkdir(parents=True, exist_ok=True)

        # Read existing content to avoid overwriting keys
        existing_keys: set = set()
        existing_content = ""
        if env_path.exists():
            existing_content = env_path.read_text(encoding="utf-8")
            for line in existing_content.splitlines():
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and "=" in stripped:
                    key = stripped.split("=", 1)[0].strip()
                    existing_keys.add(key)

        lines_to_add = []
        if "SETUP_COMPLETE" not in existing_keys:
            lines_to_add.append("SETUP_COMPLETE=true")
        if "FROM_BROWSER" not in existing_keys:
            lines_to_add.append(f"FROM_BROWSER={from_browser}")

        if not lines_to_add:
            return True  # Nothing to write, already configured

        # Ensure trailing newline before appending
        with open(env_path, "a", encoding="utf-8") as f:
            if existing_content and not existing_content.endswith("\n"):
                f.write("\n")
            f.write("\n".join(lines_to_add) + "\n")

        return True

    except OSError as exc:
        logger.error("Failed to write setup config to %s: %s", env_path, exc)
        return False


def get_setup_status_text(results: Dict[str, Any]) -> str:
    """Return a human-readable summary of auto-setup results.

    Args:
        results: Dict from run_auto_setup()

    Returns:
        Multi-line status text.
    """
    lines = []
    lines.append("Setup complete! Here's what I found:")
    lines.append("")

    cookies_found = results.get("cookies_found", {})
    if results.get("aisa_configured"):
        lines.append("  - AISA API key configured")
    else:
        lines.append("  - AISA API key not configured")

    env_written = results.get("env_written", False)
    if env_written:
        lines.append("")
        lines.append("Configuration saved. Future runs will use the AISA-first setup defaults.")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# OpenClaw server-side setup (no browser, JSON output)
# ---------------------------------------------------------------------------

_OPENCLAW_KEY_NAMES = [
    "AISA_API_KEY",
]


def _has_python312_plus() -> bool:
    candidates = [
        "/usr/local/python3.12/bin/python3.12",
        shutil.which("python3.14"),
        shutil.which("python3.13"),
        shutil.which("python3.12"),
        shutil.which("python3"),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            proc = subprocess.run(
                [candidate, "-c", "import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)"],
                capture_output=True,
                check=False,
                text=True,
            )
        except OSError:
            continue
        if proc.returncode == 0:
            return True
    return False


def run_openclaw_setup(config: Dict[str, Any]) -> Dict[str, Any]:
    """Server-side setup probe: no browser auth, just tool + key availability.

    Returns a dict suitable for JSON output to stdout so that SKILL.md
    can present appropriate options to the user.
    """
    node = shutil.which("node") is not None
    python3 = _has_python312_plus()

    keys: Dict[str, bool] = {}
    for key_name in _OPENCLAW_KEY_NAMES:
        short = key_name.lower().replace("_api_key", "").replace("_key", "").replace("_token", "")
        # Normalize env key names for UI-facing status output.
        keys[short] = bool(config.get(key_name))

    x_method: Optional[str] = "aisa" if config.get("AISA_API_KEY") else None

    return {
        "node": node,
        "python3": python3,
        "keys": keys,
        "aisa_configured": bool(config.get("AISA_API_KEY")),
        "x_method": x_method,
    }


# ---------------------------------------------------------------------------
# Legacy PAT auth compatibility flow
# ---------------------------------------------------------------------------

_PAT_BASE = "https://api.scrapecreators.com/v1/github/pat"


def auth_with_pat(github_token: str) -> Optional[Dict[str, Any]]:
    """Authenticate with the legacy compatibility service using a GitHub PAT.

    POSTs the token to the legacy PAT auth endpoint. The service verifies it
    against GitHub's API, creates/finds the account, and returns an API key.

    Returns:
        Dict with api_key, github_username, etc. on success, None on failure.
    """
    try:
        req = Request(f"{_PAT_BASE}/auth", data=b"", method="POST")
        req.add_header("Authorization", f"Bearer {github_token}")
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except HTTPError as exc:
        if exc.code == 422:
            logger.warning("PAT auth: insufficient scope — user needs user:email")
        else:
            logger.warning("PAT auth failed: %s", exc)
        return None
    except (URLError, OSError) as exc:
        logger.warning("PAT auth request failed: %s", exc)
        return None

    if not data.get("api_key"):
        logger.warning("PAT auth returned no api_key: %s", data)
        return None

    return data


# ---------------------------------------------------------------------------
# Legacy device auth compatibility flow
# ---------------------------------------------------------------------------

_DEVICE_BASE = "https://api.scrapecreators.com/v1/github/device"


def run_device_auth() -> Optional[Tuple[str, str, str, int]]:
    """Start the legacy device authorization flow.

    POSTs to the compatibility service device/code endpoint.

    Returns:
        (device_code, user_code, verification_uri, interval) on success,
        None on failure.
    """
    try:
        body = json.dumps({}).encode()
        req = Request(f"{_DEVICE_BASE}/code", data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except (HTTPError, URLError, OSError) as exc:
        logger.warning("Device auth code request failed: %s", exc)
        return None

    device_code = data.get("device_code")
    user_code = data.get("user_code")
    verification_uri = data.get("verification_uri")
    interval = data.get("interval", 5)

    if not device_code or not user_code:
        logger.warning("Device auth returned incomplete response: %s", data)
        return None

    return (device_code, user_code, verification_uri or "", interval)


def poll_device_auth(
    device_code: str,
    interval: int,
    timeout: int = 300,
    user_code: str = "",
    clipboard_ok: bool = False,
) -> Optional[str]:
    """Poll for an access token after the user authorizes the device.

    Args:
        device_code: The device_code from run_device_auth().
        interval: Polling interval in seconds.
        timeout: Maximum time to poll in seconds.
        user_code: The user code to remind about during polling.
        clipboard_ok: Whether the code was copied to clipboard.

    Returns:
        access_token on success, None on timeout or failure.
    """
    import sys

    deadline = time.time() + timeout
    last_reminder = time.time()
    reminder_count = 0
    max_reminders = 4
    reminder_interval = 30  # seconds between reminders

    while time.time() < deadline:
        time.sleep(interval)

        # Periodic reminder of the code while waiting
        if (
            user_code
            and reminder_count < max_reminders
            and time.time() - last_reminder >= reminder_interval
        ):
            clipboard_hint = " (on your clipboard)" if clipboard_ok else ""
            print(
                f"  Still waiting... Your code: {user_code}{clipboard_hint}",
                file=sys.stderr,
                flush=True,
            )
            last_reminder = time.time()
            reminder_count += 1

        try:
            body = json.dumps({"device_code": device_code}).encode()
            req = Request(f"{_DEVICE_BASE}/token", data=body, method="POST")
            req.add_header("Content-Type", "application/json")
            with urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
        except HTTPError as exc:
            if exc.code in (400, 403, 428):
                continue
            logger.warning("Device auth poll error: %s", exc)
            return None
        except (URLError, OSError):
            continue

        if data.get("access_token"):
            return data["access_token"]

        error = data.get("error")
        if error == "slow_down":
            interval = min(interval + 2, 30)
            continue
        if error == "authorization_pending":
            continue
        if error in ("expired_token", "access_denied"):
            logger.warning("Device auth failed: %s", error)
            return None

    return None


def fetch_api_key(access_token: str) -> Optional[str]:
    """Fetch the legacy compatibility API key using the GitHub access token.

    GETs the device/profile endpoint with Bearer auth.

    Returns:
        api_key string on success, None on failure.
    """
    try:
        req = Request(f"{_DEVICE_BASE}/profile")
        req.add_header("Authorization", f"Bearer {access_token}")
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except (HTTPError, URLError, OSError) as exc:
        logger.warning("Failed to fetch API key: %s", exc)
        return None

    return data.get("api_key")


def run_full_device_auth(timeout: int = 300) -> Dict[str, Any]:
    """Run the complete legacy GitHub device auth flow and return a result.

    Chains: start device flow -> open browser -> poll -> fetch API key.
    Designed to be called from the CLI and have its stdout parsed by the LLM.

    Returns:
        Dict with status and relevant fields:
        - {"status": "success", "api_key": "sc_...", "user_code": "ABCD-1234"}
        - {"status": "error", "message": "..."}
        - {"status": "timeout", "user_code": "ABCD-1234"}
        - {"status": "denied"}
    """
    import webbrowser

    # Step 1: Start device flow
    result = run_device_auth()
    if result is None:
        return {"status": "error", "message": "Failed to start legacy device auth flow"}

    device_code, user_code, verification_uri, interval = result

    import sys

    # Step 2: Copy code to clipboard BEFORE opening browser
    clipboard_ok = False
    if sys.platform == "darwin":
        try:
            subprocess.run(
                ["pbcopy"], input=user_code.encode(), check=True, timeout=5,
            )
            clipboard_ok = True
        except Exception:
            pass  # pbcopy unavailable or failed, fall through

    # Step 3: Show code prominently, then open browser
    clipboard_hint = "  (copied to clipboard)" if clipboard_ok else ""
    code_line = f"  Your code: {user_code}{clipboard_hint}"
    action_line = "  Paste it on the GitHub page that just opened"
    width = max(len(code_line), len(action_line)) + 2
    border = "-" * width
    print(f"\n+{border}+", file=sys.stderr)
    print(f"|{code_line.ljust(width)}|", file=sys.stderr)
    print(f"|{action_line.ljust(width)}|", file=sys.stderr)
    print(f"+{border}+", file=sys.stderr)

    if verification_uri:
        try:
            webbrowser.open(verification_uri)
        except Exception:
            print(f"Open: {verification_uri}", file=sys.stderr)

    print("Waiting for authorization...", file=sys.stderr, flush=True)

    # Step 4: Poll for token (with periodic code reminders)
    access_token = poll_device_auth(
        device_code, interval, timeout=timeout,
        user_code=user_code, clipboard_ok=clipboard_ok,
    )
    if access_token is None:
        return {"status": "timeout", "user_code": user_code, "clipboard_ok": clipboard_ok}

    # Step 4: Fetch API key
    api_key = fetch_api_key(access_token)
    if api_key is None:
        return {
            "status": "error",
            "message": "Authorized but failed to fetch API key",
            "clipboard_ok": clipboard_ok,
        }

    return {"status": "success", "method": "device", "api_key": api_key, "user_code": user_code, "clipboard_ok": clipboard_ok}


# ---------------------------------------------------------------------------
# Unified legacy GitHub auth: PAT first, device flow fallback
# ---------------------------------------------------------------------------


def run_github_auth(timeout: int = 300) -> Dict[str, Any]:
    """Try legacy PAT auth via gh CLI, fall back to the legacy device flow.

    1. Check for `gh` CLI
    2. If found, run `gh auth token` to get a PAT
    3. POST PAT to the compatibility service — if it works, done
    4. If PAT fails for any reason, fall through to device flow

    Returns JSON-serializable dict with status, method, and api_key.
    """
    import sys

    # Step 1: Try PAT via gh CLI
    gh_path = shutil.which("gh")
    if gh_path:
        try:
            result = subprocess.run(
                ["gh", "auth", "token"],
                capture_output=True, text=True, timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                token = result.stdout.strip()
                print("Found gh CLI — trying PAT auth...", file=sys.stderr)
                pat_result = auth_with_pat(token)
                if pat_result and pat_result.get("api_key"):
                    return {
                        "status": "success",
                        "method": "pat",
                        "api_key": pat_result["api_key"],
                        "github_username": pat_result.get("github_username", ""),
                    }
                # PAT failed — might be insufficient scope
                print(
                    "PAT auth didn't work (scope or endpoint issue). "
                    "Falling back to GitHub device flow...",
                    file=sys.stderr,
                )
        except Exception as exc:
            logger.debug("gh auth token failed: %s", exc)

    # Step 2: Fall back to device flow
    if not gh_path:
        print("gh CLI not found — using GitHub device flow...", file=sys.stderr)

    return run_full_device_auth(timeout=timeout)
