# 记忆规则

这份规则只定三件事：闭环的哪一环读 EverOS，哪一环写，写什么。规则里的词按 `harness\GLOSSARY.md` 理解。出处列在文末"来源"一节。

## 1. 和 EverOS 使用规则的分工

1. 接口怎么调用，以 EverOS 使用规则 `everos-usage.md` 为准。
   - 它在 `memory-stack` 项目的 `docs` 文件夹里，不在这个仓库里。
2. 这份规则不重写接口用法，只写闭环里什么时候用、写什么。
3. 两份规则冲突时，接口细节听 `everos-usage.md`，时机和授权听这份规则。
4. `everos-usage.md` 先按用户同意的修订稿改正，这份规则才合并。

## 2. 什么时候读

1. 第一环开始时搜两次。
   - 用 `everos_search` 搜以前的决定和经验。
   - 用 `everos_kb_search` 搜知识文章，`top_k` 至少取 9，逐条看相关度分数。
2. 知识文章的结果要带 `app_id`。
   - `app_id` 只能是 `second-brain`、`claude-code`、`default` 三者之一。
   - 不带 `app_id` 的结果不是本机 EverOS 给的，不能用。
3. 开场简报列出查到的每一条，并标明用上、没用上或已过时。
4. 第二环收集信息时，先查知识库，再往外查。
5. 其他环节默认不搜。
6. 搜不到只说明 EverOS 里没有，资料本身可能还在原文件里。

## 3. 什么时候写，写什么

1. 只在第四环复盘时写。
2. 只写确认过的结论，不写过程。
3. 每条结论在正文里写明三件事：适用情况、可信程度、何时重新检查。
4. 写之前要有授权。授权记在启动记录里，并写明允许写入哪些类型的结论。
5. 启动记录没写授权时，结论只留在任务记录里。
6. 每次写入都传 `defer_extraction: false`。新代码不传也是 false，但旧会话里的进程还是旧代码，所以照样要传。
7. 写入返回 `accumulated`，说明内容还在缓冲区。这时对同一个 `session_id` 调一次 `everos_flush`，再搜一次确认。
8. 写完用 `everos_search` 搜一次，确认这条结论能搜到。搜不到就记进任务记录，不算写成。

## 4. 存在哪里

1. 记忆统一存在 `claude-code/claude-code` 分区。
2. 不传 `project_id`。
   - 新版 MCP 会忽略它。
   - 直接调接口时，`app_id` 和 `project_id` 都填 `claude-code`。
3. `session_id` 填任务编号，格式是 `h-YYYYMMDD-<简称>`。
   - 简称只用小写字母、数字和连字符，最长 40 个字符。
   - 例子：`h-20261019-memory-guard`。
   - 新版 MCP 只收这种格式和 UUID，其他格式会被拒绝，什么也不写。
4. `sender_id` 是写入方的名字，由配置决定，agent 不用自己填。
   - Codex 填 `codex`，Cursor 填 `cursor`，Claude Code 填 `claude-code`，Pi 填 `pi`。
   - 这四个值写在各自的 MCP 配置里。
   - 第二大脑直接调接口，助手消息的 `sender_id` 填 `grok`。
   - 配置没设好时，记录照常写入，写入方记为 `unknown-client`，每周报告会标出来。
5. 任务编号和工具名在结论正文里也写一遍，作为保底。

## 5. 谁来写，走哪条路

1. Codex、Cursor、Claude Code、Pi 的任务，由它们自己写。
   - 它们都通过 `everos-local` 写。
2. Grok Bot 上的任务，由第二大脑这个 agent 读写。
3. 第二大脑只走一条路：在用户电脑上用本机命令，调 WSL 里的 `http://127.0.0.1:8000`。
   - 记忆搜索：`POST /api/v2/memory/search`，`app_id` 和 `project_id` 都填 `claude-code`。
   - 知识搜索：`POST /api/v2/knowledge/search`，三个分区各查一次。
   - 写入：`POST /api/v2/memory/add`，格式和第 4 节一致。
4. 第二大脑不用 `second-brain-tools` 项目 `scripts` 文件夹里的任何脚本。
   - 尤其是 `everos_mcp_server.py`，它是旧的 `everos-kb`，连的是 EverOS Cloud。
   - 云端那份知识库停在 2026-09-10，还要用云端密钥。
