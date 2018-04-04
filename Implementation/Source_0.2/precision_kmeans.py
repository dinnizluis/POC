# Script 9 - Luis Diniz - 31/03/2018

# Goals: - Calculte the precision rate of KMeans with 7 features input
#       - Calculte the precision rate of KMeans with 3 features input
#       - Calculte the precision rate of KMeans with 2 features input
#       - Export results to csv file

# Step 1 :: Import libraries
import pandas as pd
from sklearn.metrics import confusion_matrix
# Step 2 :: Load data
path_in = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
path_out = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
k2 = pd.read_csv(path_out + 'kmeans2f.csv', sep='\t')
k3 = pd.read_csv(path_out + 'kmeans3f.csv', sep='\t')
k7 = pd.read_csv(path_out + 'kmeans7f.csv', sep='\t')
y = pd.read_csv(path_in + 'labels.csv', sep='\t')

y_norm = y[y['label'] == False]
y_dos  = y[y['label'] == True]
k7_norm = k7[k7['0'] == False]
k7_dos  = k7[k7['0'] == True]

# Quantity of normal instances in the original dataset
y0 = y_norm.shape[0]
# Quantity of anomalies in the original dataset
y1 = y_dos.shape[0]

# Quantity of instances predicted as normal
k0 = k7_norm.shape[0]
# Quantity of predicted anomalies
k1 = k7_dos.shape[0]

#print('y1 = ' + str(y1) + ' y0 = ' + str(y0))
#print('k1 = ' + str(k1) + ' k0 = ' + str(k0))

print(confusion_matrix(y, k7))
#fix this line
print(pd.crosstab(y, k7, rownames=['real'], colnames=['predicted'], margins=True))

# there is a built-in precision and recall function, use them

#data = [{'[Label 1]': truePos, '[Label 0]': falsePos},
#		{'[Label 1]': trueNeg, '[Label 0]': falseNeg}]

#index = ['[Predicted 0]', '[Predicted 1]']
#confusion_matrix = pd.DataFrame(data, index=index)
#print(confusion_matrix)

# Definition of precision :: 

# Step 3 :: Do calculations
def calc_precision(x, y):
    if (x.shape[1] == y.shape[1]):
        correct = 0
        for index, row in x.iterrows():
            if (x['0'][index] == y['label'][index]):
                correct += 1

        return (correct / (x.shape[0])) * 100


#rate2f = calc_precision(k2, y)
#rate3f = calc_precision(k3, y)
#rate7f = calc_precision(k7, y)

# Step 4 :: Export results
#rates = [{'Rate for 2 features': rate2f, 'Rate for 3 features': rate3f, 'Rate for 7 features': rate7f}]
#res = pd.DataFrame(rates)
#res.to_csv(path_out + 'kmeans_results.csv', sep='\t', index=False)
#print('Data successfully exported!')
