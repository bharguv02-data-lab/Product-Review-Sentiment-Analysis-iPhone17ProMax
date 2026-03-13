import re

#  Read the saved HTML
html = open("raw.txt", "r", encoding="utf-8", errors="ignore").read()

#  Remove scripts/styles (big junk)
html = re.sub(r"(?is)<script.*?>.*?</script>", " ", html)
html = re.sub(r"(?is)<style.*?>.*?</style>", " ", html)

#  Remove all HTML tags -> plain text
text = re.sub(r"(?s)<[^>]+>", "\n", html)

#  Split into lines + basic cleanup
lines = [l.strip() for l in text.splitlines()]
lines = [l for l in lines if l]  # remove empty lines

clean = []
for l in lines:
    low = l.lower()

    # remove obvious UI / junk
    if "sort by" in low or "newest first" in low or "oldest first" in low:
        continue
    if low in {"reply", "advertisement", "video review", "reviews", "gsmarena"}:
        continue
    if "hours ago" in low or "minutes ago" in low or "days ago" in low:
        continue

    # remove very short junk
    if len(l) < 5:
        continue

    # remove code-like / location-like short tokens 
    if re.fullmatch(r"[A-Za-z0-9]{2,5}", l):
        continue

    
    if "user opinions and reviews" in low:
        continue

    

    clean.append(l)

# 5) Save cleaned reviews
open("comments.txt", "w", encoding="utf-8").write("\n".join(clean))

print("DONE. Kept reviews:", len(clean))
print("First 10:")
for x in clean[:10]:
    print("-", x[:120])
