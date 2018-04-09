# Script 9 - Luis Diniz - 31/03/2018

# Goals: - Calculte the precision, recall and accuracy rate of KMeans with 7 features input
#        - Calculte the precision, recall and accuracy rate of KMeans with 3 features input
#        - Calculte the precision, recall and accuracy rate of KMeans with 2 features input
#        - Export results to csv files

# Step 1 :: Import libraries
import pandas as pd
from sklearn.metrics import *

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
k2 = pd.read_csv(path_out + 'kmeans2f.csv', sep='\t')
k3 = pd.read_csv(path_out + 'kmeans3f.csv', sep='\t')
k7 = pd.read_csv(path_out + 'kmeans7f.csv', sep='\t')
y = pd.read_csv(path_in + 'labels.csv', sep='\t')

# Step 3 :: Do calculations

# Cross tabulation table
crtb7 = pd.crosstab(y['label'], k7['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb3 = pd.crosstab(y['label'], k3['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb2 = pd.crosstab(y['label'], k2['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)

# Definition of precision :: Of all predicted y = 1, what fraction was actually y = 1?
precisionk7 = precision_score(y['label'], k7['0'], average='binary')
precisionk3 = precision_score(y['label'], k3['0'], average='binary')
precisionk2 = precision_score(y['label'], k2['0'], average='binary')

# Definition of recall :: Of all y = 1, what did we correct predict y = 1?
recallk7 = recall_score(y['label'], k7['0'], average='binary')
recallk3 = recall_score(y['label'], k3['0'], average='binary')
recallk2 = recall_score(y['label'], k2['0'], average='binary')

# Definition of accuracy :: Fraction of predictions the model got right
acck7 = accuracy_score(y['label'], k7['0'], normalize=True)
acck3 = accuracy_score(y['label'], k3['0'], normalize=True)
acck2 = accuracy_score(y['label'], k2['0'], normalize=True)

# Step 4 :: Export results

crtb7.to_csv(path_out + 'crosstabKmeans7.csv', sep='\t')
crtb3.to_csv(path_out + 'crosstabKmeans3.csv', sep='\t')
crtb2.to_csv(path_out + 'crosstabKmeans2.csv', sep='\t')

data = [{'Precision': precisionk7, 'Recall': recallk7, 'Accuracy': acck7},
		{'Precision': precisionk3, 'Recall': recallk3, 'Accuracy': acck3},
		{'Precision': precisionk2, 'Recall': recallk2, 'Accuracy': acck2}]
index = ['7 Features', '3 Features', '2 Features']
metrics = pd.DataFrame(data=data, index=index)
metrics.to_csv(path_out + 'metricsKmeans.csv', sep='\t')
print('Data successfully exported!')