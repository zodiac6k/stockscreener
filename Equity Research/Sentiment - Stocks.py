import pandas as pd
from textblob import TextBlob

# Load your portfolio
portfolio = pd.read_csv('my_news.csv', sep='\t')

# Load the news dataset (CSV with Top1–Top25 columns)
news = pd.read_csv('Combined_News_DJIA.csv')

# Combine all Top1–Top25 columns into a single DataFrame column
top_cols = [col for col in news.columns if col.startswith('Top')]
news_long = news.melt(id_vars=['Date', 'Label'], value_vars=top_cols, var_name='Top', value_name='Headline')
news_long = news_long.dropna(subset=['Headline'])

# Sentiment function
def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

news_long['sentiment'] = news_long['Headline'].apply(get_sentiment)

# For each stock, find matching headlines and calculate average sentiment
def stock_sentiment(stock_name):
    matches = news_long[news_long['Headline'].str.contains(stock_name, case=False, na=False)]
    if not matches.empty:
        return matches['sentiment'].mean()
    else:
        return None

portfolio['sentiment'] = portfolio['Stock Name'].apply(stock_sentiment)

# Save results
portfolio.to_csv('portfolio_with_sentiment.csv', index=False)
print(portfolio[['Stock Name', 'sentiment']].head())