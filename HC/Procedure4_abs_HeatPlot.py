import seaborn as sns
import pandas
import numpy as np;
import matplotlib.pyplot as plt

#############################################################################
# Haonan Tong
#############################################################################

db = pandas.read_csv('ExpressionData_summary.csv',index_col = 'id')
# db_abs = db.loc[:,'log2r10':'log2r60'].abs()
# db_abs = db_abs.rename(columns=lambda x: 'abs'+x)
# ExpressionData_summary = pandas.concat([db, db_abs], axis=1)
# print ExpressionData_summary.head()

# ExpressionData_summary.to_csv('ExpressionData_summary.csv')
# raw_input("Press Enter to continue...")
data = db.loc[:,'abslog2r10':'abslog2r60']
print data.head()
# raw_input()
#############################################################################
# Heat Plot
#############################################################################
    # sns.palplot(sns.cubehelix_palette(n_colors=50, start=x, rot=0, light=0.7, dark=0))
# cmap = sns.color_palette('Greens', 7)
cmap = sns.diverging_palette(240, 10, n=21)

plt.figure(figsize = (10,5))
g_hp = sns.heatmap(data, cmap=cmap, robust=True,center=0, yticklabels=False, vmin=0, vmax=3)
fig = plt.gcf()
fig.show()
plt.savefig('Heatmap_abs_Plot.pdf',bbox_inches='tight')

#############################################################################
# Clustermap
#############################################################################
# sns.clustermap
# Correlation as data point distance measurements; 
# UPGMA algorithm as cluster distance measurements.
# sns.set(color_codes=True)

# print data.head()
cmap = sns.diverging_palette(240, 10, n=21)

g = sns.clustermap(data, robust=True, figsize=(10, 5),
	method='average', metric="correlation",center=0, col_cluster=False, cmap = cmap, vmin=0, vmax=3)
# plt.setp(g.ax_heatmap.get_yticklabels(), rotation=45)

g.ax_heatmap.set(yticks=[])
g.ax_heatmap.set(ylabel='')
g.cax.set_visible(False)
# g.ax_heatmap.set_title('Hierachical Clustering On Correlation-Based Disimilariy Meassurements')

# plt.show()


# # save the figure
# fig = plt.gcf()
# fig.set_size_inches(18.5, 10.5)
plt.savefig('Clustermap_abs_Plot.pdf',bbox_inches='tight')
