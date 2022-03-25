## Overview of the project
Historical game data has become a pivotal component to analyze individual and team performance. 	Analyzing data has become an industry standard to improve working conventions and realize key business objectives. 

Basketball is one of the popular sports in North America and has a lot of data readily accessible for the public to see and use. This project will analyze the National Basketball Association seasonal game data and create a model that predicts which team will win in a given matchup. 

## Data Resources
- games.csv (Game results showing totals for both home and away teams on points, field goal percentage, assists, and rebounds)
- games_details.csv (Individual player stats by game. Includes points, field goal attempts, percentages, rebounds, assists, blocks, plus-minus etc.)
- players.csv (players details)
- ranking.csv (ranking of NBA given a day and season split into west and east on CONFERENCE column)
- teams.csv (Information about city, arena capacity, coaches, owners, years of operation)

Note: games_details.csv would need to be cleaned to assign each unique PLAYER_ID a numeric value across all of their games played, factoring in their total points, assists, rebounds, blocks etc.

Cleaned data table ("power_rankings_df") to be exported and stored on AWS S3 for shared team access.

All the data sources are from [Kaggle](https://www.kaggle.com/datasets/nathanlauga/nba-games)

## Key Objectives
1. Data Exploration & Visualization
    - Analysis of seasonal team data
    - Analysis of individual player data
    - Analysis of team key matchups
    - Calculations of ELO rating

2. Machine learning 
    - Create a prediction model for key team matchups

<img src='https://user-images.githubusercontent.com/85041697/159171394-7c7942bb-1fa4-4f02-a531-e75672845233.jpg' height=300 width=500>

## Outcomes

Using the data we gathered through this project we hope to create a working model to predict game-to-game outcomes of matchups between teams throughout the season. The team has a graet interest in the NBA in general so when we came up with this topic there we came to a unanimous decision to go ahead with it. 

