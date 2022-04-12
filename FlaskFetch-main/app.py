from flask import Flask, request, url_for, render_template, redirect, abort, flash, jsonify
# from models import MyTweets, RedditPost
# from mongoengine import connect
# from datetime import datetime

# from twitter import *
# # reddit connection
# import praw

app = Flask(__name__)   # create our flask app



@app.route('/')
def posts():
    # tweets = [{'a': 1, 'b': 2}]
    # reddit_posts = [{'a': 1, 'b': 2}]
    return render_template("index.html")

@app.route('/twitterpost', methods=['GET','POST'])
def post_to_twitter():

    

    if request.method == 'POST':
        # gets the text from the webpage
        status = request.form.get('team1')
        # generate the table from your two teams

        # read in your model
        # Implementing Logistic Regression
        from imblearn.over_sampling import RandomOverSampler
        from collections import Counter
        ros = RandomOverSampler(random_state=1)
        X_resampled, y_resampled = ros.fit_resample(X_train_scaled, y_train)
        Counter(y_resampled)

        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression(solver='lbfgs', random_state=1)
        model.fit(X_resampled, y_resampled)

        # pass in the data into the model
        from sklearn.metrics import balanced_accuracy_score
        balanced_accuracy_score(y_test, y_pred)
        print(balanced_accuracy_score)
        
        # result from model is 1
        res = 1
        if res == 1:
            result = "home team wins"
        else:
            result = "away team wins"
        # send the data back to front end
        
        print(f"This is python printing something from front-end - {status}")
        return render_template('index.html', winner=result)
    else:
        return redirect(url_for("posts"))


@app.route('/forjs')
def chart_stay():
    res = [{"x_vals":"bread", "y_vals": 3},
           {"x_vals":"fish", "y_vals": 1},
           {"x_vals":"pasta", "y_vals": 5},
           {"x_vals":"water", "y_vals": 8},
           {"x_vals":"chicken", "y_vals": 3}]
    return jsonify(res)



if __name__ == "__main__":
    app.run(debug=True)