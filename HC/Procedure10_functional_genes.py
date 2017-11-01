import seaborn as sns
import pandas
import numpy as np;
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt


#############################################################################
# Functional Analysis
# For different feautres as input for Hierachical Clustering, which 
# are best in terms of correlation to describe the functional genes.
# Haonan Tong
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

def f_HC(data,file_str):
	Z = hierarchy.linkage(data,method = 'average',metric='correlation')
	plt.figure()

	fancy_dendrogram(
	    Z,
	    truncate_mode='none',
	    p=40,
	    leaf_rotation=90.,
	    leaf_font_size=12.,
	    show_contracted=True,
	    annotate_above=.5,  # useful in small plots so annotations don't overlap
	    max_d=.45 ,  # plot a horizontal cut-off line
	)

	# plt.show()
	fig = plt.gcf()
	fig.set_size_inches(18.5, 10.5)
	fig.savefig(file_str,bbox_inches='tight')


db = pandas.read_csv('DB5.csv',index_col = 'id')
# print list(db)
#############################################################################
# ethylene
#############################################################################
GO_str = 'ethylene'
#------------------------------------------------------------------
# Unnormalized t0-t6
data = db.loc[(db[GO_str]==1),'t0':'t6']
f_HC(data,'Functional_Genes/ethylene/untp.pdf')

#------------------------------------------------------------------
# Normalized t0-t6
data = db.loc[(db[GO_str]==1),'nfea_t0':'nfea_t6']
f_HC(data,'Functional_Genes/ethylene/ntp.pdf')

#------------------------------------------------------------------
# log2t0-t6
data = np.log2( db.loc[(db[GO_str]==1),'t0':'t6'] )
f_HC(data,'Functional_Genes/ethylene/log2untp.pdf')

#------------------------------------------------------------------
# abs log2t0-t6
data = np.log2( db.loc[(db[GO_str]==1),'t0':'t6'] )
data = data.abs()
f_HC(data,'Functional_Genes/'+GO_str+'/abslog2untp.pdf')

#------------------------------------------------------------------
# Unnormalized log2ratio
data = db.loc[(db[GO_str]==1),'log2r10':'log2r60']
f_HC(data,'Functional_Genes/ethylene/unlr.pdf')

#------------------------------------------------------------------
# Normalized log2ratio
data = db.loc[(db[GO_str]==1),'nfea_log2r10':'nfea_log2r60']
f_HC(data,'Functional_Genes/ethylene/nlr.pdf')

#------------------------------------------------------------------
# abs unnormalized log2ratio
data = db.loc[(db[GO_str]==1),'abslog2r10':'abslog2r60']
f_HC(data,'Functional_Genes/ethylene/abs_unlr.pdf')

#------------------------------------------------------------------
# normalized abs log2ratio
data = db.loc[(db[GO_str]==1),'abslog2r10':'abslog2r60']
data = ( data - data.mean() ) / data.std()
f_HC(data,'Functional_Genes/ethylene/abs_nlr.pdf')

#------------------------------------------------------------------
# Normalized log2ratio + t0:t6
data = db.loc[(db[GO_str]==1),'nfea_t0':'nfea_log2r60']
f_HC(data,'Functional_Genes/ethylene/n_tp_lr.pdf')


#############################################################################
# auxin
#############################################################################
GO_str = 'auxin'
#------------------------------------------------------------------
# Unnormalized t0-t6
data = db.loc[(db[GO_str]==1),'t0':'t6']
f_HC(data,'Functional_Genes/'+GO_str+'/untp.pdf')

#------------------------------------------------------------------
# Normalized t0-t6
data = db.loc[(db[GO_str]==1),'nfea_t0':'nfea_t6']
f_HC(data,'Functional_Genes/'+GO_str+'/ntp.pdf')

#------------------------------------------------------------------
# log2t0-t6
data = np.log2( db.loc[(db[GO_str]==1),'t0':'t6'] )
f_HC(data,'Functional_Genes/'+GO_str+'/log2untp.pdf')

#------------------------------------------------------------------
# abs log2t0-t6
data = np.log2( db.loc[(db[GO_str]==1),'t0':'t6'] )
data = data.abs()
f_HC(data,'Functional_Genes/'+GO_str+'/abslog2untp.pdf')

#------------------------------------------------------------------
# Unnormalized log2ratio
data = db.loc[(db[GO_str]==1),'log2r10':'log2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/unlr.pdf')

#------------------------------------------------------------------
# Normalized log2ratio
data = db.loc[(db[GO_str]==1),'nfea_log2r10':'nfea_log2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/nlr.pdf')

#------------------------------------------------------------------
# abs unnormalized log2ratio
data = db.loc[(db[GO_str]==1),'abslog2r10':'abslog2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/abs_unlr.pdf')

#------------------------------------------------------------------
# normalized abs log2ratio
data = db.loc[(db[GO_str]==1),'abslog2r10':'abslog2r60']
data = ( data - data.mean() ) / data.std()
f_HC(data,'Functional_Genes/'+GO_str+'/abs_nlr.pdf')

#------------------------------------------------------------------
# Normalized log2ratio + t0:t6
data = db.loc[(db[GO_str]==1),'nfea_t0':'nfea_log2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/n_tp_lr.pdf')



#############################################################################
# cellwall
#############################################################################
GO_str = 'cellwall'
#------------------------------------------------------------------
# Unnormalized t0-t6
data = db.loc[(db[GO_str]==1),'t0':'t6']
f_HC(data,'Functional_Genes/'+GO_str+'/untp.pdf')

#------------------------------------------------------------------
# Normalized t0-t6
data = db.loc[(db[GO_str]==1),'nfea_t0':'nfea_t6']
f_HC(data,'Functional_Genes/'+GO_str+'/ntp.pdf')

# log2t0-t6
data = np.log2( db.loc[(db[GO_str]==1),'t0':'t6'] )
f_HC(data,'Functional_Genes/'+GO_str+'/log2untp.pdf')

# abs log2t0-t6
data = np.log2( db.loc[(db[GO_str]==1),'t0':'t6'] )
data = data.abs()
f_HC(data,'Functional_Genes/'+GO_str+'/abslog2untp.pdf')

#------------------------------------------------------------------
# Unnormalized log2ratio
data = db.loc[(db[GO_str]==1),'log2r10':'log2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/unlr.pdf')

#------------------------------------------------------------------
# Normalized log2ratio
data = db.loc[(db[GO_str]==1),'nfea_log2r10':'nfea_log2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/nlr.pdf')

#------------------------------------------------------------------
# abs unnormalized log2ratio
data = db.loc[(db[GO_str]==1),'abslog2r10':'abslog2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/abs_unlr.pdf')

#------------------------------------------------------------------
# normalized abs log2ratio
data = db.loc[(db[GO_str]==1),'abslog2r10':'abslog2r60']
data = ( data - data.mean() ) / data.std()
f_HC(data,'Functional_Genes/'+GO_str+'/abs_nlr.pdf')

#------------------------------------------------------------------
# Normalized log2ratio + t0:t6
data = db.loc[(db[GO_str]==1),'nfea_t0':'nfea_log2r60']
f_HC(data,'Functional_Genes/'+GO_str+'/n_tp_lr.pdf')







