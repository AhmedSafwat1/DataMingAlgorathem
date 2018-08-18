from sklearn.datasets import load_diabetes
from sklearn.naive_bayes import GaussianNB
import numpy as np

iris = load_diabetes()
print(iris.data)
print(iris.feature_names)
print(iris.target)
model=GaussianNB()
model.fit(iris.data, iris.target)
predicted=model.predict([[.03,.05,.06,-.002,0.01,-0.01,.5,.4,.3,.1],[.5,0.1,.6,.9,.8,.1,10,11,12,13]])
predicted=predicted.astype(int)
from sklearn.metrics import confusion_matrix
expected=np.array([84,232])
expected = expected.astype(int)
print("expected",(expected))
predicted_by_Algorithm=predicted
print("predict" ,predicted)
results=confusion_matrix(predicted,expected)
print(results)
print("***************************")
print((results[0][0]),results[0][1],results[1][0],results[1][1])