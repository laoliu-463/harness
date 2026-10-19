import sys
root = sys.argv[1]
bad = 0
for row in open(sys.argv[2], encoding="utf-8"):
    f, n, needle = row.rstrip("\n").split("\t")
    lines = open(f"{root}/{f}", encoding="utf-8").read().splitlines()
    line = lines[int(n) - 1] if int(n) <= len(lines) else ""
    ok = needle in line
    bad += not ok
    print(("OK  " if ok else "FAIL"), f, n, needle if ok else f"{needle!r} not in {line[:80]!r}")
print("failures:", bad)
