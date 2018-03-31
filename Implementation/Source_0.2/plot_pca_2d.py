#Script 4 - Luis Diniz - 31/03/2018

#Goals: - Plot the result from principal component analysis 

#Step 1 :: Import the libraries
import matplotlib.pyplot as plt
import pandas as pd 

#Step 2 :: Load the data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
x = pd.read_csv(path_out+'nslkdd2d.csv', sep='\t')
label = pd.read_csv(path_in+'labels.csv', sep='\t')
x['label'] = label


#Step 3 :: Separate the regular and the attack instances
x_norm = x[x['label'] == 0]
y_norm = x_norm
x_dos = x[x['label'] == 1]
y_dos = x_dos

x_norm = x_norm.drop(['1', 'label'], axis=1)
y_norm = y_norm.drop(['0', 'label'], axis=1)
x_dos = x_dos.drop(['1', 'label'], axis=1)
y_dos = y_dos.drop(['0', 'label'], axis=1)



#Step 4 :: Plot figure
def graphpca2d():
	plt.figure()
	plt.plot(x_norm, y_norm, 'bo')
	plt.plot(x_dos, y_dos, 'r+')
	#plt.xscale('log')
	#plt.yscale('log')
	plt.xlabel('Feature 1')
	plt.ylabel('Feature 2')
	plt.title('PCA [7 to 2]')
	plt.show()

graphpca2d()