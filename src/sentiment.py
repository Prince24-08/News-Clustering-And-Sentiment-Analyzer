from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    return "Neutral"

def apply_sentiment(df):
    df["sentiment"] = df["text"].apply(get_sentiment)
    return df