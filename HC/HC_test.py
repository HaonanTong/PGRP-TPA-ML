from scipy.cluster import hierarchy
import numpy as np
import scipy
import matplotlib.pyplot as plt

x = np.random.rand(10).reshape(5, 2)
print x
Z = hierarchy.linkage(x,method = 'average',metric='correlation')

print Z

print 'Z[0]:', Z[0]

fig = plt.figure(figsize=(7, 5))
dn = scipy.cluster.hierarchy.dendrogram(Z)
plt.show()

# hierarchy.to_tree(Z)

rootnode, nodelist = hierarchy.to_tree(Z, rd=True)
# print rootnode.get_count()
# print rootnode.get_id()
# print nodelist
