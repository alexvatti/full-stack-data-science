# import the streamlit library
import streamlit as st
import joblib

# give a title to our app
st.title('Welcome to Telecom Churn Prediction Application ')



st.image('churn.png')

gender= st.number_input("Enter Gender Value(Female=0/Male=1)",min_value=0,max_value=1,value=1)
multi_screen  = st.number_input("Enter multi_screen  Value(no=0/yes=1)", min_value=0,max_value=1,value=0)
mail_subscribed = st.number_input("Enter mail_subscribed Value(no=0/yes=1)",min_value=0,max_value=1,value=0)

age = st.number_input("Enter age Value",min_value=18,max_value=82,value=37,step=10)
no_of_days_subscribed = st.number_input("Enter no_of_days_subscribed Value",min_value=1,max_value=243,value=99,step=1)
weekly_mins_watched = st.number_input("Enter weekly_mins_watched Value",min_value=0,max_value=526,value=269,step=1)
minimum_daily_mins = st.number_input("Enter minimum_daily_mins Value",min_value=0,max_value=20,value=10,step=1)

weekly_max_night_mins = st.number_input("Enter weekly_max_night_mins Value",min_value=42,max_value=175,value=100,step=1)
videos_watched = st.number_input("Enter videos_watched Value",min_value=0,max_value=19,value=4,step=1)
customer_support_calls=st.number_input("Enter customer_support_calls Value",min_value=0,max_value=9,value=1,step=1)

#mean,std
#(38 ,10),(99,39),(270,80) ,(10,2) , (30,9) , (4,2), (1.5,1.3)

age = (age - 38)/10
no_of_days_subscribed = (no_of_days_subscribed-99)/39
weekly_mins_watched = (weekly_mins_watched-270)/80
minimum_daily_mins = (minimum_daily_mins-10)/2
weekly_max_night_mins = (weekly_max_night_mins-30)/9
videos_watched = (videos_watched-4)/2
customer_support_calls = (customer_support_calls-1.5)/1.3

pickled_model = joblib.load(open('telecom_churn_rf_model.joblib', 'rb'))

ans=pickled_model.predict([[gender, age, no_of_days_subscribed, multi_screen, mail_subscribed, weekly_mins_watched,  minimum_daily_mins,  weekly_max_night_mins, videos_watched,  customer_support_calls ]])
if(st.button('Predict')):
    # print t
    if ans[0] == 1:
        predicted_label = "Churn"
    else:
        predicted_label = "Stay"

    st.header("Telecom Churn Predicted is {}".format(predicted_label))







