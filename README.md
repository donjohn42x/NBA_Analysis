# NBA_Analysis
Notes for database setup

Data files retrieved from:
https://www.kaggle.com/nathanlauga/nba-games

games.csv - Game results showing totals for both home and away teams on points, field goal percentage, assists, and rebounds
game_details.csv - Individual player stats by game. Includes points, field goal attempts, percentages, rebounds, assists, blocks, plus-minus etc.
ranking.csv - Total standings (win-loss records) for every calendar day during a given season
teams.csv - Information about city, arena capacity, coaches, owners, years of operation
players.csv - Player names by season they were active

games_details.csv would need to be cleaned to assign each unique PLAYER_ID a numeric value across all of their games played, factoring in their total points, assists, rebounds, blocks etc.

Cleaned data table ("power_rankings_df") to be exported and stored on AWS S3 for shared team access.