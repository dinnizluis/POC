import pandas as pd
from techniques import *

contamination_dos = 0.4093
contamination_u2r = 0.0015
contamination_r2l = 0.0479
contamination_probe = 0.1545
max_features = [32, 7, 3, 2]


#DoS Execution
print('DoS -----------------------------------------------------')
dos_32 = pd.read_csv('../Input/nslkdd_32f_dos.csv', sep='\t')
dos_7 = pd.read_csv('../Input/nslkdd_7f_dos.csv', sep='\t')
dos_3 = pd.read_csv('../Input/nslkdd_3f_dos.csv', sep='\t')
dos_2 = pd.read_csv('../Input/nslkdd_2f_dos.csv', sep='\t')

dos_out_ee = []
dos_out_hbos = []
dos_out_if = []
dos_out_kmeans = []
dos_out_lof = []

dos_in = [dos_32, dos_7, dos_3, dos_2]

#for i in range(len(dos_in)):
#	dos_out_ee.append(run_ellipticEnvelope(dos_in[i], contamination=contamination_dos))
#	dos_out_hbos.append(run_hbos(dos_in[i]))
#	dos_out_if.append(run_isolationForest(dos_in[i], contamination=contamination_dos, max_features=max_features[i]))
#	dos_out_kmeans.append(run_kmeans(dos_in[i]))
#	dos_out_lof.append(run_lof(dos_in[i], contamination=contamination_dos))
#	print('Finished execution for '+str(max_features[i])+' features')

#for i in range(len(dos_in)):
#	print(dos_out_ee[i].shape)
#	print(dos_out_hbos[i].shape)
#	print(dos_out_if[i].shape)
#	print(dos_out_kmeans[i].shape)
#	print(dos_out_lof[i].shape)

#U2R Execution
print('U2R -----------------------------------------------------')
u2r_32 = pd.read_csv('../Input/nslkdd_32f_u2r.csv', sep='\t')
u2r_7 = pd.read_csv('../Input/nslkdd_7f_u2r.csv', sep='\t')
u2r_3 = pd.read_csv('../Input/nslkdd_3f_u2r.csv', sep='\t')
u2r_2 = pd.read_csv('../Input/nslkdd_2f_u2r.csv', sep='\t')

u2r_out_ee = []
u2r_out_hbos = []
u2r_out_if = []
u2r_out_kmeans = []
u2r_out_lof = []

u2r_in = [u2r_32, u2r_7, u2r_3, u2r_2]

for i in range(len(u2r_in)):
	wait = input("U2R Execution started! PRESS ENTER TO CONTINUE.")
	u2r_out_ee.append(run_ellipticEnvelope(u2r_in[i], contamination=contamination_u2r))
	wait = input("Elliptic Envelope finished PRESS ENTER TO CONTINUE.")
	u2r_out_hbos.append(run_hbos(u2r_in[i]))
	wait = input("HBOS finished PRESS ENTER TO CONTINUE.")
	u2r_out_if.append(run_isolationForest(u2r_in[i], contamination=contamination_u2r, max_features=max_features[i]))
	wait = input("Isolation Forest finished PRESS ENTER TO CONTINUE.")
	u2r_out_kmeans.append(run_kmeans(u2r_in[i]))
	wait = input("KMeans finished PRESS ENTER TO CONTINUE.")
	u2r_out_lof.append(run_lof(u2r_in[i], contamination=contamination_u2r))
	wait = input('Finished execution for '+str(max_features[i])+' features')

for i in range(len(u2r_in)):
	print(u2r_out_ee[i].shape)
	print(u2r_out_hbos[i].shape)
	print(u2r_out_if[i].shape)
	print(u2r_out_kmeans[i].shape)
	print(u2r_out_lof[i].shape)

#R2L Execution
print('R2L -----------------------------------------------------')
r2l_32 = pd.read_csv('../Input/nslkdd_32f_r2l.csv', sep='\t')
r2l_7 = pd.read_csv('../Input/nslkdd_7f_r2l.csv', sep='\t')
r2l_3 = pd.read_csv('../Input/nslkdd_3f_r2l.csv', sep='\t')
r2l_2 = pd.read_csv('../Input/nslkdd_2f_r2l.csv', sep='\t')

r2l_out_ee = []
r2l_out_hbos = []
r2l_out_if = []
r2l_out_kmeans = []
r2l_out_lof = []

r2l_in = [r2l_32, r2l_7, r2l_3, r2l_2]

for i in range(len(r2l_in)):
	r2l_out_ee.append(run_ellipticEnvelope(r2l_in[i], contamination=contamination_r2l))
	r2l_out_hbos.append(run_hbos(r2l_in[i]))
	r2l_out_if.append(run_isolationForest(r2l_in[i], contamination=contamination_r2l, max_features=max_features[i]))
	r2l_out_kmeans.append(run_kmeans(r2l_in[i]))
	r2l_out_lof.append(run_lof(r2l_in[i], contamination=contamination_r2l))
	print('Finished execution for '+str(max_features[i])+' features')

