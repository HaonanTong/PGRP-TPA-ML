import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np;

# def plotHeat(db):
# 	cmap = sns.diverging_palette(240, 10, n=21, center="dark")
# 	plt.figure()
# 	g_hp = sns.heatmap(db.loc[:,'log2r10':'log2r60'],  vmin=-3, vmax=3, yticklabels=False, cmap=cmap)
# 	# plt.show()

# db = pd.read_csv('HC.csv',index_col = 'id')
# for class_indx in db.HC.unique():
# 	db_tmp = db[(db['HC']==class_indx)]
# 	plotHeat(db_tmp)
# 	plt.savefig("HC_Cluster"+`class_indx`+".pdf",bbox_inches='tight')
db = pd.read_csv('DB3.csv',index_col = 'id')

# print len(db)
# print type(db['HC.45'].unique())
# cluster = np.sort(db['HC.45'].unique())
# HC_validation = pd.DataFrame({'cluster':cluster})
# HC_validation.set_index('cluster')
clusters = np.sort(db['HC.45'].unique())

#------------------------------------------------
ngenes = np.array([])
for cluster in clusters:
	db_tmp = db[(db['HC.45'] == cluster)]
	# print db_tmp.head(5)
	num_cluster = len(db_tmp)
	ngenes = np.append(ngenes, num_cluster)

#------------------------------------------------
nethylene = np.array([])
for cluster in clusters:
	db_tmp = db[(db['HC.45'] == cluster)&(db['ethylene']==1)]
	num_cluster = len(db_tmp)
	nethylene = np.append(nethylene, num_cluster)

#------------------------------------------------
nauxin = np.array([])
for cluster in clusters:
	db_tmp = db[(db['HC.45'] == cluster)&(db['auxin']==1)]
	num_cluster = len(db_tmp)
	nauxin = np.append(nauxin, num_cluster)

#------------------------------------------------
ncellwall = np.array([])
for cluster in clusters:
	db_tmp = db[(db['HC.45'] == cluster)&(db['cellwall']==1)]
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
