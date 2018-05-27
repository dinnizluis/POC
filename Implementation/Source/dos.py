import pandas as pd

path_in  = '../Input/'
path_out  = '../Output/'
dos_n = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'mailbomb', 'worm']

columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

train = pd.read_csv(path_in+'KDDTrain+.csv')
train.columns = columns

test = pd.read_csv(path_in+'KDDTest+.csv')
test.columns = columns

# Concatenate train and test into df
df = train.append(test, ignore_index=True)

ind = [] #Has the indeces of the DoS instances
for index, row in df.iterrows():
	if(df['label'][index] in dos_n):
		ind.append(index) 
print(len(ind)) #Quantity of DoS instances that should be found

data = []
#ind = pd.DataFrame(data = ind)
algorithm = ['kmeans', 'lof', 'isolationForest', 'ellipticEnvelope', 'hbos']
for i in range(0, len(algorithm)):
	df = pd.read_csv(path_out + algorithm[i] + '_complete.csv', sep = '\t')
	alg_ind = []
	for index, row in df.iterrows():
		if(df['0'][index] == 1):
			alg_ind.append(index)
	alg_ind = pd.DataFrame(data = alg_ind)
	tp = 0
	fp = 0
	for index, row in alg_ind.iterrows():
		if(alg_ind[0][index] in ind):
			tp = tp + 1
		else:
			fp = fp + 1
	print(algorithm[i])
	print('dos: ' + str(tp))
	print('other: ' + str(fp))

	data.append({'Expected ': len(ind), 'Actual DoS ': tp, 'Other attacks ': fp})

results = pd.DataFrame(data=data, index=algorithm)
print(results)
results.to_csv(path_out + 'dos.csv', sep='\t')
