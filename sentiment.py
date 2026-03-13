from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

reviews = open("comments.txt", "r", encoding="utf-8").read().splitlines()

pos = neu = neg = 0

for r in reviews:
    score = analyzer.polarity_scores(r)["compound"]
    if score >= 0.05:
        pos += 1
    elif score <= -0.05:
        neg += 1
    else:
        neu += 1

print("Total:", len(reviews))
print("Positive:", pos)
print("Neutral :", neu)
print("Negative:", neg)

import matplotlib.pyplot as plt
keywords_counts = {
    "camera": 8,
    "battery": 2,
    "performance": 8,
    "heating": 2,
    "price": 26,
    "connectivity": 2
}

plt.figure(figsize=(8,4))
plt.bar(keywords_counts.keys(), keywords_counts.values(), color="blue")
plt.title("Keyword Counts in Negative/Weakly Negative Reviews")
plt.xlabel("Keyword Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("keyword_counts.png")
plt.show()

# existing counts
labels = ["Positive", "Neutral", "Negative"]
values = [pos, neu, neg]

plt.figure(figsize=(6,4))
plt.bar(labels, values, color=["green", "gray", "red"])
plt.title("Sentiment Distribution of Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()
plt.savefig("sentiment_distribution.png", dpi=300, bbox_inches="tight")
