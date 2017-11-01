import seaborn as sns
import pandas as pd
import numpy as np;
import matplotlib.pyplot as plt

#############################################################################
# Haonan Tong
#############################################################################

db = pd.read_csv('DB_Heatmap.csv',index_col = 'id')

# Ethylene Response
data_ethylene = db.loc[(db['ethylene']==1),"log2r10":"log2r60"]
# cmap = sns.diverging_palette(240, 10, n=5, center="dark")
cmap = sns.diverging_palette(250, 10, sep=20, l=55,  as_cmap=True)

plt.figure()
g_hp = sns.heatmap(data_ethylene, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/ALL/Heatmap_ethylene_ALL.pdf',bbox_inches='tight')

# Auxin Response
data_auxin = db.loc[(db['auxin']==1),"log2r10":"log2r60"]
# cmap = sns.diverging_palette(240, 10, n=5, center="dark")
plt.figure()
g_hp = sns.heatmap(data_auxin, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/ALL/Heatmap_auxin_ALL.pdf',bbox_inches='tight')

# cellwall Response
data_wall = db.loc[(db['cellwall']==1),"log2r10":"log2r60"]
# cmap = sns.diverging_palette(240, 10, n=5, center="dark")
plt.figure()
g_hp = sns.heatmap(data_wall, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/ALL/Heatmap_wall_ALL.pdf',bbox_inches='tight')



