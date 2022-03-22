# NBA_Analysis
Shared Repository for Capstone Project
Machine Learning Model Overview:
Supervised Learning – Since we are dealing with labeled data.
Classification – Since we are dealing with Discrete Outcomes e.g. WIN/LOSS.
Logistic Regression – Since we are predicting binary outcomes i.e. WIN/LOSS
 
Features (variables used to make a prediction): 
Target (predicted outcome): HOME_TEAM_WINS (Games.csv)
Dependencies (PENDING):
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
