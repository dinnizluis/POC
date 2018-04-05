#Script 7 - Luis Diniz - 31/03/2018

#Goals: - Run KMeans with 2 features [PCA output]
#       - Export results to csv file

#Step 1 :: Import libraries
from sklearn import cluster
import pandas as pd 

#Step 2 :: Load data
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
df = pd.read_csv(path_out+'nslkdd2d.csv', sep='\t')

#Step 3 :: Execute KMeans
k_means = cluster.KMeans(n_clusters = 2)
k_means.fit(df)

#Step 4 :: Export results
res = pd.DataFrame(data = k_means.labels_)
res.to_csv(path_out+'kmeans2f.csv', sep='\t', index = False)
print('Data successfully exported!')