from flask import Flask, request, url_for, render_template, redirect, abort, flash,jsonify
import psycopg2
import pandas as pd
from config import aws
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
# from imblearn.ensemble import BalancedRandomForestClassifier
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
    if request.method == 'POST':
        # gets the text from the webpage
        home_team = request.form.get('home')
        away_team = request.form.get('away')

        # generate the table from your two teams
        print(home_team, away_team)
        
        # Import data from postgresql
        conn = psycopg2.connect(
        database="NBA_ML",
        user="root",
        password=aws,
        host="root.cv2swqkze1kh.us-east-1.rds.amazonaws.com",
        port='5432'
        )

        games_df = pd.read_sql_query('select * from game_detail_new',con=conn)
        
        trans_df = pd.DataFrame()

        # row list for df
        row = []
        
        #Last 10 games df for both teams
        last_10h = games_df[games_df["team_abbreviation"] == home_team]
        last_10h.sort_values("game_date", ascending=False)
        #[games_df["game_date"]< games_df["game_date"]].head(10)
        last_10a = games_df[games_df["team_abbreviation"] == away_team]
        #[games_df["game_date"]< games_df["game_date"]].head(10)
        last_10a.sort_values("game_date", ascending=False)

        last_10h = last_10h.head(10)
        last_10a = last_10a.head(10)
        
        # win_rateH = 0
        # win_rateA = 0

        needed_features = ["fga", "fg_pct", "fg3_pct", "dreb", "reb", "ast"]

        for feature in needed_features:
            row.append(round((sum(last_10h[feature])/10),2))
            row.append(round((sum(last_10a[feature])/10),2))
        
        row.append(round((len(last_10h[last_10h["wl"]=="W"])/10),2))
        row.append(round((len(last_10a[last_10a["wl"]=="W"])/10),2))
        
        trans_df = trans_df.append(pd.DataFrame([row]), ignore_index=True)

        trans_df=trans_df.set_axis(["fga_home","fga_away", "fg_pct_home", "fg_pct_away", "fg3_pct_home", "fg3_pct_away", 
                                "dreb_home", "dreb_away", "reb_home", "reb_away", "ast_home", "ast_away", "win_rate_home", "win_rate_away"], axis=1)

         #Creating input data
        X_df = trans_df

        # Create a StandardScaler instances
        scaler = StandardScaler()
        # Fit the StandardScaler
        X_scaler = scaler.fit(X_df)

        #Scale the input
        X_scaled = X_scaler.transform(X_df)

        X_df.columns= X_df.columns.str.strip().str.upper()

        # read in your model
        filename = 'finalized_RF_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        
        # pass in the data into the model
        prob = loaded_model.predict_proba(X_df)
        prediction = loaded_model.predict(X_df)

        # result from model is 1
        print(f'prob:{prob}, prediction:{prediction}')

        print()
        
        if prediction[0] == 1:
            probability = prob[0][1]
            result = f"Home team wins ({home_team})"
        else:
            probability = prob[0][0]    
            result = f"Away team wins ({away_team})"

        probability = round(float(probability)*100,2)
       
        # print(f"This is python printing something from front-end - {status}")
        return render_template('predictor.html', home = home_team, away = away_team, winner=result, probability=' with '+str(probability)+' % !')
    else:
        return redirect(url_for("posts"))



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

