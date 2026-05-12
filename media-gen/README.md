# Media Gen

GitHub-ready release package prepared specifically for agentskill.sh import and refresh.

## Notes

- Generate images and videos with AIsa. Supports Gemini, Wan, and Seedream image generation plus Wan text-to-video and image-to-video models. One API key; the bundled client routes each model to the correct endpoint automatically. Use when: you need a neutral AIsa media-generation skill that spans multiple model families without changing credentials or request flow.
- This directory keeps one root-level skill per folder so agentskill.sh can scan the repository cleanly.
- The same skill can also be submitted by direct `SKILL.md` URL when needed.
