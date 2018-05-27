#Performance calculation - Luis Diniz - 11/04/2018

import pandas as pd 
from sklearn.metrics import *

# Step 2 :: Load data
path_in = '../Implementation/Input/'
path_out = '../Output/'

def performance(algorithm_name, path_in=path_in, path_out=path_out, y='labels', label='label', pred='0'):
	x = pd.read_csv(path_out+algorithm_name+'_complete.csv', sep='\t')
	x7 = pd.read_csv(path_out+algorithm_name+'7f.csv',sep='\t')
	x3 = pd.read_csv(path_out+algorithm_name+'3f.csv',sep='\t')
	x2 = pd.read_csv(path_out+algorithm_name+'2f.csv',sep='\t')
	y = pd.read_csv(path_in + 'labels.csv', sep='\t')
	y_32 = pd.read_csv(path_in + 'labels_32.csv', sep='\t')

	# Step 3 :: Do calculations
	crtb = pd.crosstab(y_32['label'], x['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
	crtb7 = pd.crosstab(y['label'], x7['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
	crtb3 = pd.crosstab(y['label'], x3['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)
	crtb2 = pd.crosstab(y['label'], x2['0'], rownames=['Observed'], colnames=['Predicted'], margins=True)

	# Definition of precision :: Of all predicted y = 1, what fraction was actually y = 1?
	precision_x = precision_score(y_32['label'], x['0'], average='binary')
	precision_x7 = precision_score(y['label'], x7['0'], average='binary')
	precision_x3 = precision_score(y['label'], x3['0'], average='binary')
	precision_x2 = precision_score(y['label'], x2['0'], average='binary')

	# Definition of recall :: Of all y = 1, what did we correct predict y = 1?
	recall_x = recall_score(y_32['label'], x['0'], average='binary')
	recall_x7 = recall_score(y['label'], x7['0'], average='binary')
	recall_x3 = recall_score(y['label'], x3['0'], average='binary')
	recall_x2 = recall_score(y['label'], x2['0'], average='binary')

	# Definition of accuracy :: Fraction of predictions the model got right
	acc_x = accuracy_score(y_32['label'], x['0'], normalize=True)
	acc_x7 = accuracy_score(y['label'], x7['0'], normalize=True)
	acc_x3 = accuracy_score(y['label'], x3['0'], normalize=True)
	acc_x2 = accuracy_score(y['label'], x2['0'], normalize=True)

	# Area Under the ROC Curve
	auc_x = roc_auc_score(y_32['label'], x['0'])
	auc_x7 = roc_auc_score(y['label'], x7['0'])
	auc_x3 = roc_auc_score(y['label'], x3['0'])
	auc_x2 = roc_auc_score(y['label'], x2['0'])

	data = [{'Precision': precision_x, 'Recall': recall_x, 'Accuracy': acc_x, 'AUC': auc_x},
			{'Precision': precision_x7, 'Recall': recall_x7, 'Accuracy': acc_x7, 'AUC': auc_x7},
			{'Precision': precision_x3, 'Recall': recall_x3, 'Accuracy': acc_x3, 'AUC': auc_x3},
			{'Precision': precision_x2, 'Recall': recall_x2, 'Accuracy': acc_x2, 'AUC': auc_x2}]
	index = ['32 Features', '7 Features', '3 Features', '2 Features']
	metrics = pd.DataFrame(data=data, index=index)
	return metrics, crtb, crtb7, crtb3, crtb2