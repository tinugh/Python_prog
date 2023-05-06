
#sklearn======>package name
#neighbours===>module
#KNeighboursClassifier=====>function
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3) #k=3
x1=[7,7,3,1]
y1=[7,4,4,4]
target=['bad','bad','good','good']

#[(7,7),(7,4),(3,4),(1,4)]
#zip' function is used for combining
features=list(zip(x1,y1))
print(features)

#fit function
knn.fit(features,target)  #model_creation
print(knn.predict([[3,7]]))









