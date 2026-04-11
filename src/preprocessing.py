import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def preprocess_data(df):

    df.columns = df.columns.str.lower().str.strip()

    if "title" in df.columns and "description" in df.columns:
        df["text"] = df["title"] + " " + df["description"]
    elif "description" in df.columns:
        df["text"] = df["description"]
    elif "title" in df.columns:
        df["text"] = df["title"]
    else:
        raise Exception(f"No usable text column found. Columns: {df.columns}")

    df["clean_text"] = df["text"].apply(clean_text)

    return df