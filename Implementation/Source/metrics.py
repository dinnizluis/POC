from sklearn.metrics import *
import pandas as pd 


def get_auc(attack):
	index = ['32 Features', '7 Features', '3 Features', '2 Features']
	columns = ['EE', 'HBOS', 'IF', 'KMeans', 'LOF']
	if attack == 1: #DoS attack
		label_dos = pd.read_csv('../Input/labels_dos.csv', sep='\t')
		
		dos_ee = pd.read_csv('../Output/dos_ee.csv', sep='\t')
		auc_dos_ee = []
		auc_dos_ee.append(roc_auc_score(label_dos['label'], dos_ee['32']))
		auc_dos_ee.append(roc_auc_score(label_dos['label'], dos_ee['7']))
		auc_dos_ee.append(roc_auc_score(label_dos['label'], dos_ee['3']))
		auc_dos_ee.append(roc_auc_score(label_dos['label'], dos_ee['2']))
		ans = pd.DataFrame(data=auc_dos_ee, index=index)

		dos_hbos = pd.read_csv('../Output/dos_hbos.csv', sep='\t')
		auc_dos_hbos = []
		auc_dos_hbos.append(roc_auc_score(label_dos['label'], dos_hbos['32']))
		auc_dos_hbos.append(roc_auc_score(label_dos['label'], dos_hbos['7']))
		auc_dos_hbos.append(roc_auc_score(label_dos['label'], dos_hbos['3']))
		auc_dos_hbos.append(roc_auc_score(label_dos['label'], dos_hbos['2']))
		ans[1] = auc_dos_hbos

		dos_if = pd.read_csv('../Output/dos_if.csv', sep='\t')
		auc_dos_if = []
		auc_dos_if.append(roc_auc_score(label_dos['label'], dos_if['32']))
		auc_dos_if.append(roc_auc_score(label_dos['label'], dos_if['7']))
		auc_dos_if.append(roc_auc_score(label_dos['label'], dos_if['3']))
		auc_dos_if.append(roc_auc_score(label_dos['label'], dos_if['2']))
		ans[2] = auc_dos_if

		dos_k = pd.read_csv('../Output/dos_kmeans.csv', sep='\t')
		auc_dos_kmeans = []
		auc_dos_kmeans.append(roc_auc_score(label_dos['label'], dos_k['32']))
		auc_dos_kmeans.append(roc_auc_score(label_dos['label'], dos_k['7']))
		auc_dos_kmeans.append(roc_auc_score(label_dos['label'], dos_k['3']))
		auc_dos_kmeans.append(roc_auc_score(label_dos['label'], dos_k['2']))
		ans[3] = auc_dos_kmeans

		dos_lof = pd.read_csv('../Output/dos_lof.csv', sep='\t')
		auc_dos_lof = []
		auc_dos_lof.append(roc_auc_score(label_dos['label'], dos_lof['32']))
		auc_dos_lof.append(roc_auc_score(label_dos['label'], dos_lof['7']))
		auc_dos_lof.append(roc_auc_score(label_dos['label'], dos_lof['3']))
		auc_dos_lof.append(roc_auc_score(label_dos['label'], dos_lof['2']))
		ans[4] = auc_dos_lof

		ans.columns = columns
		return ans
	elif attack == 2: #u2r attack
		label_u2r = pd.read_csv('../Input/labels_u2r.csv', sep='\t')

		u2r_ee = pd.read_csv('../Output/u2r_ee.csv', sep='\t')
		auc_u2r_ee = []
		auc_u2r_ee.append(roc_auc_score(label_u2r['label'], u2r_ee['32']))
		auc_u2r_ee.append(roc_auc_score(label_u2r['label'], u2r_ee['7']))
		auc_u2r_ee.append(roc_auc_score(label_u2r['label'], u2r_ee['3']))
		auc_u2r_ee.append(roc_auc_score(label_u2r['label'], u2r_ee['2']))
		ans = pd.DataFrame(data=auc_u2r_ee, index=index)

		u2r_hbos = pd.read_csv('../Output/u2r_hbos.csv', sep='\t')
		auc_u2r_hbos = []
		auc_u2r_hbos.append(roc_auc_score(label_u2r['label'], u2r_hbos['32']))
		auc_u2r_hbos.append(roc_auc_score(label_u2r['label'], u2r_hbos['7']))
		auc_u2r_hbos.append(roc_auc_score(label_u2r['label'], u2r_hbos['3']))
		auc_u2r_hbos.append(roc_auc_score(label_u2r['label'], u2r_hbos['2']))
		ans[1] = auc_u2r_hbos

		u2r_if = pd.read_csv('../Output/u2r_if.csv', sep='\t')
		auc_u2r_if = []
		auc_u2r_if.append(roc_auc_score(label_u2r['label'], u2r_if['32']))
		auc_u2r_if.append(roc_auc_score(label_u2r['label'], u2r_if['7']))
		auc_u2r_if.append(roc_auc_score(label_u2r['label'], u2r_if['3']))
		auc_u2r_if.append(roc_auc_score(label_u2r['label'], u2r_if['2']))
		ans[2] = auc_u2r_if

		u2r_k = pd.read_csv('../Output/u2r_kmeans.csv', sep='\t')
		auc_u2r_kmeans = []
		auc_u2r_kmeans.append(roc_auc_score(label_u2r['label'], u2r_k['32']))
		auc_u2r_kmeans.append(roc_auc_score(label_u2r['label'], u2r_k['7']))
		auc_u2r_kmeans.append(roc_auc_score(label_u2r['label'], u2r_k['3']))
		auc_u2r_kmeans.append(roc_auc_score(label_u2r['label'], u2r_k['2']))
		ans[3] = auc_u2r_kmeans

		u2r_lof = pd.read_csv('../Output/u2r_lof.csv', sep='\t')
		auc_u2r_lof = []
		auc_u2r_lof.append(roc_auc_score(label_u2r['label'], u2r_lof['32']))
		auc_u2r_lof.append(roc_auc_score(label_u2r['label'], u2r_lof['7']))
		auc_u2r_lof.append(roc_auc_score(label_u2r['label'], u2r_lof['3']))
		auc_u2r_lof.append(roc_auc_score(label_u2r['label'], u2r_lof['2']))
		ans[4] = auc_u2r_lof

		ans.columns = columns
		return ans		
	elif attack == 3: #r2l attack
		label_r2l = pd.read_csv('../Input/labels_r2l.csv', sep='\t')

		r2l_ee = pd.read_csv('../Output/r2l_ee.csv', sep='\t')
		auc_r2l_ee = []
		auc_r2l_ee.append(roc_auc_score(label_r2l['label'], r2l_ee['32']))
		auc_r2l_ee.append(roc_auc_score(label_r2l['label'], r2l_ee['7']))
		auc_r2l_ee.append(roc_auc_score(label_r2l['label'], r2l_ee['3']))
		auc_r2l_ee.append(roc_auc_score(label_r2l['label'], r2l_ee['2']))
		ans = pd.DataFrame(data=auc_r2l_ee, index=index)

		r2l_hbos = pd.read_csv('../Output/r2l_hbos.csv', sep='\t')
		auc_r2l_hbos = []
		auc_r2l_hbos.append(roc_auc_score(label_r2l['label'], r2l_hbos['32']))
		auc_r2l_hbos.append(roc_auc_score(label_r2l['label'], r2l_hbos['7']))
		auc_r2l_hbos.append(roc_auc_score(label_r2l['label'], r2l_hbos['3']))
		auc_r2l_hbos.append(roc_auc_score(label_r2l['label'], r2l_hbos['2']))
		ans[1] = auc_r2l_hbos

		r2l_if = pd.read_csv('../Output/r2l_if.csv', sep='\t')
		auc_r2l_if = []
		auc_r2l_if.append(roc_auc_score(label_r2l['label'], r2l_if['32']))
		auc_r2l_if.append(roc_auc_score(label_r2l['label'], r2l_if['7']))
		auc_r2l_if.append(roc_auc_score(label_r2l['label'], r2l_if['3']))
		auc_r2l_if.append(roc_auc_score(label_r2l['label'], r2l_if['2']))
		ans[2] = auc_r2l_if

		r2l_k = pd.read_csv('../Output/r2l_kmeans.csv', sep='\t')
		auc_r2l_kmeans = []
		auc_r2l_kmeans.append(roc_auc_score(label_r2l['label'], r2l_k['32']))
		auc_r2l_kmeans.append(roc_auc_score(label_r2l['label'], r2l_k['7']))
		auc_r2l_kmeans.append(roc_auc_score(label_r2l['label'], r2l_k['3']))
		auc_r2l_kmeans.append(roc_auc_score(label_r2l['label'], r2l_k['2']))
		ans[3] = auc_r2l_kmeans

		r2l_lof = pd.read_csv('../Output/r2l_lof.csv', sep='\t')
		auc_r2l_lof = []
		auc_r2l_lof.append(roc_auc_score(label_r2l['label'], r2l_lof['32']))
		auc_r2l_lof.append(roc_auc_score(label_r2l['label'], r2l_lof['7']))
		auc_r2l_lof.append(roc_auc_score(label_r2l['label'], r2l_lof['3']))
		auc_r2l_lof.append(roc_auc_score(label_r2l['label'], r2l_lof['2']))
		ans[4] = auc_r2l_lof

		ans.columns = columns
		return ans	

	elif attack == 4: #probe attack
		label_probe = pd.read_csv('../Input/labels_probe.csv', sep='\t')

		probe_ee = pd.read_csv('../Output/probe_ee.csv', sep='\t')
		auc_probe_ee = []
		auc_probe_ee.append(roc_auc_score(label_probe['label'], probe_ee['32']))
		auc_probe_ee.append(roc_auc_score(label_probe['label'], probe_ee['7']))
		auc_probe_ee.append(roc_auc_score(label_probe['label'], probe_ee['3']))
		auc_probe_ee.append(roc_auc_score(label_probe['label'], probe_ee['2']))
		ans = pd.DataFrame(data=auc_probe_ee, index=index)

		probe_hbos = pd.read_csv('../Output/probe_hbos.csv', sep='\t')
		auc_probe_hbos = []
		auc_probe_hbos.append(roc_auc_score(label_probe['label'], probe_hbos['32']))
		auc_probe_hbos.append(roc_auc_score(label_probe['label'], probe_hbos['7']))
		auc_probe_hbos.append(roc_auc_score(label_probe['label'], probe_hbos['3']))
		auc_probe_hbos.append(roc_auc_score(label_probe['label'], probe_hbos['2']))
		ans[1] = auc_probe_hbos

		probe_if = pd.read_csv('../Output/probe_if.csv', sep='\t')
		auc_probe_if = []
		auc_probe_if.append(roc_auc_score(label_probe['label'], probe_if['32']))
		auc_probe_if.append(roc_auc_score(label_probe['label'], probe_if['7']))
		auc_probe_if.append(roc_auc_score(label_probe['label'], probe_if['3']))
		auc_probe_if.append(roc_auc_score(label_probe['label'], probe_if['2']))
		ans[2] = auc_probe_if

		probe_k = pd.read_csv('../Output/probe_kmeans.csv', sep='\t')
		auc_probe_kmeans = []
		auc_probe_kmeans.append(roc_auc_score(label_probe['label'], probe_k['32']))
		auc_probe_kmeans.append(roc_auc_score(label_probe['label'], probe_k['7']))
		auc_probe_kmeans.append(roc_auc_score(label_probe['label'], probe_k['3']))
		auc_probe_kmeans.append(roc_auc_score(label_probe['label'], probe_k['2']))
		ans[3] = auc_probe_kmeans

		probe_lof = pd.read_csv('../Output/probe_lof.csv', sep='\t')
		auc_probe_lof = []
		auc_probe_lof.append(roc_auc_score(label_probe['label'], probe_lof['32']))
		auc_probe_lof.append(roc_auc_score(label_probe['label'], probe_lof['7']))
		auc_probe_lof.append(roc_auc_score(label_probe['label'], probe_lof['3']))
		auc_probe_lof.append(roc_auc_score(label_probe['label'], probe_lof['2']))
		ans[4] = auc_probe_lof

		ans.columns = columns
		return ans	

dos_rs = get_auc(1)
u2r_rs = get_auc(2)
r2l_rs = get_auc(3)
probe_rs = get_auc(4)

print(dos_rs)
print(u2r_rs)
print(r2l_rs)
print(probe_rs)

dos_rs.to_csv('../Output/dos_results.csv', sep='\t')
u2r_rs.to_csv('../Output/u2r_results.csv', sep='\t')
r2l_rs.to_csv('../Output/r2l_results.csv', sep='\t')
probe_rs.to_csv('../Output/probe_results.csv', sep='\t')
print('Results successfully exported!')