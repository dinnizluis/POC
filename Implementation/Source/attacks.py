import pandas as pd
import numpy as np

columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_host_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"]

dos = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'worm', 'mailbomb']
u2r = ['buffer_overflow', 'loadmodule', 'rootkit', 'perl', 'sqlattack', 'xterm', 'ps']
r2l = ['guess_passwd', 'ftp_write', 'imap', 'phf', 'multihop', 'warezmaster', 'warezclient', 'spy', 'xlock', 'xsnoop', 'snmpguess', 'snmpgetattack', 'httptunnel', 'sendmail', 'named']
probe = ['satan', 'ipsweep', 'nmap', 'portsweep', 'mscan', 'saint'] 

train = pd.read_csv('../Input/KDDTrain+.csv')
train.columns = columns


normal_count_train = 0
dos_count_train = 0
probe_count_train = 0
u2r_count_train = 0
r2l_count_train = 0

attacks_train = train['label'].values

for i in range(0, len(attacks_train)):
	if attacks_train[i] != 'normal':
		if attacks_train[i] in dos:
			dos_count_train = dos_count_train+1
		elif attacks_train[i] in probe:
			probe_count_train = probe_count_train+1
		elif attacks_train[i] in u2r:
			u2r_count_train = u2r_count_train+1
		else:
			r2l_count_train = r2l_count_train+1
	else:
		normal_count_train = normal_count_train+1

test = pd.read_csv('../Input/KDDTest+.csv')
test.columns = columns


normal_count_test = 0
dos_count_test = 0
probe_count_test = 0
u2r_count_test = 0
r2l_count_test = 0

attacks_test = test['label'].values

for i in range(0, len(attacks_test)):
	if attacks_test[i] != 'normal':
		if attacks_test[i] in dos:
			dos_count_test = dos_count_test+1
		elif attacks_test[i] in probe:
			probe_count_test = probe_count_test+1
		elif attacks_test[i] in u2r:
			u2r_count_test = u2r_count_test+1
		else:
			r2l_count_test = r2l_count_test+1
	else:
		normal_count_test = normal_count_test+1

tot_train = dos_count_train+u2r_count_train+r2l_count_train+probe_count_train+normal_count_train
tot_test = dos_count_test+u2r_count_test+r2l_count_test+probe_count_test+normal_count_test

index = ['Dos', 'U2R', 'R2L', 'Probe', 'Normal', 'All']
data = [{'Train': dos_count_train, 'Test': dos_count_test, '_Total': dos_count_train+dos_count_test},
		{'Train': u2r_count_train, 'Test': u2r_count_test, '_Total': u2r_count_train+u2r_count_test},
		{'Train': r2l_count_train, 'Test': r2l_count_test, '_Total': r2l_count_train+r2l_count_test},
		{'Train': probe_count_train, 'Test': probe_count_test, '_Total': probe_count_train+probe_count_test},
		{'Train': normal_count_train, 'Test': normal_count_test, '_Total': normal_count_train+normal_count_test},
		{'Train': tot_train, 'Test': tot_test, '_Total': tot_test+tot_train}]

out = pd.DataFrame(data=data, index=index)

print(out)
out.to_csv('../Output/nslkdd_details.csv', sep='\t')