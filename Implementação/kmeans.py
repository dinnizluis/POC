import pandas as pd
from sklearn import cluster

#Loading the dataset
df = pd.read_csv("KDDTest+_probe_no_label.csv", sep='\t') 
#df = pd.read_csv("KDDTrain+_20Percent_pcd_no_label.csv", sep='\t') 
y = pd.read_csv("KDDTest+_probe.csv", sep='\t')

k_means = cluster.KMeans(n_clusters = 2)
k_means.fit(df)

n_rows, n_cols = df.shape
correct = 0
for i in range(0, n_rows):
	if(y['label'][i] == k_means.labels_[i]):
		correct += 1

rate = (correct/n_rows)*100
print("rate = ", rate)