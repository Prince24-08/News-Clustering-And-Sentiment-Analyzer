from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.vectorizer import vectorize
from src.clustering import apply_kmeans
from src.sentiment import apply_sentiment
from src.evaluation import evaluate_clustering
from src.utils import display_sample, cluster_distribution
import matplotlib.pyplot as plt

def main():
    print("Loading dataset...")
    df = load_data()

    print("Preprocessing text...")
    df = preprocess_data(df)

    print("Vectorizing (TF-IDF)...")
    X, vectorizer = vectorize(df["clean_text"])

    print("Applying K-Means...")
    labels, model = apply_kmeans(X)

    print("Performing Sentiment Analysis...")
    df = apply_sentiment(df)

    print("Evaluating...")
    df["cluster"] = labels


    cluster_names = {
        0: "Business",
        1: "General",
        2: "War/Politics",
        3: "Technology",
        4: "Health"
    }

    df["cluster_name"] = df["cluster"].map(cluster_names)

    print(df[["title", "cluster_name"]].head(10))

    print("Results:")
    display_sample(df, labels)

    
    print("\nCluster Distribution:\n")
    print(df["cluster_name"].value_counts())

  
    df["cluster_name"].value_counts().plot(kind="bar")
    plt.title("Cluster Distribution")
    plt.xlabel("Cluster Type")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()