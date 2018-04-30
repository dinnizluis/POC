# LOCAL OUTLIER FACTOR - Luis Diniz - 05/04/2018

# Goals: - Perform anomaly detection using LOF with the processed data

# Step 1 :: Import libraries
import pandas as pd 
import numpy as np 
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt 

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x = pd.read_csv(path_in + 'nslkdd_complete.csv', sep='\t')
x_7d = pd.read_csv(path_in + 'nslkdd_7f.csv', sep='\t')
x_3d = pd.read_csv(path_in + 'nslkdd_3f.csv', sep='\t')
x_2d = pd.read_csv(path_in + 'nslkdd_2f.csv', sep='\t')

# Step 3 :: Fit the model
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.4)

y = clf.fit_predict(x)
y = pd.DataFrame(data=y)
# Change the -1 label to 0
for index, row in y.iterrows():
	if(y[0][index] == -1):
		y[0][index] = 0

y_7d = clf.fit_predict(x_7d)
y_7d = pd.DataFrame(data=y_7d)
# Change the -1 label to 0
for index, row in y_7d.iterrows():
	if(y_7d[0][index] == -1):
		y_7d[0][index] = 0

y_3d = clf.fit_predict(x_3d)
y_3d = pd.DataFrame(data=y_3d)
# Change the -1 label to 0
for index, row in y_3d.iterrows():
	if(y_3d[0][index] == -1):
		y_3d[0][index] = 0

y_2d = clf.fit_predict(x_2d)
y_2d = pd.DataFrame(data=y_2d)
# Change the -1 label to 0
for index, row in y_2d.iterrows():
	if(y_2d[0][index] == -1):
		y_2d[0][index] = 0


# Step 4 :: Export results
y.to_csv(path_out + 'lof_complete.csv', sep='\t', index=False)
y_7d.to_csv(path_out + 'lof7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out + 'lof3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out + 'lof2f.csv', sep='\t', index=False)
print('Data successfully exported!')

# Calculate the performance of the algorithm
from metrics import *

algorithm_name = 'lof'
metrics, crtb, crtb7, crtb3, crtb2 = performance(algorithm_name)

crtb.to_csv(path_out + algorithm_name + '32_crosstab.csv', sep='\t')
crtb7.to_csv(path_out + algorithm_name + '7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + algorithm_name + '3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + algorithm_name + '2_crosstab.csv', sep='\t')
metrics.to_csv(path_out + algorithm_name +'_metrics.csv', sep='\t')
print('Data successfully exported - stats!')
