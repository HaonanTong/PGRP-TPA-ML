import seaborn as sns
import pandas as pd
import numpy as np;
import matplotlib.pyplot as plt

#############################################################################
# Haonan Tong
#############################################################################

db = pd.read_csv('DB_Heatmap.csv',index_col = 'id')
cmap = sns.diverging_palette(250, 10, sep=20, l=55,  as_cmap=True)

################################################################
# TF Analysis
################################################################
# Ethylene Response
data_ethylene_TF = db.loc[(db['ethylene']==1) & (db['TF']==1),"log2r10":"log2r60"]
plt.figure()
g_hp = sns.heatmap(data_ethylene_TF, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/TF/Heatmap_ethylene_TF.pdf',bbox_inches='tight')

# Auxin Response
data_auxin_TF = db.loc[(db['auxin']==1) & (db['TF']==1),"log2r10":"log2r60"]
plt.figure()
g_hp = sns.heatmap(data_auxin_TF, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/TF/Heatmap_auxin_TF.pdf',bbox_inches='tight')

# cellwall Response
data_wall_TF = db.loc[(db['cellwall']==1) & (db['TF']==1),"log2r10":"log2r60"]
plt.figure()
g_hp = sns.heatmap(data_wall_TF, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/TF/Heatmap_wall_TF.pdf',bbox_inches='tight')