for i in range(len(r2l_in)):
	print(r2l_out_ee[i].shape)
	print(r2l_out_hbos[i].shape)
	print(r2l_out_if[i].shape)
	print(r2l_out_kmeans[i].shape)
	print(r2l_out_lof[i].shape)

#Probe Execution
print('Probe -----------------------------------------------------')
probe_32 = pd.read_csv('../Input/nslkdd_32f_probe.csv', sep='\t')
probe_7 = pd.read_csv('../Input/nslkdd_7f_probe.csv', sep='\t')
probe_3 = pd.read_csv('../Input/nslkdd_3f_probe.csv', sep='\t')
probe_2 = pd.read_csv('../Input/nslkdd_2f_probe.csv', sep='\t')

probe_out_ee = []
probe_out_hbos = []
probe_out_if = []
probe_out_kmeans = []
probe_out_lof = []

probe_in = [probe_32, probe_7, probe_3, probe_2]

for i in range(len(probe_in)):
	probe_out_ee.append(run_ellipticEnvelope(probe_in[i], contamination=contamination_probe))
	probe_out_hbos.append(run_hbos(probe_in[i]))
	probe_out_if.append(run_isolationForest(probe_in[i], contamination=contamination_probe, max_features=max_features[i]))
	probe_out_kmeans.append(run_kmeans(probe_in[i]))
	probe_out_lof.append(run_lof(probe_in[i], contamination=contamination_probe))
	print('Finished execution for '+str(max_features[i])+' features')

for i in range(len(probe_in)):
	print(probe_out_ee[i].shape)
	print(probe_out_hbos[i].shape)
	print(probe_out_if[i].shape)
	print(probe_out_kmeans[i].shape)
	print(probe_out_lof[i].shape)


#Export results
for i in range(len(dos_out_ee)):
	dos_out_ee[i].to_csv('../Output_dos/ee_dos_'+str(max_features[i])+'.csv', sep='\t', index=False)
	dos_out_hbos[i].to_csv('../Output_dos/hbos_dos_'+str(max_features[i])+'.csv', sep='\t', index=False)
	dos_out_if[i].to_csv('../Output_dos/if_dos_'+str(max_features[i])+'.csv', sep='\t', index=False)
	dos_out_kmeans[i].to_csv('../Output_dos/kmeans_dos_'+str(max_features[i])+'.csv', sep='\t', index=False)
	dos_out_lof[i].to_csv('../Output_dos/lof_dos_'+str(max_features[i])+'.csv', sep='\t', index=False)

	u2r_out_ee[i].to_csv('../Output_u2r/ee_u2r_'+str(max_features[i])+'.csv', sep='\t', index=False)
	u2r_out_hbos[i].to_csv('../Output_u2r/hbos_u2r_'+str(max_features[i])+'.csv', sep='\t', index=False)
	u2r_out_if[i].to_csv('../Output_u2r/if_u2r_'+str(max_features[i])+'.csv', sep='\t', index=False)
	u2r_out_kmeans[i].to_csv('../Output_u2r/kmeans_u2r_'+str(max_features[i])+'.csv', sep='\t', index=False)
	u2r_out_lof[i].to_csv('../Output_u2r/lof_u2r_'+str(max_features[i])+'.csv', sep='\t', index=False)

	r2l_out_ee[i].to_csv('../Output_r2l/ee_r2l_'+str(max_features[i])+'.csv', sep='\t', index=False)
	r2l_out_hbos[i].to_csv('../Output_r2l/hbos_r2l_'+str(max_features[i])+'.csv', sep='\t', index=False)
	r2l_out_if[i].to_csv('../Output_r2l/if_r2l_'+str(max_features[i])+'.csv', sep='\t', index=False)
	r2l_out_kmeans[i].to_csv('../Output_r2l/kmeans_r2l_'+str(max_features[i])+'.csv', sep='\t', index=False)
	r2l_out_lof[i].to_csv('../Output_r2l/lof_r2l_'+str(max_features[i])+'.csv', sep='\t', index=False)

	probe_out_ee[i].to_csv('../Output_probe/ee_probe_'+str(max_features[i])+'.csv', sep='\t', index=False)
	probe_out_hbos[i].to_csv('../Output_probe/hbos_probe_'+str(max_features[i])+'.csv', sep='\t', index=False)
	probe_out_if[i].to_csv('../Output_probe/if_probe_'+str(max_features[i])+'.csv', sep='\t', index=False)
	probe_out_kmeans[i].to_csv('../Output_probe/kmeans_probe_'+str(max_features[i])+'.csv', sep='\t', index=False)
	probe_out_lof[i].to_csv('../Output_probe/lof_probe_'+str(max_features[i])+'.csv', sep='\t', index=False)
