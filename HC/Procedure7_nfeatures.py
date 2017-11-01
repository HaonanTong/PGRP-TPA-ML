import seaborn as sns
import pandas as pd
import numpy as np;
import matplotlib.pyplot as plt

#############################################################################
# Haonan Tong
#############################################################################
#------------------------------------------------------------------------------------------
# Generate normalized features
db = pd.read_csv('DB3.csv',index_col = 'id')
# print list(db)

myFeatures1 = np.log2(db.loc[:,'t0':'t6'])
# print myFeatures1.head()
myFeatures2 = db.loc[:,'log2r10':'log2r60']

myFeatures = pd.concat([myFeatures1, myFeatures2], axis=1, join='inner')
# print myFeatures.head()

# print myFeatures.mean()
# print myFeatures.std()

myFeatures_norm = (myFeatures - myFeatures.mean()) / myFeatures.std()
# print myFeatures_norm.mean()
# print myFeatures_norm.std()
myFeatures_norm = myFeatures_norm.rename(columns=lambda x: 'nfea_'+x)

print myFeatures_norm.head()
db4 = pd.concat([db, myFeatures_norm], axis=1, join='inner')
db4.to_csv('DB4.csv')

#------------------------------------------------------------------------------------------
# Heatplot
cmap = sns.diverging_palette(250, 10, sep=20, l=55,  as_cmap=True)
plt.subplots(figsize=(20,15))
g_hp = sns.heatmap(myFeatures_norm, robust=True, 
	yticklabels=False, center=0,vmin = -1, vmax = 1, cmap=cmap)
# plt.savefig('newFeatures/Heatmap_Plot.pdf',bbox_inches='tight')

#------------------------------------------------------------------------------------------
# Clustermap
sns.set(color_codes=True)

# print data.head()
g = sns.clustermap(myFeatures_norm, robust=True, figsize=(20, 15),
	method='average', metric="correlation",center=0, vmin = -1, vmax = 1, col_cluster=False, cmap = cmap)
# plt.setp(g.ax_heatmap.get_yticklabels(), rotation=45)

g.ax_heatmap.set(yticks=[])
g.ax_heatmap.set(ylabel='')
g.cax.set_visible(False)
# g.ax_heatmap.set_title('Hierachical Clustering On Correlation-Based Disimilariy Meassurements')
# plt.show()

# save the figure
# plt.savefig('newFeatures/Clustermap_Plot.pdf',bbox_inches='tight')