# import the streamlit library
import streamlit as st
import pickle

# give a title to our app
st.title('Welcome to House Price Prediction Application ')



st.image('House-Price.png')
MedInc= st.number_input("Enter MedInc Value",min_value=0.0,max_value=15.0,value=3.5,step=0.1)
HouseAge = st.number_input("Enter HouseAge Value", min_value=1.0,max_value=52.0,value=29.0,step=0.1)
AveBedrms = st.number_input("Enter AveBedrms Value",min_value=0.0,max_value=34.0,value=1.0,step=0.1)
Population = st.number_input("Enter Population Value",min_value=3,max_value=35682,value=1166,step=10)
AveOccup = st.number_input("Enter AveOccup Value",min_value=0.0,max_value=1243.0,value=2.8,step=0.1)


pickled_model = pickle.load(open('house-price-prediction-model.pkl', 'rb'))

ans=pickled_model.predict([[MedInc,HouseAge,AveBedrms,Population,AveOccup]])
if(st.button('Predict')):
    # print t
    st.header("Predicted House Price is {} (units 1,00,000)".format(round(ans[0],2)))






