from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

reviews = open("comments.txt", "r", encoding="utf-8").read().splitlines()

negative_reviews = []

for r in reviews:
    score = analyzer.polarity_scores(r)["compound"]
    if score <= 0:
        negative_reviews.append(r)

print("Negative reviews:", len(negative_reviews))

# keyword counting
keywords = {
  "camera": ["camera","photo","front camera","back camera","switch","seconds","delay","zoom","telephoto"],
  "battery": ["battery","drain","mAh","charging","charge","power","battery life"],
  "performance": ["slow","lag","delay","seconds","update","ios","bug","issue"],
  "heating": ["heat","hot","overheat","warm","temperature"],
  "price": ["price","expensive","cost","worth","value"],
  "connectivity": ["esim","icloud","carplay","bluetooth"]
}


for k, words in keywords.items():
    count = 0
    for r in negative_reviews:
        if any(w in r.lower() for w in words):
            count += 1
    print(k, ":", count)
