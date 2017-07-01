import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import math

from sklearn.linear_model import LinearRegression

data = pd.read_csv('../homicide_database.csv')
# data.head()

data_  = data[['Record ID' , 'Victim Age' , 'Perpetrator Age']]
# ignore the 998 victim age
data_ = data_[data_['Victim Age'] != 998]

# the ' ' value at this id causing problems
data_ = data_.replace(to_replace = ' ' , value = '0')

data_['Perpetrator Age'] = [int(s) for s in data_['Perpetrator Age']]

train = data_[data_['Perpetrator Age'] != 0]
test = data_[data_['Perpetrator Age'] == 0]

lm = LinearRegression()
lm.fit(np.array(train[['Victim Age']] ), np.array(train[['Perpetrator Age']]))

plt.figure(0)
plt.scatter(train['Victim Age'] , train['Perpetrator Age'])
plt.plot(train['Victim Age'] , lm.predict(train[['Victim Age']]) , color = 'red')
plt.show()


test.loc[: ,'Perpetrator Age'] =lm.predict(test[['Victim Age']])
test['Perpetrator Age'] = [math.ceil(s*1) for s in test['Perpetrator Age']]
print "The new Prepetrator Age has been Predicted!!"
