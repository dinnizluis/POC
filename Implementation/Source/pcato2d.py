#Script 2 - Luis Diniz - 31/03/2018

#Goals: - Reduce the 7 dimensions to 2
#       - Export the result to a csv file

#Step 1 :: Import libraries
import pandas as pd 
import numpy as np 
from sklearn.decomposition import PCA

#Step 2 :: Load the input data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
df_7_d = pd.read_csv(path_in+'nslkdd.csv', sep='\t')

#Step 3 :: Fit the data
pca = PCA(n_components = 2)
df_7_d = df_7_d.values
pca.fit(df_7_d)

#Step 4:: Reduce dimensions
df_2_d = pca.transform(df_7_d)

#Step 4.5 :: Convert to df
df_2_d = pd.DataFrame(data = df_2_d)
print(df_2_d)

#Step 5 :: Export to csv
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
df_2_d.to_csv(path_out+'nslkdd2d.csv', sep='\t', index = False)
print('Data successfully exported!')