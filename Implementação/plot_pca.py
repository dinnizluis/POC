#Script to plot the orginal data

# Luis Diniz  - 19/03/2018 [UFV]_v1

from pylab import *
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import preprocessing

df = pd.read_csv("KDD_DoS_pca.csv", sep = '\t')

x1 = []
y1 = []
x2 = []
y2 = []


feature1 = "Scr_bytes"
feature2 = "Dst_host_srv_rerror_rate" 
x1 = df[df['label'] == 1]
y1 = df[df['label'] == 1]
x2 = df[df['label'] == 0]
y2 = df[df['label'] == 0]

norm_x1 = x1.drop(df.columns[[1, 2]], axis=1)
#norm_x1 = preprocessing.normalize(norm_x1)
norm_y1 = y1.drop(df.columns[[0, 2]], axis = 1)
#norm_y1 = preprocessing.normalize(norm_y1)
norm_x2 = x2.drop(df.columns[[1, 2]], axis = 1)
#norm_x2 = preprocessing.normalize(norm_x2)
norm_y2 = y2.drop(df.columns[[0, 2]], axis = 1)
#norm_y2 = preprocessing.normalize(norm_y2)

figure()
plot(norm_x1, norm_y1, 'bo')
plot(norm_x2, norm_y2, 'r+')
yscale('log')
xscale('log')
xlabel('X')
ylabel('Y')
title('Original data after principal component analysis')
show()