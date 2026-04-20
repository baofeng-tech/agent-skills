# Publishing agentskill.sh Release

1. Run `python3.12 scripts/build_agentskill_sh_release.py`.
2. Push the generated contents to the public GitHub repository `https://github.com/baofeng-tech/agent-skills`.
3. Submit that repository at `https://agentskill.sh/submit`.
4. For ongoing sync, add the webhook `https://agentskill.sh/api/webhooks/github`.
5. Keep the generated catalog files at repo root for GitHub import clarity.

## Notes

- agentskill.sh accepts either a GitHub repo URL or a direct `SKILL.md` URL.
- This release layer keeps one skill per root directory so repo scanning stays predictable.
- It removes plugin wrapper files such as `package.json` and `index.ts` when they are not part of the shipped standard skill surface.
