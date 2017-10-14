# Import KMeans
from sklearn.cluster import KMeans 

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3)

# Fit model to points (points is the array with the data)
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)

#The output should be an array with the labels of each sample (0, 1 or 2)