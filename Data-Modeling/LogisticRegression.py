import sklearn.linear_model
import numpy as np

#using Logistic regression
###########binary classification

data = np.array([[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]])

price = np.array([1, 0,  1, 1, 1])

reg = sklearn.linear_model.LogisticRegression()
reg.fit(data, price)

print(reg.predict([[3000, 900], [1500, 700]]))
#[0 1]