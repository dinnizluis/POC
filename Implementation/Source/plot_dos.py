import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import metrics 
import numpy as np

def all_techniques():
	x = [32, 7, 3, 2]

	ellipticEnvelope = pd.read_csv('../Output/ellipticEnvelope_metrics.csv', sep='\t')
	y1 = ellipticEnvelope['AUC'].values

	hbos = pd.read_csv('../Output/hbos_metrics.csv', sep='\t')
	y2 = hbos['AUC'].values
	
	isolationForest = pd.read_csv('../Output/isolationForest_metrics.csv', sep='\t')
	y3 = isolationForest['AUC'].values
	
	kmeans = pd.read_csv('../Output/kmeans_metrics.csv', sep='\t')
	y4 = kmeans['AUC'].values
	
	lof = pd.read_csv('../Output/lof_metrics.csv', sep='\t')
	y5 = lof['AUC'].values

	plt.figure()
	
	plt.plot(x, y1, 'r^', label = 'Elliptic Envelope')
	plt.plot(x, y1, 'k')

	plt.plot(x, y2, 'o', label = 'HBOS')
	plt.plot(x, y2, 'k')

	plt.plot(x, y3, 'v', label = 'Random Forests')
	plt.plot(x, y3, 'k')

	plt.plot(x, y4, 'h', label = 'K Means')
	plt.plot(x, y4, 'k')

	plt.plot(x, y5, 'D', label = 'LOF')
	plt.plot(x, y5, 'k')

	# Now add the legend with some customizations.
	legend = plt.legend(loc=8, shadow=True)

	# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	for label in legend.get_lines():
		label.set_linewidth(1.5)  # the legend line width
	
	plt.xlabel('# features')
	plt.ylabel('AUC')

	plt.show()

all_techniques()

def precison_recall():
	kmeans = pd.read_csv('../Output/hbos_metrics.csv', sep='\t')
	x = kmeans['Recall'].values
	y = kmeans['Precision'].values

	plt.figure()

	plt.xlabel('Recall')
	plt.ylabel('Precision')

	plt.plot(x, y)

	plt.show()

#precison_recall()

def roc_curve(algorithm):
	algorithm = pd.read_csv('../Output/'+algorithm+'_complete.csv', sep='\t')
	labels = pd.read_csv('../Input/labels_32.csv', sep='\t')
	x = algorithm['0'].values
	y = labels['label'].values

	fpr, tpr, thresholds = metrics.roc_curve(y, x, pos_label=1)

	plt.figure()
	plt.plot(fpr, tpr, label = 'ROC Curve')
	
	legend = plt.legend(loc='best', shadow=True)
	
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	for label in legend.get_lines():
		label.set_linewidth(1.5)  # the legend line width
	
	plt.xlabel('FPR')
	plt.ylabel('TPR (sensitivity)')
	plt.show()

#roc_curve('kmeans')