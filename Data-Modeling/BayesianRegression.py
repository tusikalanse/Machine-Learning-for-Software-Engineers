import sklearn.linear_model
import numpy as np

#using Bayesian regression

data = np.array([[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]])

price = np.array([10.99, 12.5 ,  9.99, 10.99, 11.99])

reg = sklearn.linear_model.BayesianRidge()
reg.fit(data, price)

print(reg.predict([[3000, 900], [1500, 700]]))
#[14.34471001  8.99777909]

print(reg.coef_)
#[0.00347274 0.00068913]
print(reg.intercept_)
#3.3062843444286365