from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
Y_iris = iris.target

K_means = cluster.KMeans(n_clusters = 3)
K_means.fit(X_iris)

print(K_means.labels_[::10])
print(Y_iris[::10])