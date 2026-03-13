import re

text = open("raw.txt", "r", encoding="utf-8", errors="ignore").read()

lines = [l.strip() for l in text.splitlines() if l.strip()]

clean = []
for l in lines:
    low = l.lower()
    if "sort by" in low or "reply" in low or "hours ago" in low:
        continue
    if len(l) < 15:
        continue
    clean.append(l)

open("comments.txt", "w", encoding="utf-8").write("\n".join(clean))
print("DONE:", len(clean))
