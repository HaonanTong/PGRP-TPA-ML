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
# nTF Analysis
################################################################
# Ethylene Response
data_ethylene_nTF = db.loc[(db['ethylene']==1) & (db['TF']==0),"log2r10":"log2r60"]
plt.figure()
g_hp = sns.heatmap(data_ethylene_nTF, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/nTF/Heatmap_ethylene_nTF.pdf',bbox_inches='tight')

# Auxin Response
data_auxin_nTF = db.loc[(db['auxin']==1) & (db['TF']==0),"log2r10":"log2r60"]
plt.figure()
g_hp = sns.heatmap(data_auxin_nTF, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/nTF/Heatmap_auxin_nTF.pdf',bbox_inches='tight')

# cellwall Response
data_wall_nTF = db.loc[(db['cellwall']==1) & (db['TF']==0),"log2r10":"log2r60"]
plt.figure()
g_hp = sns.heatmap(data_wall_nTF, robust=True, yticklabels=False, center=0,vmin = -3, vmax = 3, cmap=cmap)
plt.savefig('GO/nTF/Heatmap_wall_nTF.pdf',bbox_inches='tight')



