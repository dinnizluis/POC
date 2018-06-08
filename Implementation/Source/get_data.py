from process_data import *
import pandas as pd 
from sklearn import preprocessing
import numpy as np

train = pd.read_csv('../Input/KDDTrain+.csv')
test  = pd.read_csv('../Input/KDDTest+.csv')

train = place_columns(train)
test = place_columns(test)

nslkdd = train.append(test, ignore_index=True)

non_numeric_features = ['Protocol_type', 'Service', 'Flag', 'Land', 'Logged_in', 'Root_shell', 'Su_attempted', 'Is_guest_login', 'Is_host_login']
nslkdd_complete = drop_features(nslkdd, non_numeric_features)

dos = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'worm', 'mailbomb']
u2r = ['buffer_overflow', 'loadmodule', 'rootkit', 'perl', 'sqlattack', 'xterm', 'ps']
r2l = ['guess_passwd', 'ftp_write', 'imap', 'phf', 'multihop', 'warezmaster', 'warezclient', 'spy', 'xlock', 'xsnoop', 'snmpguess', 'snmpgetattack', 'httptunnel', 'sendmail', 'named']
probe = ['satan', 'ipsweep', 'nmap', 'portsweep', 'mscan', 'saint'] 

nslkdd_32f_dos = drop_rows(nslkdd_complete, get_indexes(dos, nslkdd_complete))
nslkdd_32f_u2r = drop_rows(nslkdd_complete, get_indexes(u2r, nslkdd_complete))
nslkdd_32f_r2l = drop_rows(nslkdd_complete, get_indexes(r2l, nslkdd_complete))
nslkdd_32f_probe = drop_rows(nslkdd_complete, get_indexes(probe, nslkdd_complete))

labels_dos = get_binary_labels(nslkdd_32f_dos)
labels_u2r = get_binary_labels(nslkdd_32f_u2r)
labels_r2l = get_binary_labels(nslkdd_32f_r2l)
labels_probe = get_binary_labels(nslkdd_32f_probe)

labels_dos.columns = ["label"]
labels_u2r.columns = ["label"]
labels_r2l.columns = ["label"]
labels_probe.columns = ["label"]

#Get rid of the label and the difficulty level
nslkdd_32f_dos = drop_features(nslkdd_32f_dos, ['label', 'num'])
nslkdd_32f_u2r = drop_features(nslkdd_32f_u2r, ['label', 'num'])
nslkdd_32f_r2l = drop_features(nslkdd_32f_r2l, ['label', 'num'])
nslkdd_32f_probe = drop_features(nslkdd_32f_probe, ['label', 'num'])

#Lists of features referenced in the literature (will be used for feature selection)
dos_features = ['Duration', 'Scr_bytes', 'Count', 'Srv_rerror_rate', 'Dst_host_same_srv_rate', 'Dst_host_srv_serror_rate', 'Dst_host_srv_rerror_rate']
u2r_features = ['Num_file_creations', 'Num_shells']
r2l_features = ['Duration', 'Num_failed_logins']
probe_features = ['Duration', 'Scr_bytes']

#Feature selection
nslkdd_7f_dos = select_features(nslkdd_32f_dos, dos_features)
nslkdd_2f_u2r = select_features(nslkdd_32f_u2r, u2r_features)
nslkdd_2f_r2l = select_features(nslkdd_32f_r2l, r2l_features)
nslkdd_2f_probe = select_features(nslkdd_32f_probe, probe_features)

#PCA
nslkdd_2f_dos = run_pca(2, nslkdd_32f_dos)
nslkdd_7f_u2r = run_pca(7, nslkdd_32f_u2r)
nslkdd_7f_r2l = run_pca(7, nslkdd_32f_r2l)
nslkdd_7f_probe = run_pca(7, nslkdd_32f_probe)

nslkdd_3f_dos = run_pca(3, nslkdd_32f_dos)
nslkdd_3f_u2r = run_pca(3, nslkdd_32f_u2r)
nslkdd_3f_r2l = run_pca(3, nslkdd_32f_r2l)
nslkdd_3f_probe = run_pca(3, nslkdd_32f_probe)

#Normalize all data

nslkdd_32f_dos = preprocessing.normalize(nslkdd_32f_dos)
nslkdd_7f_dos = preprocessing.normalize(nslkdd_7f_dos)
nslkdd_3f_dos = preprocessing.normalize(nslkdd_3f_dos)
nslkdd_2f_dos = preprocessing.normalize(nslkdd_2f_dos)

nslkdd_32f_u2r = preprocessing.normalize(nslkdd_32f_u2r)
nslkdd_7f_u2r = preprocessing.normalize(nslkdd_7f_u2r)
nslkdd_3f_u2r = preprocessing.normalize(nslkdd_3f_u2r)
nslkdd_2f_u2r = preprocessing.normalize(nslkdd_2f_u2r)

