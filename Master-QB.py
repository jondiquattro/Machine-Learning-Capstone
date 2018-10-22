import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('MasterTeam.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values




from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

"""
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test= sc_X.fit_transform(X_test)   """

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)



import statsmodels.formula.api as sm
X = np.append(arr = np.ones((,1)).astype(int), values = X, axis = 1)
X_opt = X[:,[0, 1, 2, 3, 4,5]]
regressor_OLS = sm.OLS(endog =y, exog = X_opt).fit()

regressor_OLS.summary()


import statsmodels.formula.api as sm
X = np.append(arr = np.ones((114,1)).astype(int), values = X, axis = 1)
X_opt = X[:,[0, 1, 3, 4,5]]
regressor_OLS = sm.OLS(endog =y, exog = X_opt).fit()

regressor_OLS.summary()



y_pred = regressor.predict(X_test)


accuracy = regressor.score(X_test, y_test)


print(accuracy)