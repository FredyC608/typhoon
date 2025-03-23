import streamlit as st
import pickle as p
import predict_depression as pdp

# Custom Styling
st.markdown("""
    <style>
        .stApp {background-color: black;}
        .title {text-align: center; font-size: 28px; font-weight: bold; color: #3c6382;}
        .card {background-color: black; padding: 20px; border-radius: 10px; 
               box-shadow: 0px 0px 10px rgba(0,0,0,0.1); margin: 20px 0;}
        .btn-container {text-align: center;}
    </style>
""", unsafe_allow_html=True)

# Load Data
with open('pickle.pkl', 'rb') as file:
    loaded_data = p.load(file)
    print (type(loaded_data))

# Display Title
st.markdown('<p class="title">📊 Questionnaire Results</p>', unsafe_allow_html=True)

# Display Loaded Data
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Navigation Button
st.markdown('<div class="btn-container">', unsafe_allow_html=True)
st.write(pdp.predict_depression(loaded_data))

st.page_link("pages/2Questionnaire.py", label="✏️ Edit Answers", help="Modify your responses")
st.markdown('</div>', unsafe_allow_html=True)
