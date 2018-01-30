#Importing libraries
import scipy.io
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import pickle

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from sklearn.covariance import EllipticEnvelope

#Loading the dataset
df = pd.read_csv("KDDTrain+_20Percent.csv") 
#Deleting labels and string features
df = df.drop(df.columns[[1, 2, 3, 41, 42]], axis=1)

#EllipticEnvelope
#Binary function
#outlier_frac = 1
#ell = EllipticEnvelope(contamination=outlier_frac)
#ell.fit(df)

#pred = ell.predict(df)
#print(sum(pred == -1))

#Continuous Function
decision = ell.decision_function(df)
#decision.min(), decision.max()