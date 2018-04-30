#Feature Selection  - Removing features with low variance

from sklearn.feature_selection import VarianceThreshold
import pandas as pd 

path_in  = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
X = pd.read_csv(path_in+'nslkdd_complete.csv', sep='\t')
print(X.shape)
selected = VarianceThreshold(threshold =(.8*(1-.8)) )
selected.fit_transform(X)
print(X.shape)