# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 03:27:50 2020

@author: Rofiat
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

def welcome():
    return 'You are welcome'



def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    '''

   Parameters
    ----------
    age : int
          Age of the user
    sex : int
          Male or Female
    cp : int
        chest pain type  
    trestbps : int
        resting blood pressure
    chol : int
        serum cholesterol in mg/dl
    fbs : int
        fasting blood sugar > 120 mg/dl
    restecg : int
        resting electrocardiographic results
    thalach :int
        maximum heart rate achieved
    exang : int
        exercise induced anginahh
    oldpeak : int
        ST depression induced by exercise relative to stress
    slope : int
        The slope of the peak exercise segment
    ca : int
        number of major vessels coloured by flourosopy
    thal : int
        3-normal, 6-fixed defect, 7-reverable defect

    Returns
     Prediction 
    '''
    prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    print(prediction)
    return prediction



def main():
    st.title('Heart Disease Checker')
    html_temp = '''
    <div style ='background_color:pink;padding:10px'>
    <h2 style ='color:white;text-align:center;'>Streamlit Heart Disease Check ML App </h2>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html = True)
    age = st.text_input('Age','  ')
    sex = st.text_input('Sex|1-Male; 0-Female','  ')
    cp = st.text_input('chest pain type(cp)','  ')  
    trestbps = st.text_input('resting blood pressure(restecg)','  ')
    chol = st.text_input('serum cholesterol','  ')
    fbs = st.text_input('fasting blood sugar(fbs)|1-True; 0-False','  ')
    restecg = st.text_input('resting electrocardiographic results(restecg)','  ')
    thalach = st.text_input('max heart rate achieved(thalach)','  ')
    exang = st.text_input('exercise induced angina(exang)|1-yes; 0-no','   ')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest(oldpeak)','  ')
    slope = st.text_input('slope|1-upsloping, 2-flat, 3-downsloping','  ')    
    ca = st.text_input('number of major cells colored by florosopy(ca)','  ')
    thal = st.text_input('thal|3-normal, 6-fixed defect, 7-reversable defect','  ')
    result = ''
    if st.button('Predict'):
        result = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success('The output is {}'.format(result))
    
    
if __name__=='__main__':
    main() 
    
