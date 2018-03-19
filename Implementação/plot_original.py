#Script to plot the orginal data

# Luis Diniz  - 19/03/2018 [UFV]_v1

from pylab import *
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("KDDTest+_probe.csv", sep = '\t')
#print(df['Duration'])
#print(df.columns)
x1 = []
y1 = []
x2 = []
y2 = []

for index, row in df.iterrows():
	if(df['label'][index] == 1):
		x1.append(df['Duration'][index])
		y1.append(df['Scr_bytes'][index])
	else:
		x2.append(df['Duration'][index])
		y2.append(df['Scr_bytes'][index])

figure()
plot(x1, y1, 'bo')
plot(x2, y2, 'r+')
xlabel('Duration')
ylabel('Source Bytes')
title('Original data')
show()