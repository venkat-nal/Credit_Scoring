import streamlit as st
import pickle
import numpy as np
import pandas as pd

#Load the model

pickle_in = open("Classifier.pkl",'rb')
Classifier = pickle.load(pickle_in)

def classify_customer(Recency,Frequency,Monetary):
    prediction=Classifier.predict([[Recency,Frequency,Monetary]])
    print(prediction)
    return prediction

def main():
    st.title("")
    html_temp = """
    <div style = "background-color: tomato;padding: 10px">
    <h2 style = "color:white;text-align:center;">Customer Credit Scoring ML app </h2>
    </div>
     """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Recency = st.text_input("Recency","")
    Frequency = st.text_input("Frequency","")
    Monetary = st.text_input("Monetary","")
    result = ''
    if st.button('Enter'):
        result = classify_customer(Recency,Frequency,Monetary)
        if result == 0:
            st.success(f"The Customer should be given 30 days ")
        elif result == 1:
            st.success(f"The Customer should be given 5 days")
        elif result == 2:
            st.success(f"The Customer should be given 20 days")
        elif result == 3:
            st.success(f"The Customer should be given 45 days")
        else:
            st.success(f"The Customer should be given 10 days")

            
if __name__ == '__main__':
    main()

