from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def evaluate_clustering(df, labels):
    le = LabelEncoder()
    true_labels = le.fit_transform(df["category"])

    acc = accuracy_score(true_labels, labels)
    print("\nClustering Accuracy (approx):", acc)

    
