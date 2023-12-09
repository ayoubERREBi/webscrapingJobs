# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:33:51 2023

@author: DeLL
"""

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


st.write('''
         # Welcome to iris predicting classes
         
         
         ''')
    
st.sidebar.header("inputs parametres")

def flower_species_input():
    return st.sidebar.selectbox('Select Flower Species', ('Setosa', 'Versicolor', 'Virginica'))

def user_input():
    sepal_length = st.sidebar.slider('sepal length',4.3,7.9,5.3)
    sepal_with = st.sidebar.slider('sepal with',1.3,7.9,2.3)
    pital_length = st.sidebar.slider('pital length',2.3,7.9,1.3)
    pital_with = st.sidebar.slider('pital with',0.3,7.9,3.3)
    data = {'sepal_length':sepal_length,
            'sepal_with':sepal_with,
            'pital_length':pital_length,
            'pital_with':pital_with
            }
    fleur_parameters = pd.DataFrame(data,index=[0])
    flower_species = flower_species_input()
    return fleur_parameters,flower_species

df,flower_species=user_input()

st.subheader('we want to find the class for this flor')
st.write(flower_species)
st.write(df)





















