import pandas
import numpy as np

df = pandas.read_csv('Profiles-ANan-DEGs-Filtered.csv',index_col = 'id')

# print df[0:5]
# print df.head()
# print df.iloc[:,[1]].head()
# print df.mean()
# print df.mean(1)

t0 = df.iloc[:,[0,1,2]]
t1 = df.iloc[:,[3,4,5]]
t2 = df.iloc[:,[6,7,8]]
t3 = df.iloc[:,[9,10,11]]
t4 = df.iloc[:,[12,13,14]]
t5 = df.iloc[:,[15,16,17]]
t6 = df.iloc[:,[18,19,20]]


# TimeSeries
df['t0'] = t0.mean(1)
df['t1'] = t1.mean(1)
df['t2'] = t2.mean(1)
df['t3'] = t3.mean(1)
df['t4'] = t4.mean(1)
df['t5'] = t5.mean(1)
df['t6'] = t6.mean(1)

# ratio to zero time point
df['r00'] = np.divide(df['t0'],df['t0'])
df['r10'] = np.divide(df['t1'],df['t0'])
df['r20'] = np.divide(df['t2'],df['t0'])
df['r30'] = np.divide(df['t3'],df['t0'])
df['r40'] = np.divide(df['t4'],df['t0'])
df['r50'] = np.divide(df['t5'],df['t0'])
df['r60'] = np.divide(df['t6'],df['t0'])

# log2(ratio)
df['log2r00'] = np.log2(df['r00'])
df['log2r10'] = np.log2(df['r10'])
df['log2r20'] = np.log2(df['r20'])
df['log2r30'] = np.log2(df['r30'])
df['log2r40'] = np.log2(df['r40'])
df['log2r50'] = np.log2(df['r50'])
df['log2r60'] = np.log2(df['r60'])

df['log2mean'] = df.loc[:,'log2r10':'log2r60'].mean(1)
df['log2std'] = df.loc[:,'log2r10':'log2r60'].std(1)
print df.head()

## normalize log2ratio to be mean = 0, std = 1 for a given gene object
df_norm = df.loc[:,'log2r10':'log2r60'].sub(df['log2mean'], axis='index')
print df_norm.head()
std_mtrx = np.tile(df['log2std'], (6, 1))
std_mtrx =  std_mtrx.conj().T
df_norm = np.divide(df_norm,std_mtrx)
# df.rename(columns=lambda x: x+'x' if x in os_list else x)
df_norm = df_norm.rename(columns=lambda x: 'n'+x)
print df_norm.head()

# print df_norm.mean(1).head()
# print df_norm.std(1).head()
ExpressionData_summary = pandas.concat([df, df_norm], axis=1)
print ExpressionData_summary.head()

ExpressionData_summary.to_csv('ExpressionData_summary.csv')



