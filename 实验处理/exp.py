import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# 聚类中心
centroids = kmeans.cluster_centers_
print("聚类中心：", centroids)

# 每个样本所属的聚类
labels = kmeans.labels_
print("每个样本所属的聚类：", labels)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('K - Means Clustering on Iris Dataset')
plt.show()

from sklearn.metrics import silhouette_score
silhouette_avg = silhouette_score(X, labels)
print("轮廓系数：", silhouette_avg)