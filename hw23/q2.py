from sklearn.metrics import silhouette_score

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans


mean = (100, 100)
cov = [[1, 0], [0, 1]]
s1 = np.random.multivariate_normal(mean, cov, 5)
y1 = np.ones(5)

mean = (0, 0)
cov = [[1, 0], [0, 1]]
s2 = np.random.multivariate_normal(mean, cov, 5)
y2 = np.zeros(5)

x = np.concatenate((s1, s2), axis=0)
print(x)
y = np.concatenate((y1, y2), axis=0)
print(y)


X = x
val = []
k = []

for n_cluster in range(2, 10):
    kmeans = KMeans(n_clusters=n_cluster).fit(X)
    label = kmeans.labels_
    sil_coeff = silhouette_score(X, label, metric='euclidean')
    print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))
    val.append(sil_coeff)
    k.append(n_cluster)

plt.figure()
plt.plot(k,val)
plt.xlabel("Number of cluster")
plt.show()
    