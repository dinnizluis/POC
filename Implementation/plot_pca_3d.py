import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df  = pd.read_csv("KDD_DoS_pca3d.csv", sep='\t')


x1 = []
y1 = []
x2 = []
y2 = []
z1 = []
z2 = []

x1 = df[df['label'] == 1]
y1 = df[df['label'] == 1]
z1 = df[df['label'] == 1]
x2 = df[df['label'] == 0]
y2 = df[df['label'] == 0]
z2 = df[df['label'] == 0]

norm_x1 = x1.drop(x1.columns[[1, 2, 3]], axis=1)
norm_y1 = y1.drop(y1.columns[[0, 2, 3]], axis=1)
norm_z1 = z1.drop(z1.columns[[0, 1, 3]], axis=1)
norm_x2 = x2.drop(x2.columns[[1, 2, 3]], axis=1)
norm_y2 = y2.drop(y2.columns[[0, 2, 3]], axis=1)
norm_z2 = z2.drop(z2.columns[[0, 1, 3]], axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')