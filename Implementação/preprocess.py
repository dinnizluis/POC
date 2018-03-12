#Script to clean the dataset and format it
import pandas as pd

#Loading the dataset
df = pd.read_csv("KDDTrain+_20Percent.csv")
df.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", "Srv_diff_host_rate",
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

#Dropping labels and string features
df = df.drop(['Protocol_type', 'Service', 'Flag', 'num'], axis=1)
n_rows, n_columns = df.shape

for i in range(0, n_rows):
	if(df['label'][i] == 'normal'):
		df.iloc[i, df.columns.get_loc('label')] = 0
	else:
		df.iloc[i, df.columns.get_loc('label')] = 1


#Exporting the new dataframe with labels
df.to_csv('KDDTrain+_20Percent_pcd.csv', sep='\t', index = False)

#Exporting the new dataframe with no labels
df = df.drop(['label'], axis=1)
df.to_csv('KDDTrain+_20Percent_pcd_no_label.csv', sep='\t', index = False)