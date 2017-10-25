import pandas
from sklearn.cluster import KMeans
#################################################################
def getNewLabel(kmeans):
	# Mapping expression level -1 0 1 => label as 0 1 2
	d = {'cluster_centers' : kmeans.cluster_centers_.tolist(), 'labeled_as' : [0, 1, 2]}
	d = pandas.DataFrame(d)

	d = d.sort_index(by=['cluster_centers'], ascending=[True])
	d['should_labeled_as'] = [0,1,2]

	L = list()
	for l in kmeans.labels_:
		indx = d['labeled_as'].tolist().index(l)
		# print indx 
		new_label = d['should_labeled_as'].tolist()[indx]
		# print new_label
		L.append(new_label)
		# print L
	return L
################################################################


db = pandas.read_csv('ExpressionData_summary.csv',index_col = 'id')
#print df.head()

features = db.loc[:,'nlog2r10':'nlog2r60']

################################################################
# TPA by KMEANS
################################################################
# ---------------------------------------------------------------
# Clustering based on tp1
X = features.loc[:,'nlog2r10']
X = X.values.reshape(-1,1) # make it to be array type
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Mapping the label
db['label10']=getNewLabel(kmeans)

# ---------------------------------------------------------------
# Clustering based on tp2
X = features.loc[:,'nlog2r20']
X = X.values.reshape(-1,1) # make it to be array type
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Mapping the label
db['label20']=getNewLabel(kmeans)

# ---------------------------------------------------------------
# Clustering based on tp3
X = features.loc[:,'nlog2r30']
X = X.values.reshape(-1,1) # make it to be array type
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Mapping the label
db['label30']=getNewLabel(kmeans)
print db.head()

# ---------------------------------------------------------------
# Clustering based on tp4
X = features.loc[:,'nlog2r40']
X = X.values.reshape(-1,1) # make it to be array type
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Mapping the label
db['label40']=getNewLabel(kmeans)

# ---------------------------------------------------------------
# Clustering based on tp5
X = features.loc[:,'nlog2r50']
X = X.values.reshape(-1,1) # make it to be array type
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# Mapping the label
db['label50']=getNewLabel(kmeans)


# ---------------------------------------------------------------
# Clustering based on tp6
X = features.loc[:,'nlog2r60']
X = X.values.reshape(-1,1) # make it to be array type
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
################################################################



# Mapping the label
db['label60']=getNewLabel(kmeans)

print db.loc[:,'nlog2r10':'label60'].head()

