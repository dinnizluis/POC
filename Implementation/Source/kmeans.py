#KMeans - Luis Diniz - 11/04/2018

#Goals: - Run KMeans with 7 features indicated [see reference]
#		- Run KMeans with 3 features indicated
#       - Run KMeans with 2 features indicated
#       - Export results to csv file

#Step 1 :: Import libraries
from sklearn import cluster
import pandas as pd 

#Step 2 :: Load data
path_in = '../Input/'
path_out = '../Output/'
x = pd.read_csv(path_in + 'nslkdd_complete.csv', sep='\t')
x_7d = pd.read_csv(path_in + 'nslkdd_7f.csv', sep='\t')
x_3d = pd.read_csv(path_in + 'nslkdd_3f.csv', sep='\t')
x_2d = pd.read_csv(path_in + 'nslkdd_2f.csv', sep='\t')

#Step 3 :: Execute KMeans
k_means = cluster.KMeans(n_clusters = 2, init='random' ,n_init=100, random_state=0)

k_means.fit(x)
y = pd.DataFrame(data=k_means.labels_)

k_means.fit(x_7d)
y_7d = pd.DataFrame(data=k_means.labels_)

k_means.fit(x_3d)
y_3d = pd.DataFrame(data=k_means.labels_)

k_means.fit(x_2d)
y_2d = pd.DataFrame(data=k_means.labels_)

#Step 4 :: Export results
y.to_csv(path_out+'kmeans_complete.csv', sep='\t', index=False)
y_7d.to_csv(path_out+'kmeans7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out+'kmeans3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out+'kmeans2f.csv', sep='\t', index=False)
print('Data successfully exported!')

# Calculate the performance of the algorithm
from metrics import *

algorithm_name = 'kmeans'
metrics, crtb, crtb7, crtb3, crtb2 = performance(algorithm_name)

crtb.to_csv(path_out + algorithm_name + '32_crosstab.csv', sep='\t')
crtb7.to_csv(path_out + algorithm_name + '7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + algorithm_name + '3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + algorithm_name + '2_crosstab.csv', sep='\t')
metrics.to_csv(path_out + algorithm_name +'_metrics.csv', sep='\t')
print('Data successfully exported - stats!')