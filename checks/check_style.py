import re, sys
BANNED = ["→", "->", "=>", "——", "—", "–", "……", "...", "显然", "当然", "我认为", "我觉得", "等等", "毋庸置疑"]
total = 0
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    body = re.sub(r"`[^`]*`", "", text)  # 代码和路径不算
    hits = []
    for w in BANNED:
        for m in re.finditer(re.escape(w), body):
            line = body[:m.start()].count("\n") + 1
            hits.append(f"  第 {line} 行含有「{w}」")
    for i, ln in enumerate(body.splitlines(), 1):
        if ln.startswith("|"):
            continue
        for sent in re.split(r"[。！？]", ln):
            s = re.sub(r"^[\s\-\d\.#*]+", "", sent)
            if len(s) > 80:
                hits.append(f"  第 {i} 行有一句 {len(s)} 字：{s[:30]}……")
    total += len(hits)
    print(f"{path}: {len(hits)} 处")
    print("\n".join(hits))
print("合计", total, "处")
