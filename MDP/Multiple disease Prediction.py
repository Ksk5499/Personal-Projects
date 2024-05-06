# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:39:04 2024

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model=pickle.load(open("D:/Data Analytics/Interview Prep/Project Folders/Machine Learning Project/Multiple disease Prediction/trained_model.sav","rb"))
heart_disease_model=pickle.load(open("D:/Data Analytics/Interview Prep/Project Folders/Machine Learning Project/Multiple disease Prediction/trained_model2.sav","rb"))
parkinsons_model=pickle.load(open("D:/Data Analytics/Interview Prep/Project Folders/Machine Learning Project/Multiple disease Prediction/trained_model3.sav","rb"))

#side bar for navigate

with st.sidebar:
    selected=option_menu("Multiple Disease Prediction System",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Disease Prediction"],icons=["droplet-fill","heart-pulse","person-standing"],default_index=0)
    
    
# Diabetes Prediction Page
if (selected=="Diabetes Prediction"):
    #Page title
    st.title("Diabetes Prediction using ML")
    
    
    #getting the input data for users
    #columns for input data
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level in blood")
    with col3:
        BloodPressure=st.text_input("BP ")
    with col1:
        SkinThickness=st.text_input("Skin Thickness")
        
    with col2:
        Insulin=st.text_input("Insulin")
        
    with col3:
        BMI=st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age=st.text_input("Age")
    
    
    #code for Prediction
    diab_diagnosis=""
    
    #creating a button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ]])
        if (diab_prediction[0]==1):
            diab_diagnosis="The Person is Diabetic"
        else:
            diab_diagnosis="The Person is not Diabetic"
    st.success(diab_diagnosis)
if( selected=="Heart Disease Prediction"):
    st.title("Heart Disease Prediction using ML")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input("Age")
    with col2:
        sex=st.text_input("Gender")
    with col3:
        cp=st.text_input("Types of Chest pain")
    with col1:
        trestbps=st.text_input("Resting Blood Pressure")
        
    with col2:
        chol=st.text_input("Serum Cholestoral in mg/dl")
        
    with col3:
        fbs	=st.text_input("Fasting Blood Sugar")
    with col1:
        restecg	=st.text_input("Resting Electrocardiographic Results")
    with col2:
        thalach=st.text_input("Maximum heart rate achieved")
    with col1:
        exang=st.text_input("Exercise Induced Angina")
    with col2:
        oldpeak=st.text_input("Oldpeak")
    with col3:
        slope=st.text_input("The slope of the peak exercise ")
    with col1:
        ca	=st.text_input("number of major vessels (0-3) colored by flourosopy")
          
    with col2:
        thal=st.text_input("Thal")
    
    
    #code for Prediction
    heart_diagnosis=""
    
    #creating a button for prediction
    if st.button("Heart Disease Test Result"):
        heart_disease_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_disease_prediction[0]==1):
            heart_diagnosis="The Person has Heart Disease"
        else:
            heart_diagnosis="The Person does not has Heart Disease"
    st.success(heart_diagnosis)
    
if( selected=="Parkinsons Disease Prediction"):
    st.title("Parkinsons  Disease Prediction using ML")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        MDVPFo=st.text_input("Average vocal fundamental frequency")
    with col2:
        MDVPFhi	=st.text_input("Maximum vocal fundamental frequency")
    with col3:
        MDVPFlo	=st.text_input("Minimum vocal fundamental frequency")
    with col1:
        MDVPJitter=st.text_input("MDVPJitter")
        
    with col2:
        MDVPJitterABS=st.text_input("MDVPJitterABS")
        
    with col3:
        MDVPRAP	=st.text_input("MDVPRAP")
    with col1:
        MDVPPPQ=st.text_input("MDVPPPQ")
    with col2:
        MDVPShimmerDB=st.text_input("MDVPShimmerDB")
    with col1:
        ShimmerAPQ3=st.text_input("ShimmerAPQ3")
    with col2:
        ShimmerAPQ5=st.text_input("ShimmerAPQ5")
    with col3:
        MDVPAPQ =st.text_input("MDVPAPQ")
    with col1:
        ShimmerDDA=st.text_input("ShimmerDDA")
          
    with col2:
        NHR =st.text_input("NHR")
    with col3:
        HNR	=st.text_input("HNR")
    with col1:
        RPDE=st.text_input("RPDE( nonlinear dynamical complexity measure1)")
    with col2:
        DFA=st.text_input(" Signal fractal scaling exponent")
    with col3:
        spread1=st.text_input("spread1")
    with col1:
        spread2=st.text_input("spread2")
    with col2:
        D2=st.text_input("D2(nonlinear dynamical complexity measure2)")
    with col3:
        PPE=st.text_input("PPE")
    
       
    
    
    #code for Prediction
    Parkinsons_diagnosis=""
    
    #creating a button for prediction
    if st.button("Parkinsons Disease Result"):
        parkinsons_disease_prediction=parkinsons_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (parkinsons_disease_prediction[0]==1):
            Parkinsons_diagnosis="The Person has Parkinsons Disease"
        else:
            Parkinsons_diagnosis="The Person does not has Parkinsons Disease"
    st.success(Parkinsons_diagnosis)
    