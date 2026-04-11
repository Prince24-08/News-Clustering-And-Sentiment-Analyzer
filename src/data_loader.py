import pandas as pd

def load_data(path="data/bbc-text.csv"):
    df = pd.read_csv(path)
    return df