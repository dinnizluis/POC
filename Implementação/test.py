from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import pandas as pd 

sample = pd.read_csv('KDDTest+.csv')
#Selecionar colunas com as features escolhidas (coluna 0 e 4: Probing Attack)

# Create a KMeans instance with 6 clusters: model (4 types of attack and the regular data)
model = KMeans(n_clusters=5)

# Fit the data to the model
sample = sample.values #converting a df to a np array
model.fit(sample)

labels = model.predict(sample)
print(labels)

