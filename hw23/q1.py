from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


points = np.array([[5,3],[10,15],[15,12],[24,10],[30,45],[85,70],[71,80],[60,78],[55,52],[80,91],])

plt.scatter(points[:,0],points[:,1], label='True Position')

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print(kmeans.cluster_centers_)
print(kmeans.labels_)

plt.figure()
plt.scatter(points[:,0],points[:,1], c=kmeans.labels_, cmap='rainbow')
plt.show()

plt.figure()
plt.scatter(points[:,0], points[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.show()






