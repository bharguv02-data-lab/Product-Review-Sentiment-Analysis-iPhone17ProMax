# Product-Review-Sentiment-Analysis-iPhone17ProMax
# Product Review Sentiment Analysis — iPhone 17 Pro Max

This project analyzes user opinions and reviews of the Apple iPhone 17 Pro Max using Natural Language Processing (NLP).

The dataset was collected from GSMArena user reviews.

## Project Pipeline

1. Raw review data extracted from GSMArena
2. HTML and UI text cleaned
3. Reviews filtered and structured
4. Sentiment analysis using VADER
5. Issue detection through keyword analysis

## Technologies Used

Python  
VADER Sentiment Analysis  
Matplotlib  

## Key Insights

Most negative feedback focuses on:

- Price
- Camera issues
- Performance delays

## Output Visualizations

- Sentiment distribution chart
- Keyword frequency in negative reviews
## Project Structure

`clean2.py`  
Extracts and cleans raw HTML review data from GSMArena.

`clean.py`  
Filters and refines extracted review text to remove UI elements and noise.

`sentiment.py`  
Performs sentiment analysis using VADER and generates the sentiment distribution visualization.

`insights.py`  
Identifies common complaint categories (camera, battery, performance, price, etc.) using keyword analysis.

`raw.txt`  
Raw HTML page containing GSMArena user reviews.

`comments.txt`  
Cleaned dataset containing only extracted review text.

`sentiment_distribution.png`  
Visualization showing the distribution of positive, neutral, and negative reviews.

`keyword_counts.png`  
Visualization showing the most common complaint keywords.
