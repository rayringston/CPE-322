import matplotlib.pyplot as plt
from pandas import *
from scipy import stats
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model

from sklearn.metrics import r2_score
#---------------- import this function from scikit-learn


X = read_csv('cpudata.csv', usecols=[1])
# changed from 'rpidata1.csv' to 'cpudata.csv'

X = X.assign(t = X.index)
y = read_csv('cpudata.csv', usecols=[2])
# changed from 'rpidata1.csv' to 'cpudata.csv'

lr = linear_model.LinearRegression()
predicted = cross_val_predict(lr, X, y, cv=10)
print("R Squared: ", r2_score(y, predicted))
#---------------- print the R squared value of the linear regression model

plt.plot(y, predicted, 'ro')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'b-', lw=2)
plt.xlabel('Memory Available GB')
plt.ylabel('Predicted')
plt.title('Predicted vs. Memory Available')

plt.show()
