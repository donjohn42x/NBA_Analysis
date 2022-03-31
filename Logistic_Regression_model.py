# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
import tensorflow as tf
# Import checkpoint dependencies
import os
import pandas as pd 

from sklearn.linear_model import LogisticRegression 
from sklearn import metrics

# create a simple, non-parameterized Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(metrics.accuracy_score(y_test, y_pred))

from pprint import pprint
# Look at parameters used by our current forest
print('Parameters currently in use:\n')
pprint(model.get_params())

# create complex Logistic Regression with max_iter=131 
log_model = LogisticRegression(max_iter=131, verbose=2, random_state=42)
log_model.fit(x_train, y_train)
y_pred_log = log_model.predict(x_test)
print(metrics.accuracy_score(y_test, y_pred_log))