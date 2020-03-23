import sklearn.linear_model
import numpy as np

#using LASSO regression

data = np.array([[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]])

price = np.array([10.99, 12.5 ,  9.99, 10.99, 11.99])

reg = sklearn.linear_model.Lasso()
reg.fit(data, price)

print(reg.predict([[3000, 900], [1500, 700]]))
#[14.35089041  9.01561644]

print(reg.coef_)
#[0.00355685 0.        ]
print(reg.intercept_)
#3.6803424657534265