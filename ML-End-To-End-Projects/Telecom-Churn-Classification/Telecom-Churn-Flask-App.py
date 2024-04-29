import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, render_template

app=Flask(__name__)
pickled_model = joblib.load(open('telecom_churn_rf_model.joblib', 'rb'))

saved_image=None
@app.route('/')      # decorator
def home():
      return render_template('index.html',saved_image="static/churn.png")
    
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    gender = int(list(request.form.values())[0])
    age = float(list(request.form.values())[1])
    no_of_days_subscribed = float(list(request.form.values())[2])
    multi_screen = int(list(request.form.values())[3])
    mail_subscribed = int(list(request.form.values())[4])
    weekly_mins_watched = float(list(request.form.values())[5])
    minimum_daily_mins = float(list(request.form.values())[6])
    weekly_max_night_mins = float(list(request.form.values())[7])
    videos_watched = float(list(request.form.values())[8])
    customer_support_calls = float(list(request.form.values())[9])
    
    age = (age - 38)/10
    no_of_days_subscribed = (no_of_days_subscribed-99)/39
    weekly_mins_watched = (weekly_mins_watched-270)/80
    minimum_daily_mins = (minimum_daily_mins-10)/2
    weekly_max_night_mins = (weekly_max_night_mins-30)/9
    videos_watched = (videos_watched-4)/2
    customer_support_calls = (customer_support_calls-1.5)/1.3

    ans=pickled_model.predict([[gender, age, no_of_days_subscribed, multi_screen, mail_subscribed, weekly_mins_watched,
                            minimum_daily_mins,  weekly_max_night_mins, videos_watched,  customer_support_calls ]])
    if ans[0] == 1:
        predicted_label = "Churn"
    else:
        predicted_label = "Stay"
    return render_template('index.html',saved_image="static/churn.png", prediction_text='Telecom Churn Predicted is {} '.format(predicted_label))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
