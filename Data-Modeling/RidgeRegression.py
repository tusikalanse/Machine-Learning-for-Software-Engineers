import sklearn.linear_model
import numpy as np

#using ridge regression

data = np.array([[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]])

price = np.array([10.99, 12.5 ,  9.99, 10.99, 11.99])

reg = sklearn.linear_model.Ridge()
reg.fit(data, price)

print(reg.predict([[3000, 900], [1500, 700]]))
#[14.36146855  8.93208821]

print(reg.coef_)
#[0.00330976 0.00232372]
print(reg.intercept_)
#2.340845980549572