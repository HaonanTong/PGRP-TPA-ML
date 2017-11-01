import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np;

# get_Cluster_infor: Associate functional terms with each cluster
def get_Cluster_infor(db, cluster_str):
	clusters = np.sort(db[cluster_str].unique())

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

	print HC_validation

	print HC_validation[(HC_validation['#auxin']!=0) | 
						(HC_validation['#cellwall']!=0) | 
						(HC_validation['#ethylene']!=0)]


db = pd.read_csv('DB5.csv',index_col = 'id')
cluster_str = 'HC_nFea.7'
get_Cluster_infor(db,cluster_str)


db = pd.read_csv('DB5.csv',index_col = 'id')
cluster_str = 'ATP'
get_Cluster_infor(db,cluster_str)
