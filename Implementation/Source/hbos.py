#Step 1 :: Import libraries
from hbos_def import *
import pandas as pd 
from sklearn import preprocessing

# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x_7d = pd.read_csv(path_in + 'nslkdd.csv', sep='\t')
x_3d = pd.read_csv(path_out + 'nslkdd3d.csv', sep='\t')
x_2d = pd.read_csv(path_out + 'nslkdd2d.csv', sep='\t')

hbos = HBOS()

y_7d = hbos.fit_predict(x_7d)
y_7d = pd.DataFrame(data=y_7d)
y_7d = preprocessing.normalize(y_7d)
y_7d = pd.DataFrame(data=y_7d)

y_3d = hbos.fit_predict(x_3d)
y_3d = pd.DataFrame(data=y_3d)
y_3d = preprocessing.normalize(y_3d)
y_3d = pd.DataFrame(data=y_3d)

y_2d = hbos.fit_predict(x_2d)
y_2d = pd.DataFrame(data=y_2d)
y_2d = preprocessing.normalize(y_2d)
y_2d = pd.DataFrame(data=y_2d)

# Step 4 :: Export results
y_7d.to_csv(path_out + 'hbos7f.csv', sep='\t', index=False)
y_3d.to_csv(path_out + 'hbos3f.csv', sep='\t', index=False)
y_2d.to_csv(path_out + 'hbos2f.csv', sep='\t', index=False)
print('Data successfully exported!')