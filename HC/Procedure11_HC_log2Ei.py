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

#############################################################################
# Study case when E_i
#############################################################################
db = pandas.read_csv('DB5.csv',index_col = 'id')
data = np.log2( db.loc[:,'t0':'t6'] )

Z = hierarchy.linkage(data,method = 'average',metric='correlation')

thr_list = [.45, 0.4, .35, 0.3, .25, 0.2, .15, 0.1]
for thr in thr_list:
    fig = plt.figure()

    fancy_dendrogram(
        Z,
        truncate_mode='lastp',
        p=50,
        leaf_rotation=90.,
        leaf_font_size=12.,
        show_contracted=True,
        annotate_above=thr,  # useful in small plots so annotations don't overlap
        max_d=thr ,  # plot a horizontal cut-off line

    )

    # plt.show()
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('log2Ei/HC_Threshold_'+str(thr)+'.pdf',bbox_inches='tight')

    from scipy.cluster.hierarchy import fcluster
    max_d = thr
    clusters = fcluster(Z, max_d, criterion='distance')
    print str(thr)
    db['HC_log2Ei_'+str(thr)] = clusters

    # db = db.sort_values(by=['HC'],ascending=[True])
    # print db['HC.45'].head(10)

    db.to_csv('DB6.csv')








