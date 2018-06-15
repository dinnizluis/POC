import pandas as pd
from techniques import *

contamination_dos = 0.4093
contamination_u2r = 0.0015
contamination_r2l = 0.0479
contamination_probe = 0.1545
max_features = [32, 7, 3, 2]

#Load all data ---------------------------------------------------------------------------------------------------------

#DoS data
dos_32 = pd.read_csv('../Input/nslkdd_32f_dos.csv', sep='\t')
dos_7 = pd.read_csv('../Input/nslkdd_7f_dos.csv', sep='\t')
dos_3 = pd.read_csv('../Input/nslkdd_3f_dos.csv', sep='\t')
dos_2 = pd.read_csv('../Input/nslkdd_2f_dos.csv', sep='\t')
dos_in = [dos_32, dos_7, dos_3, dos_2]

#U2R data
u2r_32 = pd.read_csv('../Input/nslkdd_32f_u2r.csv', sep='\t')
u2r_7 = pd.read_csv('../Input/nslkdd_7f_u2r.csv', sep='\t')
u2r_3 = pd.read_csv('../Input/nslkdd_3f_u2r.csv', sep='\t')
u2r_2 = pd.read_csv('../Input/nslkdd_2f_u2r.csv', sep='\t')
u2r_in = [u2r_32, u2r_7, u2r_3, u2r_2]

#R2L data
r2l_32 = pd.read_csv('../Input/nslkdd_32f_r2l.csv', sep='\t')
r2l_7 = pd.read_csv('../Input/nslkdd_7f_r2l.csv', sep='\t')
r2l_3 = pd.read_csv('../Input/nslkdd_3f_r2l.csv', sep='\t')
r2l_2 = pd.read_csv('../Input/nslkdd_2f_r2l.csv', sep='\t')
r2l_in = [r2l_32, r2l_7, r2l_3, r2l_2]

#Probe data
probe_32 = pd.read_csv('../Input/nslkdd_32f_probe.csv', sep='\t')
probe_7 = pd.read_csv('../Input/nslkdd_7f_probe.csv', sep='\t')
probe_3 = pd.read_csv('../Input/nslkdd_3f_probe.csv', sep='\t')
probe_2 = pd.read_csv('../Input/nslkdd_2f_probe.csv', sep='\t')
probe_in = [probe_32, probe_7, probe_3, probe_2]

for i in range(1, 6):
	get_results(i, dos_in, exp='s', attack='dos', contamination=contamination_dos)

for i in range(1, 6):
	get_results(i, u2r_in, exp='s', attack='u2r', contamination=contamination_u2r)

for i in range(1, 6):
	get_results(i, r2l_in, exp='s', attack='r2l', contamination=contamination_r2l)

for i in range(1, 6):
	get_results(i, probe_in, exp='s', attack='probe', contamination=contamination_probe)