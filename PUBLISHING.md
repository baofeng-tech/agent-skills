# Publishing Notes

这批 skill 当前是在临时整理仓库中生成的，正式发布目标为：

- Repository: <https://github.com/AIsa-team/agent-skills>
- Branch: `agentskills`
- Branch URL: <https://github.com/AIsa-team/agent-skills/tree/agentskills>

## 建议发布步骤

1. 将本目录下各 skill 子目录复制到正式仓库 `agentskills` 分支根目录。
2. 同步复制以下索引文件到正式仓库根目录或你们约定的索引目录：
   - `index.md`
   - `index.json`
   - `well-known-skills-index.json`
3. 如果目标平台是 ClawHub，优先从 `../clawhub-release/` 选择对应变体，而不是直接从 `targetSkills/` 上传。
4. 如果后续要支持域名发现，再把 `well-known-skills-index.json` 发布到：

```text
https://your-domain/.well-known/skills/index.json
```

## 文件用途

- `index.md`: 给人类阅读的 skill 列表
- `index.json`: 给内部工具、脚本或简单注册流程读取
- `well-known-skills-index.json`: 给支持域名发现的客户端做标准入口样例

## 当前建议

- 先发布 `aisa-twitter-command-center`
- 再发布 `aisa-twitter-post-engage`
- 然后发布两个 YouTube skill
- 对其余 Twitter 变体后续再做品牌和去重整理
