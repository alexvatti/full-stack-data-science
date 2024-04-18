import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

app=Flask(__name__)
pickled_model = pickle.load(open('house-price-prediction-model.pkl', 'rb'))


saved_image=None
@app.route('/')      # decorator
def home():
      return render_template('index.html',saved_image="static/House-Price.png")
    
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    MedInc = float(list(request.form.values())[0])
    print(MedInc)

    HouseAge = float(list(request.form.values())[1])
    print(HouseAge)

    AveBedrms = float(list(request.form.values())[2])
    print(AveBedrms)

    Population = float(list(request.form.values())[3])
    print(Population)

    AveOccup = float(list(request.form.values())[4])
    print(AveOccup)
   

    ans=pickled_model.predict([[MedInc,HouseAge,AveBedrms,Population,AveOccup]])

    return render_template('index.html',saved_image="static/House-Price.png", prediction_text='Predicted House Price is {} (units 100,000) '.format(round(ans[0],2)))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
