import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)

#load the data
df = pd.read_csv("KDDTrain+_20Percent.csv")

#sellect features
df = df.drop(df.columns[[1, 2, 3, 41, 42]], axis=1) #Indices of the non wanted columns [read features]


clf = IsolationForest(max_samples=10000, random_state=rng)#Study parameters
clf.fit(df)
y_pred_train = clf.predict(df)

xx, yy = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
xx_r = xx.ravel()
yy_r = yy.ravel()
#Z = clf.decision_function(np.c_[xx_r, yy_r])#Turns the matrix into a vector
#Z = Z.reshape(xx.shape)

#plt.title("IsolationForest")
#plt.contour(xx, yy, Z, cmap=plt.cm.Bluers_r)

d = plt.scatter(df[:, 0], df[:, 1], c = "red", s=20, edgecolor='k')

plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.show()