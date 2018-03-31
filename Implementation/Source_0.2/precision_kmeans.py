#Script 9 - Luis Diniz - 31/03/2018

#Goals: - Calculte the precision rate of KMeans with 7 features input
#       - Calculte the precision rate of KMeans with 3 features input
#       - Calculte the precision rate of KMeans with 2 features input
#       - Export results to csv file

#Step 1 :: Import libraries
import pandas as pd 

#Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
k2 = pd.read_csv(path_out+'kmeans2f.csv', sep='\t')
k3 = pd.read_csv(path_out+'kmeans3f.csv', sep='\t')
k7 = pd.read_csv(path_out+'kmeans7f.csv', sep='\t')
y = pd.read_csv(path_in+'labels.csv', sep='\t')

#Step 3 :: Do calculations
def calc_precision(x, y):
	if(x.shape[1] == y.shape[1]):
		correct = 0
		for index, row in x.iterrows():
			if(x['0'][index] == y['label'][index]):
				correct += 1

		return (correct/(x.shape[0]))*100

rate2f = calc_precision(k2, y)
rate3f = calc_precision(k3, y)
rate7f = calc_precision(k7, y)

#Step 4 :: Export results
rates = [{'Rate for 2 features': rate2f, 'Rate for 3 features': rate3f, 'Rate for 7 features': rate7f}]
res = pd.DataFrame(rates)
res.to_csv(path_out+'kmeans_results.csv', sep='\t', index = False)
print('Data successfully exported!')