5. 用户电脑不在线时，第二大脑不读也不写。它把这件事记进任务记录，等电脑上线再补。

## 6. 自动保存不算结论

1. 有两个写入方会每轮自动保存对话。
   - Claude Code 的 Stop 和 SessionEnd 钩子；
   - Pi 的 `everos.ts` 扩展。
2. 自动保存的会话号是客户端自己的 UUID，不是任务编号。
3. 自动保存的内容不算第四环的结论，也不需要授权。
4. 审查者只核对任务编号下的记录。
5. Pi 的自动保存和结论都标成 `pi`，靠会话号区分。

## 7. 复盘时怎么核对和更正

1. 审查者用 WSL 里的只读接口列出这次任务写入的记录。
   - 地址：`POST http://127.0.0.1:8000/api/v2/memory/get`。
   - 请求体：`{"user_id":"<用户编号>","app_id":"claude-code","project_id":"claude-code","memory_type":"episode","page_size":100,"page":1,"filters":{"session_id":"<任务编号>"}}`。
   - `<用户编号>` 是本机 EverOS 的用户编号。任意一条已有记录的 `user_id` 就是它。
   - `session_id` 必须放在 `filters` 里。放在最外层会报 422。
   - `memory_type` 必填。
   - `page_size` 最大 100。按返回的 `total_count` 翻页，直到取完。
2. 新版 MCP 的 `everos_get` 也能列。
   - 传 `session_id` 和 `page`，效果和第 1 条一样。
   - 旧会话里的进程还是旧代码，不能筛选。拿不准时用第 1 条。
3. 列表只返回已经整理好的记录。审查者再查两样东西。
   - 用 `POST /api/v2/memory/search`，带同样的 `filters.session_id`，`query` 填任务主题。
   - 返回里的 `unprocessed_messages` 是还在缓冲区里的内容。不是空的，就说明有写入没整理完。
   - 返回里每条记录的 `atomic_facts` 是原子事实，带编号和原文。更正要用这些编号。
4. 审查者逐条核对。
   - 每条结论有没有写明适用情况、可信程度、何时重新检查；
   - `sender_ids` 是不是这次任务用的工具；
   - 内容在不在启动记录的授权范围里。
5. 接口用不了时，可以在 WSL 里搜 Markdown 文件。
   - 位置：`~/.everos/claude-code/claude-code/users/<用户编号>/episodes/`。
   - 文件按天分，不按任务分。每条记录有一行 `**session_id**: <编号>`。
   - 这只是备用办法，结果要在任务记录里注明来自文件。
6. 写错的结论按四步更正。
   - 第一步，写入正确的结论，传 `defer_extraction: false`。
   - 第二步，用 `everos_search` 搜出新旧两条原子事实的编号，以及旧事实的原文。
   - 第三步，调用 `everos_correct_fact`，`expected_old_content` 填旧事实的原文，一字不差。
   - 第四步，再搜一次，确认旧事实不再出现。
7. 旧记录不删，EverOS 会保留更正历史。
8. 某个信息来源被证明是错的，就把"这个来源靠不靠得住"也写成一条结论。

## 8. 撤不回的 EverOS 操作

1. 下面这些操作算撤不回的行动，用之前先问用户。
   - 删除、修改、替换知识文档；
   - 对别的会话清空缓冲区，也就是调用 `/memory/flush` 或 `everos_flush`；
   - 手动触发后台整理，也就是调用 `/ome/trigger`；
   - 暂停检索服务，也就是调用 `/cascade/quiesce`。
2. 已授权的写入里，对本任务自己的 `session_id` 调 `everos_flush`，算写入的一部分，不用另外问。
3. 回退到 API 时，只用 `everos-usage.md` 列出的只读接口。

## 9. 每周报告

1. 每周一由审查者跑一次，只读，只报告，不改任何记录。
2. 范围是上周一 0 点到本周一 0 点（北京时间）写入 `claude-code` 分区的记录。
3. 报告列出四类问题。
   - 没有任务编号：`session_id` 不是 `h-YYYYMMDD-<简称>` 格式。Claude Code 钩子写的 UUID 记录单独计数，不算问题。
   - 写入方不对：`sender_ids` 里有 `unknown-client`，或者有不在已知名单里的名字。
   - 缺三件事：结论正文里没写适用情况、可信程度或何时重新检查。
   - 卡在缓冲区：某个任务编号还有没整理的内容。
