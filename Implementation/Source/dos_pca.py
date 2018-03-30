#Script to clean the dataset, format and export it (with and without labels)

# Luis Diniz  - 19/03/2018 [UFV]_v1

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

#Loading the datasets
df_test = pd.read_csv("KDDTest+.csv")
df_test.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_host_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", "Srv_diff_host_rate",
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

df_train = pd.read_csv("KDDTrain+.csv")
df_train.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_host_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", "Srv_diff_host_rate",
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

#The training and the test dataset are now 1 df
df = df_test.append(df_train, ignore_index = True)

attacks = df['label']

#List of instance's labels to be kept
dos = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'worm', 'normal']

#Getting the list of anomalous instances and not of DoS class
ind = []
for index, row in df.iterrows():
	if(df['label'][index] not in dos):
		ind.append(index) 

#Dropping anomalous instaces and not of DoS class
df.drop(df.index[ind], inplace = True)

df = df.reset_index(drop=True)


#Dropping binary features
df = df.drop(['Land', 'Logged_in', 'Root_shell', 'Su_attempted', 'Is_host_login', 'Is_guest_login'], axis = 1)
#Dropping nominal features
df = df.drop(['Protocol_type', 'Service', 'Flag'], axis = 1)

#Replacing string values for binary values
labels = (df['label'] != 'normal')*1 # (*1 to convert boolean to int)

#Exporting the dfs with and without labels
df = df.drop(['label', 'num'], axis = 1)


#Run PCA
pca = PCA(n_components = 2)
df_ = df.values
pca.fit(df_)
df_ = pca.transform(df_)
df = pd.DataFrame(data = df_)

#Exporto to csv file data without labels
df.to_csv('KDD_DoS_pca.csv', sep = '\t', index = False)

#Add the labels to the data and export to a csv file
df['label'] = labels
print(df)
df.to_csv('KDD_DoS_pca_label.csv', sep = '\t', index = False)
