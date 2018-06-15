import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import metrics 
import numpy as np

def all_techniques(attack):
	x = [32, 7, 3, 2]

	ans = pd.read_csv('../Output/'+attack+'_results.csv', sep='\t')
	
	ee = ans['EE'].values
	hbos = ans['HBOS'].values
	isof = ans['IF'].values
	km = ans['KMeans'].values
	lof = ans['LOF'].values
	
	plt.figure()

	plt.plot(x, ee, 'r^', label = 'Elliptic Envelope')
	plt.plot(x, ee, 'k')

	plt.plot(x, hbos, 'o', label = 'HBOS')
	plt.plot(x, hbos, 'k')

	plt.plot(x, isof, 'v', label = 'Random Forests')
	plt.plot(x, isof, 'k')

	plt.plot(x, km, 'h', label = 'K Means')
	plt.plot(x, km, 'k')

	plt.plot(x, lof, 'D', label = 'LOF')
	plt.plot(x, lof, 'k')

	# Now add the legend with some customizations.
	legend = plt.legend(loc='best', shadow=True)

	# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	for label in legend.get_lines():
		label.set_linewidth(1.5)  # the legend line width
	
	plt.xlabel('# features')
	plt.ylabel('AUC')

	plt.show()

all_techniques('dos')
all_techniques('u2r')
all_techniques('r2l')
all_techniques('probe')

