from collections import Counter

def display_sample(df, labels):
    df["cluster"] = labels
    print("\nSample Output:\n")
    print(df[["title", "cluster_name", "sentiment"]].head(10))

def cluster_distribution(labels):
    print("\nCluster Distribution:\n")
    print(Counter(labels))