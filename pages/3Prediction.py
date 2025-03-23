import streamlit as st
import pickle as p
import predict_depression as pdp

# st.markdown(
#     """<style>
#         section[data-testid="stSidebar"] {display: none;}
#     </style>""",
#     unsafe_allow_html=True
# )

with open('pickle.pkl', 'rb') as file:
    loaded_data = p.load(file)

# Do something with the loaded data

st.write(pdp.predict_depression(loaded_data))

st.page_link("pages/2Questionnaire.py", label = "Return to edit answers")

