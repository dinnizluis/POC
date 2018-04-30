# ELLIPTIC ENVELOPE - Luis Diniz - 09/04/2018

# Goals: - Perform anomaly detection using Elliptic Envelope with the processed data

# Step 1 :: Import libraries
from sklearn.covariance import EllipticEnvelope
import pandas as pd 

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x = pd.read_csv(path_in + 'nslkdd_complete.csv', sep='\t')
x_7d = pd.read_csv(path_in + 'nslkdd_7f.csv', sep='\t')
x_3d = pd.read_csv(path_in + 'nslkdd_3f.csv', sep='\t')
x_2d = pd.read_csv(path_in + 'nslkdd_2f.csv', sep='\t')

# Step 3 :: Fit the data
clf = EllipticEnvelope(contamination=0.4, random_state=0, assume_centered=True)
clf.fit(x)
y = clf.predict(x)
y = pd.DataFrame(data=y)
# Change the -1 label to 0
for index, row in y.iterrows():
	if(y[0][index] == -1):
		y[0][index] = 0

clf = EllipticEnvelope(contamination=0.4, random_state=0, assume_centered=True)
clf.fit(x_7d)
y_7d = clf.predict(x_7d)
y_7d = pd.DataFrame(data=y_7d)
# Change the -1 label to 0
for index, row in y_7d.iterrows():
	if(y_7d[0][index] == -1):
		y_7d[0][index] = 0

clf.fit(x_3d)
y_3d = clf.predict(x_3d)
y_3d = pd.DataFrame(data=y_3d)
# Change the -1 label to 0
for index, row in y_3d.iterrows():
	if(y_3d[0][index] == -1):
		y_3d[0][index] = 0

clf.fit(x_2d)
y_2d = clf.predict(x_2d)
y_2d = pd.DataFrame(data=y_2d)
# Change the -1 label to 0
for index, row in y_2d.iterrows():
	if(y_2d[0][index] == -1):
		y_2d[0][index] = 0

# Step 4 :: Export results
y.to_csv(path_out + 'ellipticEnvelope_complete.csv', sep='\t', index=False)
y_7d.to_csv(path_out + 'ellipticEnvelope7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out + 'ellipticEnvelope3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out + 'ellipticEnvelope2f.csv', sep='\t', index=False)
print('Data successfully exported!')

# Calculate the performance of the algorithm
from metrics import *

algorithm_name = 'ellipticEnvelope'
metrics, crtb, crtb7, crtb3, crtb2 = performance(algorithm_name)

crtb.to_csv(path_out + algorithm_name + '32_crosstab.csv', sep='\t')
crtb7.to_csv(path_out + algorithm_name + '7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + algorithm_name + '3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + algorithm_name + '2_crosstab.csv', sep='\t')
metrics.to_csv(path_out + algorithm_name +'_metrics.csv', sep='\t')
print('Data successfully exported - stats!')
