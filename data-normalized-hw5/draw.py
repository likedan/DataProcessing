import scipy
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt
import numpy as np
X = np.array([[8,8],
[1,3],
 [1,2],
 [2,1],
 [2,2],
 [2,3],
 [3,2],
 [4,3],
 [6,3],
 [4,5],
 [5,4],
 [5,5],
 [6,4],
 [6,5]
 ]
)
print X
d = sch.distance.pdist(X)
print d
Z= sch.linkage(d,method='single')
print Z
P =sch.dendrogram(Z)
plt.show()
