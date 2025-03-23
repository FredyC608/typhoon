import streamlit as st
import pickle as p

# st.markdown(
#     """<style>
#         section[data-testid="stSidebar"] {display: none;}
#     </style>""",
#     unsafe_allow_html=True
# )

with open('pickle.pkl', 'rb') as file:
    loaded_data = p.load(file)

st.write(loaded_data)

# Do something with the loaded data

st.page_link("pages/2Questionnaire.py", label = "Return to edit answers")

