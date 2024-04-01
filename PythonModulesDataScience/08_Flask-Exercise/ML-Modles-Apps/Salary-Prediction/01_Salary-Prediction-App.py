import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

app=Flask(__name__)
pickled_model = pickle.load(open('salary-model.pkl', 'rb'))

yrs_min = 1
yrs_max = 11
salary_min = 37731
salary_max = 122391


@app.route('/')      # decorator
def home():
      return render_template('index.html')
    
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    yrs_exp = float(list(request.form.values())[0])
    print(yrs_exp)
   
    yrs = (yrs_exp - yrs_min)/ (yrs_max - yrs_min)
    prediction = pickled_model.predict([[yrs]])

    ans =prediction[0]
    print(ans)
    salary = ans * (salary_max - salary_min) + salary_min
    salary = round(salary,2)

    return render_template('index.html', prediction_text='Predicted Salary is {} per month'.format(salary))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
