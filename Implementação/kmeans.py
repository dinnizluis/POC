import pandas as pd
from sklearn import cluster

#Loading the dataset
df = pd.read_csv("KDD_DoS_pca.csv", sep='\t') 
#df = pd.read_csv("KDDTrain+_20Percent_pcd_no_label.csv", sep='\t') 
y = pd.read_csv("KDD_DoS_pca_label.csv", sep='\t')

print(y.columns)

k_means = cluster.KMeans(n_clusters = 2)
k_means.fit(df)

n_rows, n_cols = df.shape
correct = 0
wrong = 0
for i in range(0, n_rows):
	if(y['label'][i] == k_means.labels_[i]):
		correct += 1
	else:
		wrong += 1

rate = (correct/n_rows)*100
print("rate = ", rate)

#Script to plot the orginal data

# Luis Diniz  - 19/03/2018 [UFV]_v1

from pylab import *
import matplotlib.pyplot as plt 

x1 = []
y1 = []
x2 = []
y2 = []
regular_k = 0
probe_k = 0
for index, row in df.iterrows():
	if(k_means.labels_[index] == 1):
		probe_k += 1
		x1.append(df.columns[[0]][index])
		y1.append(df.columns[[1]][index])
	else:
		regular_k += 1
		x2.append(df.columns[[0]][index])
		y2.append(df.columns[[1]][index])

figure()
plot(x1, y1, 'r+')
plot(x2, y2, 'bo')
xlabel('F1')
ylabel('F2')
xscale('log')
yscale('log')
title('K Means')
show()