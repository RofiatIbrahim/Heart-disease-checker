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
    age : TYPE
        DESCRIPTION.
    sex : TYPE
        DESCRIPTION.
    cp : TYPE
        DESCRIPTION.
    trestbps : TYPE
        DESCRIPTION.
    chol : TYPE
        DESCRIPTION.
    fbs : TYPE
        DESCRIPTION.
    restecg : TYPE
        DESCRIPTION.
    thalach : TYPE
        DESCRIPTION.
    exang : TYPE
        DESCRIPTION.
    oldpeak : TYPE
        DESCRIPTION.
    slope : TYPE
        DESCRIPTION.
    ca : TYPE
        DESCRIPTION.
    thal : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    print(prediction)
    return prediction



def main():
    st.title('Heart Disease Check')
    html_temp = '''
    <div style ='background_color:pink;padding:10px'>
    <h2 style ='color:white;text-align:center;'>Streamlit Heart Disease Check ML App </h2>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html = True)
    age = st.text_input('age','Enter Here')
    sex = st.text_input('sex','Enter Here')
    cp = st.text_input('cp','Enter Here')  
    trestbps = st.text_input('trestbps','Enter Here')
    chol = st.text_input('chol','Enter Here')
    fbs = st.text_input('fbs','Enter Here')
    restecg = st.text_input('restecg','Enter Here')
    thalach = st.text_input('thalach','Enter Here')
    exang = st.text_input('exang','Enter Here')
    oldpeak = st.text_input('oldpeak','Enter Here')
    slope = st.text_input('slope','Enter Here')    
    ca = st.text_input('ca','Enter Here')
    thal = st.text_input('thal','Enter Here')
    result = ''
    if st.button('Predict'):
        result = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success('The output is {}'.format(result))
    
    
if __name__=='__main__':
    main() 
    
