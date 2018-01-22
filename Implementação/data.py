import pandas as pd 

df = pd.read_csv("KDDTest+.csv")
df1 = pd.DataFrame(df['Destination']['Src_bytes'], columns = ['Destination', 'Src_bytes'])

#df1 = df[['Destination']['Src_bytes']]