#Step 1 :: Import libraries
import pandas as pd
import numpy as np 

#Step 2 :: Load the train and test sets
path_in  = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_host_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 
train = pd.read_csv(path_in+'KDDTrain+.csv')
train.columns = columns

test = pd.read_csv(path_in+'KDDTest+.csv')
test.columns = columns

#Step 3 :: Concatenate train and test into df
df = train.append(test, ignore_index=True)

normal = ['normal']
dos = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'worm', 'mailbomb']
u2r = ['buffer_overflow', 'loadmodule', 'rootkit', 'perl', 'sqlattack', 'xterm', 'ps']
r2l = ['guess_passwd', 'ftp_write', 'imap', 'phf', 'multihop', 'warezmaster', 'warezclient', 'spy', 'xlock', 'xsnoop', 'snmpguess', 'snmpgetattack', 'httptunnel', 'sendmail', 'named']
probe = ['satan', 'ipsweep', 'nmap', 'portsweep', 'mscan', 'saint'] 

attacks = df.label.unique()

for i in range(len(attacks)):
	if(attacks[i] not in normal and attacks[i] not in dos and attacks[i] not in u2r and attacks[i] not in r2l and attacks[i] not in probe):
		print(attacks[i] + ' attack NOT listed!')
	#else:
	#	print(attacks[i] + ' attack listed!')

np.asarray(attacks)
np.savetxt('attacks_list.txt', attacks)