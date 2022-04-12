#Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, accuracy_score, roc_curve, roc_auc_score
import pandas as pd
import os
from rds import db_password
from psycopg2 import sql, connect
from matplotlib import pyplot
import matplotlib.pylab as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4



try:
    # declare a new PostgreSQL connection object
    conn = connect(
        dbname = "db name here",
        user = "postgres",
        host = "host address here",
        port = "port number",
        password = db_password
    )

    # print the connection if successful
    print ("psycopg2 connection:", conn)

except Exception as err:
    print ("psycopg2 connect() ERROR:", err)
    conn = None



cr = conn.cursor()
cr.execute('SELECT * FROM "data table name";')
tmp = cr.fetchall()

# Extract the column names
col_names = []
for elt in cr.description:
    col_names.append(elt[0])

# Create the dataframe, passing in the list of col_names extracted from the description
df = pd.DataFrame(tmp, columns=col_names)


## Preprocessing Data

# Select features 

""" not sure about this 
# Drop the null comumns where all values are null
df = df.dropna(axis='columns', how='all')

# Drop the null rows
df = df.dropna()

# Convert the target column values to win/loss based on their values
x = {'1': 'Win'}   
df = df.replace(x)

x = {'0': 'Loss'}   
df = df.replace(x)

df.reset_index(inplace=True, drop=True)

df.head() """

#create column with FGA difference between teams
trans_df["FGA_DIFF"]=trans_df["FGA_HOME"]-trans_df["FGA_AWAY"]
trans_df.drop(columns=["FGA_HOME","FGA_AWAY"], inplace=True)
trans_df.head()

#Create column with FG percent ratio between teams
trans_df["FG_PCT_RATIO"]=trans_df["FG_PCT_HOME"]/trans_df["FG_PCT_AWAY"]
trans_df.drop(columns=["FG_PCT_HOME", "FG_PCT_AWAY"], inplace=True)

#Create column with 3-point FG percent ratio between teams
trans_df["FG3_PCT_RATIO"] = trans_df["FG3_PCT_HOME"]/trans_df["FG3_PCT_AWAY"]
trans_df.drop(columns=["FG3_PCT_HOME", "FG3_PCT_AWAY"], inplace = True)

#Create column with Defensive rebound difference between teams
trans_df["DREB_DIFF"]=trans_df["DREB_HOME"]-trans_df["DREB_AWAY"]
trans_df.drop(columns=["DREB_HOME", "DREB_AWAY"], inplace =True)

#Create column with rebound difference between teams
trans_df["REB_DIFF"]=trans_df["REB_HOME"]-trans_df["REB_AWAY"]
trans_df.drop(columns=["REB_HOME","REB_AWAY"], inplace=True)

#Create column with assist difference between teams
trans_df["AST_DIFF"]=trans_df["AST_HOME"]-trans_df["AST_AWAY"]
trans_df.drop(columns=["AST_HOME","AST_AWAY"], inplace=True)

win=trans_df["WIN"]
trans_df.head()

win=trans_df["WIN"]
trans_df.drop(columns=["WIN"], inplace=True)
trans_df["WIN"]=win
trans_df.head()


# Split our preprocessed data into our features and target arrays

#Creating input and output data
trans_df["WIN"] = y
y = trans_df["WIN"]
X_df = trans_df.drop(["WIN"], axis=1)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_df, y, random_state=1, stratify=y)

# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Implementing Logistic Regression
from imblearn.over_sampling import RandomOverSampler
from collections import Counter
ros = RandomOverSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train_scaled, y_train)
Counter(y_resampled)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='lbfgs', random_state=1)
model.fit(X_resampled, y_resampled)

from sklearn.metrics import balanced_accuracy_score
balanced_accuracy_score(y_test, y_pred)

# Get the probability
prob = model.predict_proba(X_test_scaled)