# 每周记忆报告的提示词

由审查者每周一跑一次。只读，只报告。规则见 `rules\memory.md` 第 9 节。

---

你是审查者。做一次 EverOS 记忆的每周检查。

只做只读操作。不写入，不 flush，不更正，不删除。

范围：上周一 0 点到本周一 0 点（北京时间），`claude-code/claude-code` 分区。

步骤：

1. 调 `POST http://127.0.0.1:8000/api/v2/memory/get` 列记录。
   - 请求体带 `user_id`（本机 EverOS 的用户编号）、`app_id` 和 `project_id` 都是 `claude-code`、`memory_type: episode`、`page_size: 100`。
   - `filters` 写 `{"timestamp": {"gte": "<上周一>T00:00:00+08:00", "lt": "<本周一>T00:00:00+08:00"}}`。
   - 按 `total_count` 翻页，取完为止。
2. 逐条记录检查四件事。
   - 没有任务编号：`session_id` 不符合 `^h-\d{8}-[a-z0-9][a-z0-9-]{0,39}$`。UUID 是自动保存（Claude Code 钩子或 Pi 扩展），单独计数，不算问题。
   - 写入方不对：`sender_ids` 里有 `unknown-client`，或者有名单外的名字。名单是用户本人的 `user_id`、`codex`、`cursor`、`claude-code`、`grok`、`pi`。
   - 已知名单里的 `pi` 有两种记录。会话号是 UUID 的是自动保存，是任务编号的是结论。
   - 缺三件事：只查 `session_id` 是任务编号的记录。`episode` 正文里缺"适用情况""可信程度""何时重新检查"任何一项。
   - 卡在缓冲区：对每个任务编号调一次 `POST /api/v2/memory/search`，带 `filters.session_id`。`unprocessed_messages` 不是空的就记下。
3. 写报告。
   - 先写结论：一共几条记录，几条有问题。
   - 再按四类列出。每条写 `id`、`session_id`、`sender_ids`、`timestamp` 和问题。不抄记录正文。
   - 最后写本次查了哪些接口，有没有失败。
4. 报告写进任务记录，再交给用户。不自己更正。

接口用不了或用户电脑不在线时，报告写"本周没查成"，并写明原因。

---

## 使用备注（不进提示词）

1. 2026-10-19 实测过 `filters.timestamp` 用 `gte`，能用，返回 200。`lt` 还没实测，第一次跑之前先只读试一次。
2. "缺三件事"查的是 `episode` 正文。正文是 EverOS 用模型整理过的，原话里的三个词可能被改写。第一次跑时人工抽查几条，看会不会误报。
