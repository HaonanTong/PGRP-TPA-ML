import seaborn as sns
import pandas
import numpy as np;
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

#############################################################################
# Derive Threshold for Hierarchical Clustering
# Haonan Tong
# Reference: https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/#Plotting-a-Dendrogram
#############################################################################


def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata

db = pandas.read_csv('DB4.csv',index_col = 'id')
data = db.loc[:,'nfea_t0':'nfea_log2r60']

Z = hierarchy.linkage(data,method = 'average',metric='correlation')

fancy_dendrogram(
    Z,
    truncate_mode='lastp',
    p=40,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,
    annotate_above=.8,  # useful in small plots so annotations don't overlap
    max_d=.7 ,  # plot a horizontal cut-off line

)

# plt.show()
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('newFeatures/HC_Threshold.pdf',bbox_inches='tight')

from scipy.cluster.hierarchy import fcluster
max_d = .7
clusters = fcluster(Z, max_d, criterion='distance')
db['HC_nFea.7'] = clusters

# db = db.sort_values(by=['HC'],ascending=[True])
print db['HC_nFea.7'].head(10)

db.to_csv('DB5 .csv')








