from flask import Flask, request, url_for, render_template, redirect, abort, flash,jsonify
import psycopg2
import pandas as pd
from config import aws

app = Flask(__name__) 

@app.route('/')
def posts():
    return render_template("Index.html")

@app.route('/win_predict',methods=['GET','POST'])
def game_win_predictor():
    return render_template("predictor.html")

@app.route('/getteams', methods=['GET','POST'])
def get_teams():

    if request.method == 'POST':
        # gets the text from the webpage
        home_team = request.form.get('home')
        away_team = request.form.get('away')

        # generate the table from your two teams
        print(home_team, away_team)


        # read in your model
        
        # pass in the data into the model
        # result from model is 1
        res = 1
        if res == 1:
            result = "Home team wins"
        else:
            result = "Away team wins"
       
        # print(f"This is python printing something from front-end - {status}")
        return render_template('predictor.html', winner=result)
    else:
        return redirect(url_for("posts"))

# Import game detail data from database
@app.route('/data')
def read_data():
    # df = pd.read_csv('static/nba_game_details_cleaned.csv')
    conn = psycopg2.connect(
    database="NBA_ML",
    user="root",
    password=aws,
    host="root.cv2swqkze1kh.us-east-1.rds.amazonaws.com",
    port='5432'
    )

    cursor = conn.cursor()
    cursor.execute("select * from game_details")
    games = cursor.fetchall()
    games = jsonify(games)

    columns = ['GAME_ID', 'GAME_DATE', 'TEAM_away', 'TEAM_home', 'TEAM_ID_away',
       'TEAM_ID_home', 'WL_away', 'WL_home', 'FGM_away', 'FGM_home',
       'FGA_away', 'FGA_home', 'FG_PCT_away', 'FG_PCT_home', 'FG3_PCT_away',
       'FG3_PCT_home', 'FTM_away', 'FTM_home', 'FTA_away', 'FTA_home',
       'FT_PCT_away', 'FT_PCT_home', 'OREB_away', 'OREB_home', 'DREB_away',
       'DREB_home', 'REB_away', 'REB_home', 'AST_away', 'AST_home', 'STL_away',
       'STL_home', 'BLK_away', 'BLK_home', 'TOV_away', 'TOV_home', 'PF_away',
       'PF_home', 'PTS_away', 'PTS_home', 'WIN_home']

    return games
    
    # return games


@app.route('/analysis',methods=['GET','POST'])
def analysis():
    return render_template("Insights_Analytics1.html")


@app.route('/ml',methods=['GET','POST'])
def ml():
    return render_template("MachineLearning.html")

    
if __name__ == "__main__":
    app.run(debug=True)

