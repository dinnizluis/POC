# ISOLATION FOREST - Luis Diniz - 09/04/2018


# * Return the anomaly score of each sample using the IsolationForest algorithm
# * The IsolationForest ‘isolates’ observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature.
# * Since recursive partitioning can be represented by a tree structure, the number of splittings required to isolate a sample is equivalent to the path length from the root node to the terminating node.
# * This path length, averaged over a forest of such random trees, is a measure of normality and our decision function.
# * Random partitioning produces noticeably shorter paths for anomalies. Hence, when a forest of random trees collectively produce shorter path lengths for particular samples, they are highly likely to be anomalies.


# Goals: - Perform anomaly detection using Isolation Forest with the processed data

# Step 1 :: Import libraries
from sklearn.ensemble import IsolationForest
import pandas as pd 

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x = pd.read_csv(path_in + 'nslkdd_complete.csv', sep='\t')
x_7d = pd.read_csv(path_in + 'nslkdd_7f.csv', sep='\t')
x_3d = pd.read_csv(path_in + 'nslkdd_3f.csv', sep='\t')
x_2d = pd.read_csv(path_in + 'nslkdd_2f.csv', sep='\t')

# Step 3 :: Fit the model
clf = IsolationForest(n_estimators=200, contamination=0.4, max_samples=130146, max_features=7, random_state=0, bootstrap=True)
clf.fit(x)
y = clf.predict(x)
y = pd.DataFrame(data=y)
# Change the -1 label to 0
for index, row in y.iterrows():
	if(y[0][index] == -1):
		y[0][index] = 0

clf = IsolationForest(n_estimators=200, contamination=0.4, max_samples=130146, max_features=7, random_state=0, bootstrap=True)
clf.fit(x_7d)
y_7d = clf.predict(x_7d)
y_7d = pd.DataFrame(data=y_7d)
# Change the -1 label to 0
for index, row in y_7d.iterrows():
	if(y_7d[0][index] == -1):
		y_7d[0][index] = 0

clf = IsolationForest(n_estimators=200, contamination=0.4, max_samples=130146, max_features=3, random_state=0, bootstrap=True)
clf.fit(x_3d)
y_3d = clf.predict(x_3d)
y_3d = pd.DataFrame(data=y_3d)
# Change the -1 label to 0
for index, row in y_3d.iterrows():
	if(y_3d[0][index] == -1):
		y_3d[0][index] = 0

clf = IsolationForest(n_estimators=200, contamination=0.4, max_samples=130146, max_features=2, random_state=0, bootstrap=True)
clf.fit(x_2d)
y_2d = clf.predict(x_2d)
y_2d = pd.DataFrame(data=y_2d)
# Change the -1 label to 0
for index, row in y_2d.iterrows():
	if(y_2d[0][index] == -1):
		y_2d[0][index] = 0

# Step 4 :: Export results
y.to_csv(path_out + 'isolationForest_complete.csv', sep='\t', index=False)
y_7d.to_csv(path_out + 'isolationForest7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out + 'isolationForest3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out + 'isolationForest2f.csv', sep='\t', index=False)
print('Data successfully exported!')

# Calculate the performance of the algorithm
from metrics import *

algorithm_name = 'isolationForest'
metrics, crtb, crtb7, crtb3, crtb2 = performance(algorithm_name)

crtb.to_csv(path_out + algorithm_name + '32_crosstab.csv', sep='\t')
crtb7.to_csv(path_out + algorithm_name + '7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + algorithm_name + '3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + algorithm_name + '2_crosstab.csv', sep='\t')
metrics.to_csv(path_out + algorithm_name +'_metrics.csv', sep='\t')
print('Data successfully exported - stats!')

