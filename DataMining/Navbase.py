
from sklearn.naive_bayes import GaussianNB
import numpy as np

x=np.array([ [-3,7] , [1,5] , [1,2] , [-2,0] , [2,3] , [-4,0] , [-1,1] , [1,1] , [-2,2] , [2,7] , [-4,1] ,[-2,7] ])

print(x)

y=np.array([3,3,3,3,4,3,3,4,3,4,4,4])

print(y)

#create a GaussianNB Classifier
model=GaussianNB()

#train Model using Training Sets

model.fit(x,y)

predicted=model.predict([ [-3,7] , [1,5] , [1,2] , [-2,0] , [2,3] , [-4,0] , [-1,1] , [1,1] , [-2,2] , [2,7] , [-4,1] ,[-2,7] ])
print (predicted)


from sklearn.metrics import confusion_matrix
expected=y
predicted_by_Algorithm=predicted

results=confusion_matrix(predicted,expected)
print(results)
print((results[0][0]),results[0][1],results[1][0],results[1][1])






