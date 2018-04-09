# Elliptic Envelope Stats - Luis Diniz - 09/04/2018

# Goals:  - Calculte the precision, recall and accuracy rate of Elliptic Envelope with 7 features input
#         - Calculte the precision, recall and accuracy rate of Elliptic Envelope with 3 features input
#         - Calculte the precision, recall and accuracy rate of Elliptic Envelope with 2 features input
#         - Export results to csv files

# Step 1 :: Import libraries
import pandas as pd 
from sklearn.metrics import *

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
ell7 = pd.read_csv(path_out+'ellipticEnvelope7f.csv',sep='\t')
ell3 = pd.read_csv(path_out+'ellipticEnvelope3f.csv',sep='\t')
ell2 = pd.read_csv(path_out+'ellipticEnvelope2f.csv',sep='\t')
y = pd.read_csv(path_in + 'labels.csv', sep='\t')

# Step 3 :: Do calculations
crtb7 = pd.crosstab(y['label'], ell7['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb3 = pd.crosstab(y['label'], ell3['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
crtb2 = pd.crosstab(y['label'], ell2['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)

# Definition of precision :: Of all predicted y = 1, what fraction was actually y = 1?
precision_ell7 = precision_score(y['label'], ell7['0'], average='binary')
precision_ell3 = precision_score(y['label'], ell3['0'], average='binary')
precision_ell2 = precision_score(y['label'], ell2['0'], average='binary')

# Definition of recall :: Of all y = 1, what did we correct predict y = 1?
recall_ell7 = recall_score(y['label'], ell7['0'], average='binary')
recall_ell3 = recall_score(y['label'], ell3['0'], average='binary')
recall_ell2 = recall_score(y['label'], ell2['0'], average='binary')

# Definition of accuracy :: Fraction of predictions the model got right
acc_ell7 = accuracy_score(y['label'], ell7['0'], normalize=True)
acc_ell3 = accuracy_score(y['label'], ell3['0'], normalize=True)
acc_ell2 = accuracy_score(y['label'], ell2['0'], normalize=True)

#Step 4 :: Export results
crtb7.to_csv(path_out + 'ellipticEnvelope7_crosstab.csv', sep='\t')
crtb3.to_csv(path_out + 'ellipticEnvelope3_crosstab.csv', sep='\t')
crtb2.to_csv(path_out + 'ellipticEnvelope2_crosstab.csv', sep='\t')

data = [{'Precision': precision_ell7, 'Recall': recall_ell7, 'Accuracy': acc_ell7},
		{'Precision': precision_ell3, 'Recall': recall_ell3, 'Accuracy': acc_ell3},
		{'Precision': precision_ell2, 'Recall': recall_ell2, 'Accuracy': acc_ell2}]
index = ['7 Features', '3 Features', '2 Features']
metrics = pd.DataFrame(data=data, index=index)
metrics.to_csv(path_out + 'ellipticEnvelope_metrics.csv', sep='\t')
print('Data successfully exported!')