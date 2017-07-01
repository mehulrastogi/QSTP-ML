import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import scipy.stats as stats


data =  pd.read_csv('../sat.csv')
data.shape

from sklearn.linear_model import LinearRegression

X= (data.iloc[: , :-1])
y =(data.iloc[:, -1])

ln = LinearRegression()
ln.fit(X[['high_GPA']],y)


print "The coef of the equation are :",ln.coef_[0]
print "The intercept of the equation is" ,ln.intercept_
print "The MSE on the training set is :" , np.mean((y - ln.predict(X[['high_GPA']]))**2)


plt.figure(1)
plt.scatter(X[['high_GPA']], y)
plt.plot(X[['high_GPA']] , ln.predict(X[['high_GPA']]) , color = 'red')
plt.show()