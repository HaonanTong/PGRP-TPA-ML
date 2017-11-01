import seaborn as sns
import pandas as pd
import numpy as np;
import matplotlib.pyplot as plt


db = pd.read_csv('DB.csv',index_col = 'id')
tb = pd.read_csv('Table_Summary_Gene2.csv',index_col = 'ID')

# print tb[tb['TF']==1].head()
db['TF'] = 0
# print db.head()
db.loc[(tb['TF'] == 1),'TF'] = 1
# print db['TF'].value_counts()
# print db.loc[(db['TF'] == 1),:]

db['ethylene'] = 0
db.loc[(tb['GO0009723'] == 1),'ethylene'] = 1

db['auxin'] = 0
db.loc[(tb['GO0009733'] == 1),'auxin'] = 1

db['cellwall'] = 0
db.loc[(tb['GO0071555'] == 1),'cellwall'] = 1

db['ATP'] = 0
# print range(1,7)
for i in range(1,7):
	db.loc[(tb['ATP'] == i),'ATP'] = i

# print db.head()
# print db[db['TF']==1].head()
db.to_csv('DB2.csv')


