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

nslkdd_32f_u2r = drop_rows(nslkdd_complete, get_indexes(u2r, nslkdd_complete))
#nslkdd_32f_r2l = drop_rows(nslkdd_complete, get_indexes(r2l, nslkdd_complete))

nslkdd_32f_u2r = drop_features(nslkdd_32f_u2r, ['label', 'num'])
#nslkdd_32f_r2l = drop_features(nslkdd_32f_r2l, ['label', 'num'])

u2r_features = ['Num_file_creations', 'Num_shells']
#r2l_features = ['Duration', 'Num_failed_logins']

nslkdd_2f_u2r = select_features(nslkdd_32f_u2r, u2r_features)
#nslkdd_2f_r2l = select_features(nslkdd_32f_r2l, r2l_features)

nslkdd_7f_u2r = run_pca(7, nslkdd_32f_u2r)
#nslkdd_7f_r2l = run_pca(7, nslkdd_32f_r2l)

nslkdd_3f_u2r = run_pca(3, nslkdd_32f_u2r)
#nslkdd_3f_r2l = run_pca(3, nslkdd_32f_r2l)

nslkdd_32f_u2r = preprocessing.normalize(nslkdd_32f_u2r)
nslkdd_7f_u2r = preprocessing.normalize(nslkdd_7f_u2r)
nslkdd_3f_u2r = preprocessing.normalize(nslkdd_3f_u2r)
nslkdd_2f_u2r = preprocessing.normalize(nslkdd_2f_u2r)

nslkdd_32f_u2r = preprocessing.scale(nslkdd_32f_u2r)
nslkdd_7f_u2r = preprocessing.scale(nslkdd_7f_u2r)
nslkdd_3f_u2r = preprocessing.scale(nslkdd_3f_u2r)
nslkdd_2f_u2r = preprocessing.scale(nslkdd_2f_u2r)

#nslkdd_32f_r2l = preprocessing.normalize(nslkdd_32f_r2l)
#nslkdd_7f_r2l = preprocessing.normalize(nslkdd_7f_r2l)
#nslkdd_3f_r2l = preprocessing.normalize(nslkdd_3f_r2l)
#nslkdd_2f_r2l = preprocessing.normalize(nslkdd_2f_r2l)


nslkdd_32f_u2r = pd.DataFrame(data=nslkdd_32f_u2r)
nslkdd_7f_u2r = pd.DataFrame(data=nslkdd_7f_u2r)
nslkdd_3f_u2r = pd.DataFrame(data=nslkdd_3f_u2r)
nslkdd_2f_u2r = pd.DataFrame(data=nslkdd_2f_u2r)

#nslkdd_32f_r2l = pd.DataFrame(data=nslkdd_32f_r2l)
#nslkdd_7f_r2l = pd.DataFrame(data=nslkdd_7f_r2l)
#nslkdd_3f_r2l = pd.DataFrame(data=nslkdd_3f_r2l)
#nslkdd_2f_r2l = pd.DataFrame(data=nslkdd_2f_r2l)

nslkdd_32f_u2r.to_csv('../Input/nslkdd_32f_u2r.csv', sep='\t', index=False)
nslkdd_7f_u2r.to_csv('../Input/nslkdd_7f_u2r.csv', sep='\t', index=False)
nslkdd_3f_u2r.to_csv('../Input/nslkdd_3f_u2r.csv', sep='\t', index=False)
nslkdd_2f_u2r.to_csv('../Input/nslkdd_2f_u2r.csv', sep='\t', index=False)
print('U2R files successfully exported!')

#nslkdd_32f_r2l.to_csv('../Input/nslkdd_32f_r2l.csv', sep='\t', index=False)
#nslkdd_7f_r2l.to_csv('../Input/nslkdd_7f_r2l.csv', sep='\t', index=False)
#nslkdd_3f_r2l.to_csv('../Input/nslkdd_3f_r2l.csv', sep='\t', index=False)
#nslkdd_2f_r2l.to_csv('../Input/nslkdd_2f_r2l.csv', sep='\t', index=False)
#print('R2l files successfully exported!')