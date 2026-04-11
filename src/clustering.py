from sklearn.cluster import KMeans

def apply_kmeans(X, k=5):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    return labels, model