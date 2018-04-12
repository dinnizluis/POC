#KMeans - Luis Diniz - 11/04/2018

#Goals: - Run KMeans with 7 features indicated [see reference]
#		- Run KMeans with 3 features indicated
#       - Run KMeans with 2 features indicated
#       - Export results to csv file

#Step 1 :: Import libraries
from sklearn import cluster
import pandas as pd 

#Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x_7d = pd.read_csv(path_in + 'nslkdd.csv', sep='\t')
x_3d = pd.read_csv(path_out + 'nslkdd3d.csv', sep='\t')
x_2d = pd.read_csv(path_out + 'nslkdd2d.csv', sep='\t')

#Step 3 :: Execute KMeans
k_means = cluster.KMeans(n_clusters = 2, n_init=100, random_state=0)

k_means.fit(x_7d)
y_7d = pd.DataFrame(data=k_means.labels_)

k_means.fit(x_3d)
y_3d = pd.DataFrame(data=k_means.labels_)

k_means.fit(x_2d)
y_2d = pd.DataFrame(data=k_means.labels_)

#Step 4 :: Export results
y_7d.to_csv(path_out+'kmeans7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out+'kmeans3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out+'kmeans2f.csv', sep='\t', index=False)
print('Data successfully exported!')