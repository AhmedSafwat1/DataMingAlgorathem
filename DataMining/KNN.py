from sklearn.neighbors import KNeighborsClassifier
import csv
import numpy as np
neigh = KNeighborsClassifier(n_neighbors=3)
data = np.genfromtxt("date.csv",delimiter=";")
x=data.astype(int)
print(x)
print("**************")
targat = np.genfromtxt("output.csv",delimiter=";")
y = targat.astype(int)
print(y)
neigh.fit(x,y);
print(neigh.predict([[64,65]]))