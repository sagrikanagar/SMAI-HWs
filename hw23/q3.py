from sklearn.linear_model import Perceptron

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA


def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    num_points = len(lines)
    dim_points = 28 * 28
    data = np.empty((num_points, dim_points))
    labels = np.empty(num_points)

    for ind, line in enumerate(lines):
        num = line.split(',')
        labels[ind] = int(num[0])
        data[ind] = [int(x) for x in num[1:]]

    return (data, labels)

X, y = read_data("sample_train.csv")
test_data, test_labels = read_data("sample_test.csv")
print(test_data.shape)

pca = PCA(n_components=2)
X_k = pca.fit_transform(test_data)

X = X_k
kmeans = KMeans(n_clusters=10).fit(X)
y_kmeans = kmeans.predict(X)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans)
plt.show()

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=test_labels)   
plt.show() 