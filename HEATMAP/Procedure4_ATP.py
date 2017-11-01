import seaborn as sns
import pandas as pd
import numpy as np;
import matplotlib.pyplot as plt

#############################################################################
# Haonan Tong
#############################################################################

db = pd.read_csv('DB_Heatmap.csv',index_col = 'id')

ATP = range(1,7)
for atp in ATP:
	data_atp = db.loc[(db['ATP']==atp), "log2r10":"log2r60"]
	# cmap = sns.diverging_palette(220, 20, sep=20, center="dark", as_cmap=True)
	# cmap = sns.diverging_palette(220, 20, sep=20, l=55, as_cmap=True)
	# cmap = sns.diverging_palette(250, 10, sep=20, l=30, as_cmap=True)
	cmap = sns.diverging_palette(250, 10, sep=20, l=55, as_cmap=True)

	plt.figure()
	g_hp = sns.heatmap(data_atp, center = 0, vmin = -1, vmax = 1, robust=True, yticklabels=False, cmap=cmap)
	plt.savefig('ATP/Heatmap_atp'+`atp`+'.pdf' ,bbox_inches='tight')