# Create a K-means clustering algorithm to group customers of a retail store based on their purchase history. 
# Dataset :- https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

import  pandas as pd
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import seaborn as sns

customer_data  = pd.read_csv('C:\\Users\\riyaz\\Desktop\\Prodigy Infotech\\Prodigy-ML-02\\Mall_Customers.csv')

X = customer_data.iloc[:,3:].values

wcss = []

for i in range ( 1 , 11):
    Kmeans = KMeans(n_clusters=i, random_state= 42 , init="k-means++")
    Kmeans.fit_predict(X)
    wcss.append(Kmeans.inertia_)

# sns.set() 
# plt.plot(range (1,11), wcss) 
# plt.title("The Libow Point Graph") 
# plt.xlabel("Number of Clusters")
# plt.ylabel("WCSS") 
# plt.show()


# clusters = 5 # from graph

Kmeans = KMeans(n_clusters=5, random_state= 42 , init="k-means++")
clusters = Kmeans.fit_predict(X)
Y = Kmeans.fit_predict(X)
# print(clusters)

plt.figure(figsize=(8,8)) 
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Cluster 1') 
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Cluster 2') 
plt.scatter (X[Y==2,0], X[Y==2,1], s=50, c='blue', label='Cluster 3') 
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c='violet', label='Cluster 4') 
plt.scatter (X[Y==4,0], X[Y==4,1], s=50, c='purple', label='Cluster 5')

plt.scatter(Kmeans.cluster_centers_[:,0], Kmeans.cluster_centers_[:,1],s=100,c='cyan', label = "Centroids")

plt.show()