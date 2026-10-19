# 分发正本

这个文件夹存放分发正本。分发正本是 harness 写进仓库外工具配置的原文。

| 文件 | 写到哪里 | 写法 |
|---|---|---|
| `codex-AGENTS-snippet.md` | Codex 的 `AGENTS.md` | 插在 ste-zh 那一块之前。 |
| `cursor/harness-standing-rules.mdc` | Cursor 的 `rules` 目录 | 作为新的规则文件放进去。 |
| `claude-code-CLAUDE-snippet.md` | Claude Code 的 `CLAUDE.md` | 加在文件末尾。 |
| `pi/AGENTS.md` | Pi 的全局说明文件 `~/.pi/agent/AGENTS.md` | 新建。Pi 在 WSL 里，路径换成 WSL 里看到的写法。 |
| `pi/mcp.json.snippet` | Pi 的 `~/.pi/agent/mcp.json` | 在 `mcpServers` 里加一项，原有的项不动。 |

分发时，把相对路径换成本机 harness 仓库的完整路径。

改配置时，以这个文件夹合并后的版本为准。每次改配置前，先要你同意。

完整的分发配置是第 7 个模块。
