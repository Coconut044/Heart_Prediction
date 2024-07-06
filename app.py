import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd




load_model = pickle.load(open('C:/Users/Nitya/Downloads/mod_12.sav', 'rb'))



def heart_predict(input_data):
    input_data = (41,0,1,130,204,0,0,172,0,1.4,2,0,2)
    input_data_as_numpy_array= np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# Set feature
    input_data_reshaped = pd.DataFrame(input_data_reshaped, columns=X.columns)
    prediction = m.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0] == 0):
     return 'You dont have a Heart Disease'
    else:
     return 'You are at a risk of Heart Disease. Please Contact your doctor'
   
def main():
  st.title('Heart Disease Prediction System')

  #user input
  age,sex,trestbps,chol,fbs,restecg,cp,thalach,exang,oldpeak,slope,ca,thal

  age = st.text_input('Age: ')
  sex = st.text_input('Gender: ')
  trestbps = st.text_input('Resting Blood Pressure: ')
  chol = st.text_input('Cholestrol: ')
  fbs = st.text_input('Fasting Blood Sugar: ')
  restecg = st.text_input('ECG: ')

  cp = st.selectbox(
    "Chest Pain Type",
    ("No Chest Pain", ">0.90", "0.90-1.79", "1.80-2.10", "2.11-3.00"))
  thalach = st.text_input('Maximum Heart Rate Achieved: ')
  exang = st.text_input('Exercise Induced Angina: ')
  oldpeak = st.text_input('Old Peak: ')
  slope = st.text_input('ST/HR Slope: ')
  ca= st.text_input('Number of major vessels (0-3)')
  thal = st.selectbox(
    "Thalassemia",
    ("0", "1", "2", "3"))
  st.write("Hello")
  
  #code for prediction
  diagnosis = " "

  #create a submit button
  if st.button('Results'):
    diagnosis = heart_predict([  age,sex,trestbps,chol,fbs,restecg,cp,thalach,exang,oldpeak,slope,ca,thal])
  
  
  st.success(diagnosis)
