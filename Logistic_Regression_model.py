
# Model Training
from sklearn.model_selection import train_test_split

final_team_stats = pd.read_csv('Our dataframe here', index_col = 0)

cols = [relevant coloums listed 1,2,3, etc.]
final_team_stats.drop(final_team_stats.columns[cols],axis=1, inplace=True)

features = final_team_stats.drop(columns = 'Label')
label = final_team_stats['Label']

x_train, x_test, y_train, y_test = train_test_split(features, label, test_size = 0.2)



# Import our dependencies(not sure about these yet)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
import tensorflow as tf
import os


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