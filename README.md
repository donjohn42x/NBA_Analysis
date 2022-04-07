## Overview of the project
Historical game data has become a pivotal component to analyze individual and team performance. Analyzing data has become an industry standard to improve working conventions and realize key business objectives. 

Basketball is one of the popular sports in North America and has a lot of data readily accessible for the public to see and use. This project will analyze the National Basketball Association seasonal game data and create a model that predicts which team will win in a given matchup. 

Using the data we gathered through this project we hope to create a working model to predict game-to-game outcomes of matchups between teams throughout the season. The team has a great interest in the NBA in general so when we came up with this topic there we came to a unanimous decision to go ahead with it. 

### Key Objectives
1. Data Exploration & Visualization
    - Analysis of seasonal team data
    - Analysis of individual player data
    - Analysis of team key matchups

2. Machine learning 
    - Create a prediction model for key team matchups

<img src='https://user-images.githubusercontent.com/85041697/159171394-7c7942bb-1fa4-4f02-a531-e75672845233.jpg' height=300 width=500>

## Database
### Data Retrieval
NBA game data was retrieved using a [python script for the NBA.com API](https://github.com/donjohn42x/NBA_Analysis/blob/tomoka_branch2/nba_api_scrape.ipynb). Multiple DataFrames were created to contain information on game records, individual player stats, and team details. These data files were exported into CSV files for our analysis.

- games.csv (Game results showing totals for both home and away teams on points, field goal percentage, assists, and rebounds)
- games_details.csv (Individual player stats by game. Includes points, field goal attempts, percentages, rebounds, assists, blocks, plus-minus etc.)
- players.csv (players details)
- teams.csv (Information about city, arena capacity, coaches, owners, years of operation)

![ERD_Diagram.png](https://github.com/donjohn42x/NBA_Analysis/blob/ryan_branch/Resources/README_images/ERD_Diagram.png)

### Database Storage
The postgresSQL database is being hosted on a public AWS RDS for shared team access, and to be connected the machine learning model in python. [Script](https://github.com/donjohn42x/NBA_Analysis/blob/tomoka_branch2/Database/connect_database.ipynb)

![aws_sql_connection.png](https://github.com/donjohn42x/NBA_Analysis/blob/ryan_branch/Resources/README_images/aws_sql_connection.png)

The script utilizes SQLAlchemy language to query and join the tables.

![sqlalchemy_join.png](https://github.com/donjohn42x/NBA_Analysis/blob/ryan_branch/Resources/README_images/sqlalchemy_join.png)

## Exploratory Analysis
To help identify the most important features, and possibly noisy variables, in relation to predicting win/loss outcomes from the data set, a python script was written to plot a [correlation matrix heat map](https://github.com/donjohn42x/NBA_Analysis/blob/main/CorrelationMatrix.ipynb) for our games data set.

Based on the below results, we will target our machine learning model to feature the following stats due to the strength of their correlation to WINS:
- Field goals attempted (FGA)
- Field goal percentage (FG_PCT)
- Three-point percentage (FG3_PCT)
- Rebounds (REB)
- Assists (AST)

![corr_matrix.png](https://github.com/donjohn42x/NBA_Analysis/blob/ryan_branch/Resources/README_images/corr_matrix.png)

Additional EDA was conducted to review if the home team had an advantage to win the game. The following diagram displays the difference in average team wins (1=win 0=loss) per year. Note: during the Covid-19 pandemic, the home team advantage was reduced, perhaps due to their being no crows in attendence.

![home_away](https://github.com/donjohn42x/NBA_Analysis/blob/249e014ce5be462a6685daedc3fffafce8d74a7c/Resources/README_images/Home%20vs%20Away.jpg)

## Machine Learning Model Overview
For the machine learning model selection, our project will be dealing with the following two assumptions:
- Supervised Learning – Since we are dealing with labeled data.
- Classification – Since we are dealing with Discrete Outcomes e.g. WIN/LOSS

We will be looking to implement a Logistic Regression model as we are looking for a classification between 0 (loss) and 1 (win).

### Preprocessing
The data will be pre-processed to create a feature for identifying whether the team played at home or away, as our EDA suggested there may be a relationship of the home team being more likely to win a game. The other numerical features were selected based on the correlation matrix and stored in the "needed_features" variable.

The [model](https://github.com/donjohn42x/NBA_Analysis/blob/main/nba_analysis.ipynb) was trained using DataFrames that took the average value of the key features over each respective teams' last ten games and using the "WIN" column as the output variable.

### Model Evaluation
- Initially we tried to use a [neural network model](https://github.com/donjohn42x/NBA_Analysis/blob/main/nba_analysis_NN.ipynb) to parse the data however we were unsatisified with the results of the accuracy. Through further investigation we discovered that even the best models out there have a working accuracy of about 70% so we are on the right track given it was our first attempt. 
- After talking with the instructors for some guidance we decided to go with two simpler models in an attempt to increase the accuracy, that is how we decided to use a Logistic Regresion model as well as a RandomForest model. 
- Problems we encountered with the Logistic Regression model: 
    - The main issues we ran into with the use of the Logistic Regression model was with choosing the correct variables to use. We had to go through much trial and error to get to the correct variables to use in the model as many of the categories are closesly correlated with each other, thus meaning it was bad for the model. The more things we tried to add the more problems we had so we used our [correlation matrix](https://github.com/donjohn42x/NBA_Analysis/commit/546fa7a8782a962c5a48888a78793c63973be574) to find the correct variables to use in our analysis. 
- Problems we encountered with the RandomForest model:
    - This is a relatively simple model unfortunetally, it does not take into account previous history. The accuracy of the RandomForest model, although better, is not well trained. We can enrich the model with additional features such as previous season's data as well as additional variables, the opposite approach to the Logistic Regression model. 
 
### Features (variables used to make a prediction): 
- Target (predicted outcome): HOME_TEAM_WINS (Games.csv)
- Dependencies (PENDING):
- import matplotlib.pyplot as plt
- import pandas as pd
- import numpy as np
- from sklearn.model_selection import train_test_split
- from imblearn.ensemble import BalancedRandomForestClassifier
- from sklearn.metrics import balanced_accuracy_score
- from skl

## Dashboard Design
### This is the webpage wireframe for the dashboard:
![dashboard_design.png](https://github.com/donjohn42x/NBA_Analysis/blob/ryan_branch/Resources/README_images/dashboard_design.png)

### Tools Used to Create the Final Dashboard
1. Figma.com - a free web-based application that allows users to create a website design with built-in templates and plug-ins. We used Figma to create the wireframe.
2. Pxcode.io - a free web-based appliation that allows users to create an HTML file from the figma wireframe.
3. HTML - The front-end programing language that will be used to create  the webpage

### Decription of the Interactive Elements
- The primary feature will be to create a "Game Win Predictor" interface that will allow a user to input a home team and away team for the machine learning model to output a winner of the matchup.
- Layered in this design will also have a presentation of the EDA visualizations as well as a description of the machine learning model selected.
- A possible future implementation is to create a button that will scrape more recent NBA data for the model as the current database is static.
