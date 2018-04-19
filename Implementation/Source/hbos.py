#Step 1 :: Import libraries
from hbos_def import *
import pandas as pd 
from sklearn import preprocessing
import numpy as np 

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x_7d = pd.read_csv(path_in + 'nslkdd.csv', sep='\t')
x_3d = pd.read_csv(path_out + 'nslkdd3d.csv', sep='\t')
x_2d = pd.read_csv(path_out + 'nslkdd2d.csv', sep='\t')

hbos = HBOS()

y_7d = hbos.fit_predict(x_7d)
y_7d = pd.DataFrame(data=y_7d)
dif =  (np.amax(y_7d.values) - np.amin(y_7d.values))/2.0
threshold = dif + 0.5 * np.amin(y_7d.values)
# Change the labels to 0 and 1
for index, row in y_7d.iterrows():
	if(y_7d[0][index] < threshold):
		y_7d[0][index] = 0
	else:
		y_7d[0][index] = 1

y_3d = hbos.fit_predict(x_3d)
y_3d = pd.DataFrame(data=y_3d)
dif =  (np.amax(y_3d.values) - np.amin(y_3d.values))/2.0
threshold = dif + 0.5 * np.amin(y_3d.values)
# Change the labels to 0 and 1
for index, row in y_3d.iterrows():
	if(y_3d[0][index] < threshold):
		y_3d[0][index] = 0
	else:
		y_3d[0][index] = 1

y_2d = hbos.fit_predict(x_2d)
y_2d = pd.DataFrame(data=y_2d)
dif =  (np.amax(y_2d.values) - np.amin(y_2d.values))/2.0
threshold = dif + 0.5 * np.amin(y_2d.values)
# Change the labels to 0 and 1
for index, row in y_2d.iterrows():
	if(y_2d[0][index] < threshold):
		y_2d[0][index] = 0
	else:
		y_2d[0][index] = 1

# Step 4 :: Export results
y_7d.to_csv(path_out + 'hbos7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out + 'hbos3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out + 'hbos2f.csv', sep='\t', index=False)
print('Data successfully exported!')

# Calculate the performance of the algorithm
from metrics import *

algorithm_name = 'hbos'
metrics, crtb7, crtb3, crtb2 = performance(algorithm_name)

crtb7.to_csv(path_out + algorithm_name + '7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + algorithm_name + '3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + algorithm_name + '2_crosstab.csv', sep='\t')
metrics.to_csv(path_out + algorithm_name +'_metrics.csv', sep='\t')
print('Data successfully exported - stats!')