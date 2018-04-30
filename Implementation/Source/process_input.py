#Script_1 - Luis Diniz - 30/03/2018

#Goal: - Concatenate train and test dataset into one
#      - Remove not DoS attack instances
#	   - Select the 7 relevant features [see reference]
#	   - Normalize features selected
#	   - Export the resulting file into csv

#Step 1 :: Import libraries
import pandas as pd
from sklearn import preprocessing

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

#Step 4 :: Drop non-numeric features
df = df.drop(['Protocol_type', 'Service', 'Flag', 'Land', 'Logged_in', 'Root_shell', 'Su_attempted', 'Is_guest_login', 'Is_host_login'], axis=1)


#Step 5 :: Save indexes of not DoS attack instances
dos_n_normal = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'worm', 'normal']
ind = []
for index, row in df.iterrows():
	if(df['label'][index] not in dos_n_normal):
		ind.append(index) 

#Step 6 :: Save and export labels for precision calculation
labels_32 = (df['label'] != 'normal')*1 #Convert boolean to int

print('Labels 32: ' + str(labels_32.shape))
labels_32 = pd.DataFrame(data = labels_32)
labels_32.to_csv(path_in + 'labels_32.csv', sep='\t', index = False)
df = df.drop(['label', 'num'], axis=1)

print('DF 32: ' + str(df.shape))


#Step 7 :: Normalize features
df_7 = df
df = preprocessing.normalize(df)

#Step 8 :: Export 'complete dataset' (all attacks categories and numeric features)
df = pd.DataFrame(data = df)
df.to_csv(path_in + 'nslkdd_complete.csv', sep='\t', index = False)
print('Complete dataset successfully exported')

#Step 9 :: Remove not DoS attack instances
df_7.drop(df_7.index[ind], inplace = True)
labels_32.drop(labels_32.index[ind], inplace = True)
labels = pd.DataFrame(data = labels_32)

labels.to_csv(path_in +'labels.csv', sep='\t', index = False)

#Step 10 :: Select the relevant features
df_7 = df_7[['Duration', 'Scr_bytes', 'Count', 'Srv_rerror_rate', 'Dst_host_same_srv_rate', 'Dst_host_srv_serror_rate', 'Dst_host_srv_rerror_rate']]
df_7 = preprocessing.normalize(df_7)

#Step 11 :: Export df_7 to csv
df_7 = pd.DataFrame(data = df_7)

print('Labels 07: ' + str(labels.shape))
print('DF 07: ' + str(df_7.shape))

df_7.to_csv(path_in + 'nslkdd_7f.csv', sep='\t', index = False)
print('7 features dataset successfully exported')