from hbos_def import *
import pandas as pd 
import numpy as np 
from sklearn.neighbors import LocalOutlierFactor
from sklearn import preprocessing
from sklearn import cluster
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest


def run_ellipticEnvelope(x, contamination=0.1):
	clf = EllipticEnvelope(contamination=contamination, random_state=0, assume_centered=True)
	numeric_cols = [col for col in x if x[col].dtype.kind != 'O']
	x[numeric_cols] += 0.0000000001
	clf.fit(x)
	y = clf.predict(x)
	y = pd.DataFrame(data=y)
	# Change the -1 label to 0
	for index, row in y.iterrows():
		if(y[0][index] == -1):
			y[0][index] = 0

	return y

def run_hbos(x):
	hbos = HBOS()

	y = hbos.fit_predict(x)
	y = pd.DataFrame(data = y)
	dif =  (np.amax(y.values) - np.amin(y.values))/2.0
	threshold = dif + 0.5 * np.amin(y.values)
	# Change the labels to 0 and 1
	for index, row in y.iterrows():
		if(y[0][index] < threshold):
			y[0][index] = 0
		else:
			y[0][index] = 1

	return y

def run_isolationForest(x, contamination=0.1):
	max_features = x.shape[1]
	max_samples = x.shape[0]
	clf = IsolationForest(n_estimators=200, contamination=contamination, max_samples=max_samples, max_features=max_features, random_state=0, bootstrap=True)
	clf.fit(x)
	y = clf.predict(x)
	y = pd.DataFrame(data=y)
	# Change the -1 label to 0
	for index, row in y.iterrows():
		if(y[0][index] == -1):
			y[0][index] = 0

	return y

def run_kmeans(x):
	k_means = cluster.KMeans(n_clusters = 2, init='random' ,n_init=100, random_state=0)
	k_means.fit(x)
	y = pd.DataFrame(data=k_means.labels_)
	return y

def run_lof(x, contamination=0.1):
	#Fit the model
	clf = LocalOutlierFactor(n_neighbors=20, contamination=contamination)
	y = clf.fit_predict(x)
	y = pd.DataFrame(data=y)
	# Change the -1 label to 0
	for index, row in y.iterrows():
		if(y[0][index] == -1):
			y[0][index] = 0

	return y

def get_results(technique, inpt, exp='n', attack='none', contamination=0.1):
	if technique == 1: #Elliptic Envelope
		print("Started run for "+attack+" attacks on Elliptic Envelope")
		ee_32 = run_ellipticEnvelope(inpt[0], contamination)
		ee_7 = run_ellipticEnvelope(inpt[1], contamination)
		ee_3 = run_ellipticEnvelope(inpt[2], contamination)
		ee_2 = run_ellipticEnvelope(inpt[3], contamination)
		results_ee = pd.DataFrame()
		results_ee[0] = ee_32[0]
		results_ee[1] = ee_7[0]
		results_ee[2] = ee_3[0]
		results_ee[3] = ee_2[0]
		results_ee.columns = ['32', '7', '3', '2']
		if exp == 's':
			results_ee.to_csv('../Output/'+attack+'_ee.csv', sep='\t', index=False)
			print('Results sucessfully exported to: ../Output/'+attack+'_ee.csv')
		return results_ee

	elif technique == 2: #HBOS
		print("Started run for "+attack+" attacks on HBOS")
		hbos_32 = run_hbos(inpt[0])
		hbos_7 = run_hbos(inpt[1])
		hbos_3 = run_hbos(inpt[2])
		hbos_2 = run_hbos(inpt[3])
		results_hbos = pd.DataFrame()
		results_hbos[0] = hbos_32[0]
		results_hbos[1] = hbos_7[0]
		results_hbos[2] = hbos_3[0]
		results_hbos[3] = hbos_2[0]
		results_hbos.columns = ['32', '7', '3', '2']
		if exp == 's':
			results_hbos.to_csv('../Output/'+attack+'_hbos.csv', sep='\t', index=False)
			print('Results sucessfully exported to: ../Output/'+attack+'_hbos.csv')
		return results_hbos

	elif technique == 3: #Isolation Forests
		print("Started run for "+attack+" attacks on Random Forests")
		if_32 = run_isolationForest(inpt[0], contamination)
		if_7 = run_isolationForest(inpt[1], contamination)
		if_3 = run_isolationForest(inpt[2], contamination)
		if_2 = run_isolationForest(inpt[3], contamination)
		results_if = pd.DataFrame()
		results_if[0] = if_32[0]
		results_if[1] = if_7[0]
		results_if[2] = if_3[0]
		results_if[3] = if_2[0]
		results_if.columns = ['32', '7', '3', '2']
		if exp == 's':
			results_if.to_csv('../Output/'+attack+'_if.csv', sep='\t', index=False)
			print('Results sucessfully exported to: ../Output/'+attack+'_if.csv')
		return results_if

	elif technique == 4: #K Means
		print("Started run for "+attack+" attacks on K Means")
		k_32 = run_kmeans(inpt[0])
		k_7 = run_kmeans(inpt[1])
		k_3 = run_kmeans(inpt[2])
		k_2 = run_kmeans(inpt[3])
		results_kmeans = pd.DataFrame()
		results_kmeans[0] = k_32[0]
		results_kmeans[1] = k_7[0]
		results_kmeans[2] = k_3[0]
		results_kmeans[3] = k_2[0]
		results_kmeans.columns = ['32', '7', '3', '2']
		if exp == 's':
			results_kmeans.to_csv('../Output/'+attack+'_kmeans.csv', sep='\t', index=False)
			print('Results sucessfully exported to: ../Output/'+attack+'_kmeans.csv')
		return results_kmeans

	elif technique == 5: #LOF
		print("Started run for "+attack+" attacks on LOF")
		lof_32 = run_lof(inpt[0], contamination)
		lof_7 = run_lof(inpt[1], contamination)
		lof_3 = run_lof(inpt[2], contamination)
		lof_2 = run_lof(inpt[3], contamination)
		results_lof = pd.DataFrame()
		results_lof[0] = lof_32[0]
		results_lof[1] = lof_7[0]
		results_lof[2] = lof_3[0]
		results_lof[3] = lof_2[0]
		results_lof.columns = ['32', '7', '3', '2']
		if exp == 's':
			results_lof.to_csv('../Output/'+attack+'_lof.csv', sep='\t', index=False)
			print('Results sucessfully exported to: ../Output/'+attack+'_lof.csv')
		return results_lof

	else:
		print("INVALID TECHNIQUE!")  