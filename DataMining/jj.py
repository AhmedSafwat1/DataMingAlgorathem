from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
data = np.genfromtxt("date.csv",delimiter=";")
x =data.astype(int);
try:
    k ="k"
    if k == "" or k == " ":
        raise NameError;
    k = int(k);
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(x)
    print(kmeans.labels_)
    print(kmeans.cluster_centers_)
    print({i: x[np.where(kmeans.labels_ == i)] for i in range(kmeans.n_clusters)})
except:
    print("errrpe")




from sklearn.datasets.twenty_newsgroups import strip_newsgroup_quoting


import csv
import numpy as np
person ={0:np.array([[1,2],[1,3],[1,4]]),1:np.array([[1,2],[1,3],[1,4]])}
def write_csv (i,x):
    filename = "cluster{}.csv".format(i);
    with open(filename,'w') as csvfile:
        writefil = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        for i in range(len(x)):
            writefil.writerow(x[i]);

for i in range(2):
    write_csv(i,person[i])