4. 报告写进任务记录，再交给用户。要不要更正，由用户决定。
5. 提示词见 `rules\weekly-report-prompt.md`。

## 10. 未验证

下面三件事还没验证。试跑任务时验证，验证前不依赖它们。

1. 直接改 Markdown 文件会不会更新记忆。
2. 用 git 恢复文件以后，索引怎么重建。
3. 缓冲区里没整理的内容，会不会被同一会话后面一次正常写入顺带整理。

## 来源

| 本文 | 原文位置 | 个人改动 |
|---|---|---|
| 第 1 节 | `memory-stack` 项目 `docs\everos-usage.md` 第 3 行（自称唯一规则源） | 接口用法只引用，不重写。 |
| 第 2 节第 1、4 条 | 方案第七章第 3 条；方案第八章第 6 条（第二大脑负责第一环查经验） | 加了 `everos_kb_search` 和第二环先查知识库。 |
| 第 2 节第 1 条 `top_k` | EverOS 核查报告（2026-10-19，不在仓库里）第一节第 2 行、第二节第 8 条；WSL `~/everos-local-mcp/server.py` 第 190 到 214 行 `_kb_search` | 三个分区按名次轮流合并，不比分数，所以多取几条再看分数。 |
| 第 2 节第 2 条 | `server.py` 第 192、209 行（每条结果加 `app_id`）；`second-brain-tools` 项目 `scripts\everos_mcp_server.py` 第 3 到 5、32 行（云端旧脚本） | 2026-10-19 核实时发现第二大脑查到的是云端旧知识库，所以加了这条。 |
| 第 2 节第 6 条 | `everos-usage.md` 第 10 行 | 无。 |
| 第 3 节第 1 到 3 条 | 方案第七章第 2 条 | 无。 |
| 第 3 节第 4、5 条 | 方案第十四节 Q2 | 无。 |
| 第 3 节第 6 到 8 条 | EverOS 核查报告 第一节第 4b 行、第二节第 1 条；`server.py` 的 `_add` 和 `_flush` | 方案里没有，核查后新加。 |
| 第 4 节 | `everos\entrypoints\api\routes\memorize.py`；2026-10-19 对本机 MCP 的第一层改动 | 方案第七章第 2 条原本按任务和工具分开打标签。没有标签字段，改用 `session_id` 和 `sender_id`。任务编号格式用户已于 2026-10-19 确定。 |
| 第 5 节 | 方案第八章第 6 条；2026-10-19 对第二大脑连接方式的核实 | 第二大脑没有 MCP 连接器，所以写死只走本机接口。用户 2026-10-19 决定 Pi 算第五个 agent。 |
| 第 6 节 | `~/.claude/hooks/everos/stop-everos.py` 第 149 到 171 行；WSL `~/.pi/agent/extensions/everos.ts` 第 235、413 到 435 行 | 方案里没有。核实时发现有两个自动保存的写入方，这里把它们和结论分开。 |
| 第 7 节第 1 到 3 条 | `everos\memory\get\dto.py` 第 56 到 87 行；`everos\memory\search\dto.py` 第 71 到 114 行；`everos\memory\search\filters.py` 第 38 到 44 行；2026-10-19 16:47 实测（顶层 `session_id` 报 422，`filters.session_id` 返回 56 条，全部对得上） | 原稿只写"按 `session_id` 筛选"，没写放在 `filters` 里。 |
| 第 7 节第 5 条 | 2026-10-19 只读查看 `~/.everos/claude-code/claude-code/users/<用户编号>/episodes/` | 新加的备用办法。 |
| 第 7 节第 6、7 条 | EverOS 核查报告 第一节第 12a 行、第二节第 4 条；`routes\fact_correction.py`；`memory\search\filters.py` | 方案只写"用更正事实接口改"，这里写成四步。 |
| 第 8 节 | EverOS 核查报告 第二节第 9 条、第三节 | 按常驻规则第 4 节归为撤不回的行动。 |
| 第 9 节 | 用户 2026-10-19 选定"四层都要"中的第三层 | 方案里没有，新加。 |
| 第 10 节 | 方案第七章第 5 条；EverOS 核查报告 第五节第 2、3 条 | 无。 |
