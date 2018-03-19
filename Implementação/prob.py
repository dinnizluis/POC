#Script to clean the dataset, format and export it (with and without labels)
import pandas as pd

#Loading the dataset
df = pd.read_csv("KDDTest+.csv")
df.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", "Srv_diff_host_rate",
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

df_prob = df[['Duration', 'Scr_bytes', 'label']]		  
#print(df_prob)

#List of probing attacks
probe = ['satan', 'ipsweep', 'nmap', 'portsweep', 'mscan', 'saint', 'normal']

ind = []
#Saving the indices of the rows to be deleted
for i in range(0, df_prob.shape[0]):
	if(df_prob['label'][i] not in probe):
		ind.append(i)

#Deleting unwanted rows
df_prob.drop(df_prob.index[ind], inplace = True)
print("----------REGRISTROS APAGADOS----------")

#Replace the string values for binaries
for index, row in df_prob.iterrows():
	print(". ")
	if(df_prob['label'][index] == 'normal'):
		df_prob['label'][index] = 0
	else:
		df_prob['label'][index] = 1
print("----------STRING SUBSTITUÍDAS--------------")
print(df_prob)

#Exporting to csv file df with labels
df_prob.to_csv('KDDTest+_probe.csv', sep = '\t', index = False)

#Exporting to csv file df without labels
df_prob = df_prob.drop(['label'], axis=1)
df_prob.to_csv('KDDTest+_probe_no_label.csv', '\t', index = False)