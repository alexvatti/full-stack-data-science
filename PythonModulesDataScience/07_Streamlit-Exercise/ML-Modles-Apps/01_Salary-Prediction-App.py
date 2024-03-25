# import the streamlit library
import streamlit as st
import pickle

# give a title to our app
st.title('Welcome to Salary Prediction Application')

yrs_min = 1
yrs_max = 11
salary_min = 37731
salary_max = 122391
# TAKE yr_exp input in yrs
st.image('salary-image.jpg', caption='salary')
yrs_exp = st.number_input("Enter your Expereince (in Years)(Min-1 , Max-11)")

if (yrs_exp >= 1) or (yrs_exp<=11):
    pickled_model = pickle.load(open('salary-model.pkl', 'rb'))
    yrs = (yrs_exp - yrs_min)/ (yrs_max - yrs_min)
    ans=pickled_model.predict([[yrs]])
    salary = ans * (salary_max - salary_min) + salary_min
    if(st.button('Predict')):
        # print t
        st.text("Salary is {}.".format(salary[0]))
else:
    st.text("Enter valid Input of Exp in Yrs")


