#Script with the functions to help the processing of the data

import pandas as pd
from sklearn.decomposition import PCA

def run_pca(n_arguments, df2):
	df = df2.copy()
	#Fit the data
	pca = PCA(n_components=n_arguments)
	df = df.values
	pca.fit(df)

	#Reduce dimensions
	df_nd = pca.transform(df)

	#Convert back to df
	df_nd = pd.DataFrame(data=df_nd)

	#Return n dimensional dataframe
	return df_nd

def place_columns(df):
	columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_host_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"]
	df.columns = columns
	return df

def get_indexes(attacks, df):
	attacks.append('normal')
	ind = []
	for index, row in df.iterrows():
		if(df['label'][index] not in attacks):
			ind.append(index)

	return ind 

def drop_rows(df, ind):
	df2  = df.copy()
	df2.drop(df2.index[ind], inplace=True) 
	return df2

def get_labels(df):
	df2 = df.copy()
	return df2['label']

def get_binary_labels(df):
	#df2 = df.copy
	df2 = (df['label'] != 'normal')*1
	ans = pd.DataFrame(data=df2)
	return ans

def drop_features(df, features):
	df2 = df.copy()
	return df2.drop(features, axis=1)

def select_features(df, features):
	df2 = df.copy()
	return df2[features]