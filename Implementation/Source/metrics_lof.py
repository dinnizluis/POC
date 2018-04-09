# LOF Performance Stats - Luis Diniz - 05/04/2018

# Goals: - Calculte the precision, recall and accuracy rate of LOF with 7 features input
#        - Calculte the precision, recall and accuracy rate of LOF with 3 features input
#        - Calculte the precision, recall and accuracy rate of LOF with 2 features input
#        - Export results to csv files

# Step 1 :: Import libraries
import pandas as pd 
from sklearn.metrics import *

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
lof7 = pd.read_csv(path_out+'lof7f.csv',sep='\t')
lof3 = pd.read_csv(path_out+'lof3f.csv',sep='\t')
lof2 = pd.read_csv(path_out+'lof2f.csv',sep='\t')
y = pd.read_csv(path_in + 'labels.csv', sep='\t')

# Step 3 :: Do calculations
crtb7 = pd.crosstab(y['label'], lof7['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb3 = pd.crosstab(y['label'], lof3['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb2 = pd.crosstab(y['label'], lof2['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)

# Definition of precision :: Of all predicted y = 1, what fraction was actually y = 1?
precision_lof7 = precision_score(y['label'], lof7['0'], average='binary')
precision_lof3 = precision_score(y['label'], lof3['0'], average='binary')
precision_lof2 = precision_score(y['label'], lof2['0'], average='binary')

# Definition of recall :: Of all y = 1, what did we correct predict y = 1?
recall_lof7 = recall_score(y['label'], lof7['0'], average='binary')
recall_lof3 = recall_score(y['label'], lof3['0'], average='binary')
recall_lof2 = recall_score(y['label'], lof2['0'], average='binary')

# Definition of accuracy :: Fraction of predictions the model got right
acc_lof7 = accuracy_score(y['label'], lof7['0'], normalize=True)
acc_lof3 = accuracy_score(y['label'], lof3['0'], normalize=True)
acc_lof2 = accuracy_score(y['label'], lof2['0'], normalize=True)

# Step 4 :: Export results
crtb7.to_csv(path_out + 'crosstabLOF7.csv', sep='\t')
crtb3.to_csv(path_out + 'crosstabLOF3.csv', sep='\t')
crtb2.to_csv(path_out + 'crosstabLOF2.csv', sep='\t')

data = [{'Precision': precision_lof7, 'Recall': recall_lof7, 'Accuracy': acc_lof7},
		{'Precision': precision_lof3, 'Recall': recall_lof3, 'Accuracy': acc_lof3},
		{'Precision': precision_lof2, 'Recall': recall_lof2, 'Accuracy': acc_lof2}]
index = ['7 Features', '3 Features', '2 Features']
metrics = pd.DataFrame(data=data, index=index)
metrics.to_csv(path_out + 'metricsLOF.csv', sep='\t')
print('Data successfully exported!')