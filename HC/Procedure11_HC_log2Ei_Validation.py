import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np;

# get_Cluster_infor: Associate functional terms with each cluster
def get_Cluster_infor(db, cluster_str):
	clusters = np.sort(db[cluster_str].unique())
	# print type(clusters)
	print 'Totally clusters: '+str(clusters[-1])
	#------------------------------------------------
	ngenes = np.array([])
	for cluster in clusters:
		db_tmp = db[(db[cluster_str] == cluster)]
		# print db_tmp.head(5)
		num_cluster = len(db_tmp)
		ngenes = np.append(ngenes, num_cluster)

	#------------------------------------------------
	nethylene = np.array([])
	for cluster in clusters:
		db_tmp = db[(db[cluster_str] == cluster)&(db['ethylene']==1)]
		num_cluster = len(db_tmp)
		nethylene = np.append(nethylene, num_cluster)

	#------------------------------------------------
	nauxin = np.array([])
	for cluster in clusters:
		db_tmp = db[(db[cluster_str] == cluster)&(db['auxin']==1)]
		num_cluster = len(db_tmp)
		nauxin = np.append(nauxin, num_cluster)

	#------------------------------------------------
	ncellwall = np.array([])
	for cluster in clusters:
		db_tmp = db[(db[cluster_str] == cluster)&(db['cellwall']==1)]
		num_cluster = len(db_tmp)
		ncellwall = np.append(ncellwall, num_cluster)


	HC_validation = pd.DataFrame({'clusters':clusters,
		'#genes':ngenes,
		'#ethylene':nethylene,
		'#auxin':nauxin,
		'#cellwall':ncellwall})
	HC_validation.set_index('clusters', inplace=True)

	# print HC_validation

	print HC_validation[(HC_validation['#auxin'] > 10) | 
						(HC_validation['#cellwall'] > 10) | 
						(HC_validation['#ethylene'] > 10)]


db = pd.read_csv('DB6.csv',index_col = 'id')
thr_list = [0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1]
List_cluster_str = ['HC_log2Ei_0.45','HC_log2Ei_0.4','HC_log2Ei_0.3','HC_log2Ei_0.2','HC_log2Ei_0.1']
for thr in thr_list:
	print '----------------------------------------'
	print 'Threshold set as: '+str(thr)
	cluster_str = 'HC_log2Ei_'+str(thr)
	get_Cluster_infor(db,cluster_str)
	print '----------------------------------------'



