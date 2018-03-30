#Script_1 - Luis Diniz - 30/03/2018

#Goal: - Concatenate train and test dataset into one
#      - Remove not DoS attack instances
#	   - Select the 7 relevant features [see reference]
#	   - Normalize features selected
#	   - Export the resulting file into csv

#Step 1 :: Import the libraries to be used
import pandas as pd
from sklearn import preprocessing

#Step 2 :: Load the train and test sets
path_in  = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Input/'
train = pd.read_csv(path_in+'KDDTrain+.csv')
train.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

test = pd.read_csv(path_in+'KDDTest+.csv')
test.columns = ["Duration", "Protocol_type", "Service", "Flag", "Scr_bytes", "Dst_bytes", "Land", "Wrong_fragment", "Urgent",
			  "Hot", "Num_failed_logins", "Logged_in", "Num_compromised", "Root_shell", "Su_attempted", "Num_root", "Num_file_creations", "Num_shells", "Num_access_files", "Num_outbound_cmds", "Is_hot_login", "Is_guest_login",
			  "Count", "Srv_count", "Serror_rate", "Srv_serror_rate", "Rerror_rate", "Srv_rerror_rate", "Same_srv_state", "Diff_srv_rate", 'Srv_dff_host_rate',
			  "Dst_host_count", "Dst_host_srv_count", "Dst_host_same_srv_rate", "Dst_host_diff_srv_rate", "Dst_host_same_scr_port_rate", "Dst_host_srv_diff_host_rate", "Dst_host_serror_rate", "Dst_host_srv_serror_rate", "Dst_host_rerror_rate", "Dst_host_srv_rerror_rate", "label", "num"] 

#Step 3 :: Concatenate train and test into df
df = train.append(test, ignore_index=True)

#Step 4 :: Remove not DoS attack instances
dos_n_normal = ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 'processtable', 'worm', 'normal']
ind = []
for index, row in df.iterrows():
	if(df['label'][index] not in dos_n_normal):
		ind.append(index) 
df.drop(df.index[ind], inplace = True)

#Step 4.5 :: Save labels for precision calculation
labels = (df['label'] != 'normal')*1 #Convert boolean to int


#Step 5 :: Select the relevant features
df = df[['Duration', 'Scr_bytes', 'Count', 'Srv_rerror_rate', 'Dst_host_same_srv_rate', 'Dst_host_srv_serror_rate', 'Dst_host_srv_rerror_rate']]


#Step 6 :: Normalize features
df = preprocessing.normalize(df)

#Step 7 :: Export df to csv
df = pd.DataFrame(data = df)
labels = pd.DataFrame(data = labels)
path_out  = '/Users/dinnizluis/Dropbox/Computer Science/00_20132018_Atividades Extracurriculares/Iniciação Científica/Análise de Dados/POC/Implementation/Output/'
df.to_csv(path_out+'nslkdd.csv', sep='\t')
labels.to_csv(path_out+'labels.csv', sep='\t')
print('Results successfully exported')