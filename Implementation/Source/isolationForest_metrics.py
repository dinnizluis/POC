# Isolation Forest Stats - Luis Diniz - 09/04/2018

# Goals:  - Calculte the precision, recall and accuracy rate of Isolation Forest with 7 features input
#        - Calculte the precision, recall and accuracy rate of Isolation Forest with 3 features input
#        - Calculte the precision, recall and accuracy rate of Isolation Forest with 2 features input
#        - Export results to csv files

# Step 1 :: Import libraries
import pandas as pd 
from sklearn.metrics import *

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
isof7 = pd.read_csv(path_out+'lof7f.csv',sep='\t')
isof3 = pd.read_csv(path_out+'lof3f.csv',sep='\t')
isof2 = pd.read_csv(path_out+'lof2f.csv',sep='\t')
y = pd.read_csv(path_in + 'labels.csv', sep='\t')

# Step 3 :: Do calculations
crtb7 = pd.crosstab(y['label'], isof7['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb3 = pd.crosstab(y['label'], isof3['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb2 = pd.crosstab(y['label'], isof2['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)

# Definition of precision :: Of all predicted y = 1, what fraction was actually y = 1?
precision_isof7 = precision_score(y['label'], isof7['0'], average='binary')
precision_isof3 = precision_score(y['label'], isof3['0'], average='binary')
precision_isof2 = precision_score(y['label'], isof2['0'], average='binary')

# Definition of recall :: Of all y = 1, what did we correct predict y = 1?
recall_isof7 = recall_score(y['label'], isof7['0'], average='binary')
recall_isof3 = recall_score(y['label'], isof3['0'], average='binary')
recall_isof2 = recall_score(y['label'], isof2['0'], average='binary')

# Definition of accuracy :: Fraction of predictions the model got right
acc_isof7 = accuracy_score(y['label'], isof7['0'], normalize=True)
acc_isof3 = accuracy_score(y['label'], isof3['0'], normalize=True)
acc_isof2 = accuracy_score(y['label'], isof2['0'], normalize=True)

#Step 4 :: Export results
crtb7.to_csv(path_out + 'isolationForest7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + 'isolationForest3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + 'isolationForest2_crosstab.csv', sep='\t')

data = [{'Precision': precision_isof7, 'Recall': recall_isof7, 'Accuracy': acc_isof7},
		{'Precision': precision_isof3, 'Recall': recall_isof3, 'Accuracy': acc_isof3},
		{'Precision': precision_isof2, 'Recall': recall_isof2, 'Accuracy': acc_isof2}]
index = ['7 Features', '3 Features', '2 Features']
metrics = pd.DataFrame(data=data, index=index)
metrics.to_csv(path_out + 'isolationForest_metrics.csv', sep='\t')
print('Data successfully exported!')