nslkdd_32f_r2l = preprocessing.normalize(nslkdd_32f_r2l)
nslkdd_7f_r2l = preprocessing.normalize(nslkdd_7f_r2l)
nslkdd_3f_r2l = preprocessing.normalize(nslkdd_3f_r2l)
nslkdd_2f_r2l = preprocessing.normalize(nslkdd_2f_r2l)

nslkdd_32f_probe = preprocessing.normalize(nslkdd_32f_probe)
nslkdd_7f_probe = preprocessing.normalize(nslkdd_7f_probe)
nslkdd_3f_probe = preprocessing.normalize(nslkdd_3f_probe)
nslkdd_2f_probe = preprocessing.normalize(nslkdd_2f_probe)

#Get rid of NaN or infinty values (if there's any)

nslkdd_32f_u2r = np.nan_to_num(nslkdd_32f_u2r)
nslkdd_7f_u2r = np.nan_to_num(nslkdd_7f_u2r)
nslkdd_3f_u2r = np.nan_to_num(nslkdd_3f_u2r)
nslkdd_2f_u2r = np.nan_to_num(nslkdd_2f_u2r)

#Convert back to DF's 

nslkdd_32f_dos = pd.DataFrame(data=nslkdd_32f_dos)
nslkdd_7f_dos = pd.DataFrame(data=nslkdd_7f_dos)
nslkdd_3f_dos = pd.DataFrame(data=nslkdd_3f_dos)
nslkdd_2f_dos = pd.DataFrame(data=nslkdd_3f_dos)

nslkdd_32f_u2r = pd.DataFrame(data=nslkdd_32f_u2r)
nslkdd_7f_u2r = pd.DataFrame(data=nslkdd_7f_u2r)
nslkdd_3f_u2r = pd.DataFrame(data=nslkdd_3f_u2r)
nslkdd_2f_u2r = pd.DataFrame(data=nslkdd_2f_u2r)

nslkdd_32f_r2l = pd.DataFrame(data=nslkdd_32f_r2l)
nslkdd_7f_r2l = pd.DataFrame(data=nslkdd_7f_r2l)
nslkdd_3f_r2l = pd.DataFrame(data=nslkdd_3f_r2l)
nslkdd_2f_r2l = pd.DataFrame(data=nslkdd_2f_r2l)

nslkdd_32f_probe = pd.DataFrame(data=nslkdd_32f_probe)
nslkdd_7f_probe = pd.DataFrame(data=nslkdd_7f_probe)
nslkdd_3f_probe = pd.DataFrame(data=nslkdd_3f_probe)
nslkdd_2f_probe = pd.DataFrame(data=nslkdd_2f_probe)


#Export all DF's to csv files

labels_dos.to_csv('../Input/labels_dos.csv', sep='\t', index=False)
labels_u2r.to_csv('../Input/labels_u2r.csv', sep='\t', index=False)
labels_r2l.to_csv('../Input/labels_r2l.csv', sep='\t', index=False)
labels_probe.to_csv('../Input/labels_probe.csv', sep='\t', index=False)
print('Labels successfully exported!')

nslkdd_32f_dos.to_csv('../Input/nslkdd_32f_dos.csv', sep='\t', index=False)
nslkdd_7f_dos.to_csv('../Input/nslkdd_7f_dos.csv', sep='\t', index=False)
nslkdd_3f_dos.to_csv('../Input/nslkdd_3f_dos.csv', sep='\t', index=False)
nslkdd_2f_dos.to_csv('../Input/nslkdd_2f_dos.csv', sep='\t', index=False)
print('DoS files successfully exported!')

nslkdd_32f_u2r.to_csv('../Input/nslkdd_32f_u2r.csv', sep='\t', index=False)
nslkdd_7f_u2r.to_csv('../Input/nslkdd_7f_u2r.csv', sep='\t', index=False)
nslkdd_3f_u2r.to_csv('../Input/nslkdd_3f_u2r.csv', sep='\t', index=False)
nslkdd_2f_u2r.to_csv('../Input/nslkdd_2f_u2r.csv', sep='\t', index=False)
print('U2R files successfully exported!')

nslkdd_32f_r2l.to_csv('../Input/nslkdd_32f_r2l.csv', sep='\t', index=False)
nslkdd_7f_r2l.to_csv('../Input/nslkdd_7f_r2l.csv', sep='\t', index=False)
nslkdd_3f_r2l.to_csv('../Input/nslkdd_3f_r2l.csv', sep='\t', index=False)
nslkdd_2f_r2l.to_csv('../Input/nslkdd_2f_r2l.csv', sep='\t', index=False)
print('R2l files successfully exported!')

nslkdd_32f_probe.to_csv('../Input/nslkdd_32f_probe.csv', sep='\t', index=False)
nslkdd_7f_probe.to_csv('../Input/nslkdd_7f_probe.csv', sep='\t', index=False)
nslkdd_3f_probe.to_csv('../Input/nslkdd_3f_probe.csv', sep='\t', index=False)
nslkdd_2f_probe.to_csv('../Input/nslkdd_2f_probe.csv', sep='\t', index=False)
print('Probe files successfully exported!')