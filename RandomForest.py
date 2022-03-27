# Import our dependencies
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced


# Resample the training data with the BalancedRandomForestClassifier
from imblearn.ensemble import BalancedRandomForestClassifier
brf = BalancedRandomForestClassifier(n_estimators=100, random_state=1)
brf.fit(X_train, y_train)

# Build the model
 
h2o.init()
Train_h2o<-as.h2o(Full_df)
 
Train_h2o$H_Outcome<-as.factor(Train_h2o$H_Outcome)
 
# random forest model
model1 <- h2o.randomForest(y = 16, x=c(4:15), training_frame = Train_h2o, max_depth=4 )
 
h2o.performance(model1)