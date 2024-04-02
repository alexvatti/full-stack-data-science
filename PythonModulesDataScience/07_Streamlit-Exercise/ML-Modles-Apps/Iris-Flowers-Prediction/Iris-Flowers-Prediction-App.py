# import the streamlit library
import streamlit as st
import pickle

# give a title to our app
st.title('Welcome to Iris Flowers Prediction Application ')

mean_flowers=[5.843333333333334, 3.0573333333333337, 3.7580000000000005, 1.1993333333333336]
std_flowers=[0.8280661279778629, 0.435866284936698, 1.7652982332594667, 0.7622376689603465]

st.image('flowers.png')
sl = st.number_input("Enter Iris flower sepal_length in cm",min_value=4.0,max_value=8.0,value=5.0,step=0.1)
sw = st.number_input("Enter Iris flower sepal_width in cm", min_value=2.0,max_value=4.5,value=3.0,step=0.1)
pl = st.number_input("Enter Iris flower petal_length in cm",min_value=1.0,max_value=7.0,value=4.0,step=0.1)
pw = st.number_input("Enter Iris flower petal_width in cm",min_value=0.1,max_value=2.5,value=1.0,step=0.1)


pickled_model = pickle.load(open('iris-model.pkl', 'rb'))
sl = (sl - mean_flowers[0])/ std_flowers[0]
sw = (sw - mean_flowers[1])/ std_flowers[1]
pl = (pl - mean_flowers[2])/ std_flowers[2]
pw = (pw - mean_flowers[3])/ std_flowers[3]
ans=pickled_model.predict([[sl,sw,pl,pw]])
ans = ans[0]
if ans==0:
    flower="setosa"
elif ans==1:
    flower="versicolor"
elif ans==2:
    flower="virginica"
else:
    flower="Invalid"
if(st.button('Predict')):
        # print t
    st.header("Predicted Iris Flower is {} ".format(flower))




