from metrics import *

algorithm_name = ['kmeans', 'isolationForest', 'lof', 'ellipticEnvelope', 'hbos']

for i in range(0, len(algorithm_name)):
	metrics, crtb7, crtb3, crtb2 = performance(algorithm_name[i])

	crtb7.to_csv(path_out + algorithm_name[i] + '7_crosstab.csv', sep='\t')
	crtb3.to_csv(path_out + algorithm_name[i] + '3_crosstab.csv', sep='\t')
	crtb2.to_csv(path_out + algorithm_name[i] + '2_crosstab.csv', sep='\t')
	metrics.to_csv(path_out + algorithm_name[i] +'_metrics.csv', sep='\t')
	print('Data successfully exported!')