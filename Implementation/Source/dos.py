#Script to clean the dataset, format and export it (with and without labels)

# Luis Diniz  - 19/03/2018 [UFV]_v1

import pandas as pd
import numpy as np

feature1 = "Scr_bytes"
feature2 = "Dst_host_srv_rerror_rate" 

#Loading the datasets
df_test = pd.read_csv("KDDTest+.csv")
df_test.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

df_train = pd.read_csv("KDDTrain+.csv")
df_train.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
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

#Relevant features: source_bytes and percentage of packets with errors
df = df[[feature1, feature2, 'label']]

#Replacing string values for binary values
df['label'] = (df['label'] != 'normal')*1 # (*1 to convert boolean to int)

#Exporting the dfs with and without labels
df.to_csv('KDD_DoS_label.csv', sep = '\t', index = False)
df.drop(['label'], axis = 1)
df.to_csv('KDD_DoS.csv', sep = '\t', index = False)