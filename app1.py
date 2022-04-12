from flask import Flask, request, url_for, render_template, redirect, abort, flash,jsonify
import psycopg2
import pandas as pd
from config import aws
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 
from sklearn import metrics
import pickle

app = Flask(__name__) 

@app.route('/')
def posts():
    return render_template("Index.html")

@app.route('/win_predict',methods=['GET','POST'])
def game_win_predictor():
    return render_template("predictor.html")

@app.route('/getteams', methods=['GET','POST'])
def get_teams():
    games_df = read_data()
    if request.method == 'POST':
        # gets the text from the webpage
        home_team = request.form.get('home')
        away_team = request.form.get('away')
        print(home_team, away_team)

    # generate the table from your two teams
        trans_df = pd.DataFrame()

        # row list for df
        row = []
        
        #Last 10 games df for both teams
        last_10h = games_df[games_df["TEAM_ABBREVIATION"] == home_team][games_df["GAME_DATE"]< games_df["GAME_DATE"][i]].head(10)
        last_10a = games_df[games_df["TEAM_ABBREVIATION"] == away_team][games_df["GAME_DATE"]< games_df["GAME_DATE"][i]].head(10)
        
        win_rateH = 0
        win_rateA = 0
        
        needed_features = ["FGA", "FG_PCT", "FG3_PCT", "DREB", "REB", "AST"]
        
        for feature in needed_features:
            row.append(round((sum(last_10h[feature])/10),2))
            row.append(round((sum(last_10a[feature])/10),2))
        
        row.append(round((len(last_10h[last_10h["WL"]=="W"])/10),2))
        row.append(round((len(last_10a[last_10a["WL"]=="W"])/10),2))
        
        trans_df = trans_df.append(pd.DataFrame([row]), ignore_index=True)

        trans_df=trans_df.set_axis(["FGA_HOME","FGA_AWAY", "FG_PCT_HOME", "FG_PCT_AWAY", "FG3_PCT_HOME", "FG3_PCT_AWAY", 
                                "DREB_HOME", "DREB_AWAY", "REB_HOME", "REB_AWAY", "AST_HOME", "AST_AWAY", "WIN_RATE_HOME", "WIN_RATE_AWAY"], axis=1)
            

        

        #Creating input data
        X_df = trans_df

        # Create a StandardScaler instances
        scaler = StandardScaler()

        # Fit the StandardScaler
        X_scaler = scaler.fit(X_df)

        #Scale the input
        X_scaled = X_scaler.transform(X_df)

        # read in your model
        filename = 'finalized_RF_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        
        # pass in the data into the model
        prob = loaded_model.predict_proba(X_df)

        # result from model is 1
        
        if prob[0][0] >= 0.5:
            result = "Home team wins"
        else:
            result = "Away team wins"
       
        # print(f"This is python printing something from front-end - {status}")
        return render_template('predictor.html', winner=result+'!!!')
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

    col_names = ['GAME_ID', 'GAME_DATE', 'TEAM_away', 'TEAM_home', 'TEAM_ID_away',
       'TEAM_ID_home', 'WL_away', 'WL_home', 'FGM_away', 'FGM_home',
       'FGA_away', 'FGA_home', 'FG_PCT_away', 'FG_PCT_home', 'FG3_PCT_away',
       'FG3_PCT_home', 'FTM_away', 'FTM_home', 'FTA_away', 'FTA_home',
       'FT_PCT_away', 'FT_PCT_home', 'OREB_away', 'OREB_home', 'DREB_away',
       'DREB_home', 'REB_away', 'REB_home', 'AST_away', 'AST_home', 'STL_away',
       'STL_home', 'BLK_away', 'BLK_home', 'TOV_away', 'TOV_home', 'PF_away',
       'PF_home', 'PTS_away', 'PTS_home', 'WIN_home']


    df = pd.DataFrame(games, columns=col_names)
    # return games
    return df
    


@app.route('/analysis',methods=['GET','POST'])
def analysis():
    return render_template("Insights_Analytics1.html")

@app.route('/analysis2',methods=['GET','POST'])
def analysis2():
    return render_template("Insights_Analytics2.html")

@app.route('/analysis3',methods=['GET','POST'])
def analysis3():
    return render_template("Insights_Analytics3.html")

@app.route('/ml',methods=['GET','POST'])
def ml():
    return render_template("MachineLearning.html")

    
if __name__ == "__main__":
    app.run(debug=True)
