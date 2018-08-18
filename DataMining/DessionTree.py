from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
print("******************************")
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
sample=[[5.6,3,4.1,1.3]]
print(clf.predict([[5.9,0.5,5.1,1.8]]))


#******************************************
import graphviz
dot_data = tree.export_graphviz(clf,out_file=None)
graph = graphviz.Source(dot_data)

dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("iris",view=True)