import pandas as pd 

df = pd.read_csv("KDD_DoS.csv", sep = '\t')

df['label'] = (df['label'] != 'normal')*1 # (*1 to convert boolean to int)
print(df['label'])