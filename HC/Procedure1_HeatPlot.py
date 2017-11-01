import seaborn as sns
import pandas
import numpy as np;
import matplotlib.pyplot as plt

#############################################################################
# Haonan Tong
#############################################################################

db = pandas.read_csv('DB2.csv',index_col = 'id')
data = db.loc[:,'log2r10':'log2r60']

#############################################################################
# Heat Plot
#############################################################################
cmap = sns.diverging_palette(250, 10, sep=20, l=55,  as_cmap=True)
g_hp = sns.heatmap(data, robust=True, yticklabels=False, center=0,vmin = -1, vmax = 1, cmap=cmap)
plt.savefig('Heatmap_Plot.pdf',bbox_inches='tight')

#############################################################################
# Clustermap
#############################################################################
# sns.clustermap
# Correlation as data point distance measurements; 
# UPGMA algorithm as cluster distance measurements.
sns.set(color_codes=True)

# print data.head()
g = sns.clustermap(data, robust=True, figsize=(7, 5),
	method='average', metric="correlation",center=0, vmin = -1, vmax = 1, col_cluster=False, cmap = cmap)
# plt.setp(g.ax_heatmap.get_yticklabels(), rotation=45)

g.ax_heatmap.set(yticks=[])
g.ax_heatmap.set(ylabel='')
g.cax.set_visible(False)
# g.ax_heatmap.set_title('Hierachical Clustering On Correlation-Based Disimilariy Meassurements')
# plt.show()

# save the figure
plt.savefig('Clustermap_Plot.pdf',bbox_inches='tight')
