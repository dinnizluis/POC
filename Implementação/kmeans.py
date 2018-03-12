import pandas as pd
from sklearn import cluster

#Loading the dataset
df = pd.read_csv("20Percent_5_labels.csv", sep='\t') 
#df = pd.read_csv("KDDTrain+_20Percent_pcd_no_label.csv", sep='\t') 
y = pd.read_csv("KDDTrain+_20Percent_pcd.csv", sep='\t')

print(df.shape)
k_means = cluster.KMeans(n_clusters = 5)
k_means.fit(df)

n_rows, n_cols = df.shape
print(k_means.labels_)
correct = 0
#for i in range(0, n_rows):
#	if(y['label'][i] == k_means.labels_[i]):
#		correct += 1

#print(correct)
#rate = (correct/n_rows)*100
#print("rate = ", rate)