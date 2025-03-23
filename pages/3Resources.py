import streamlit as st
import pickle as p
import predict_depression as pdp

# # Custom Styling
# st.markdown("""
#     <style>
#         .stApp {background-color: black;}
#         .title {text-align: center; font-size: 28px; font-weight: bold; color: #3c6382;}
#         .card {background-color: black; padding: 20px; border-radius: 10px; 
#                box-shadow: 0px 0px 10px rgba(0,0,0,0.1); margin: 20px 0;}
#         .btn-container {text-align: center;}
#     </style>
# """, unsafe_allow_html=True)

# # Load Data
# with open('pickle.pkl', 'rb') as file:
#     loaded_data = p.load(file)

# # Display Title
# st.markdown('<p class="title">📊 Questionnaire Results</p>', unsafe_allow_html=True)

# # Display Loaded Data
# st.markdown('<div class="card">', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# # Navigation Button
# st.markdown('<div class="btn-container">', unsafe_allow_html=True)
# st.subheader("Results: ")
# if (pdp.predict_depression(loaded_data)):
#     st.write ("Our model suggests that your behaviors may indicate a potential concern. However, please remember that this is not a substitute for professional evaluation. Your well-being is most important, and we strongly encourage you to seek guidance from a qualified healthcare professional if you suspect that you are suffering from depression, anxiety, or mental health issues.")
# else: 
#     st.write ("Our model suggests that your behaviors don't indicate a potential concern. However, please remember that this is not a substitute for professional evaluation. Your well-being is most important, and we strongly encourage you to seek guidance from a qualified healthcare professional if you suspect that you are suffering from depression, anxiety, or mental health issues.")


# st.page_link("pages/2Questionnaire.py", label="✏️ Edit Answers", help="Modify your responses")
# st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h1 class="title"> Resources </h1>', unsafe_allow_html=True)
st.markdown('<p> Regardless of the results of the last page, there are many resources online that can help with your mental health.'
' While these resources are great, they are not a replacement for professional help. If you feel you need professional help, do not hesistate to seek it. </p>', unsafe_allow_html=True)

st.markdown('<ul>'
'<li> <a href = "https://uhs.tamu.edu/mental-health/index.html"> TAMU Mental Health website </a> </li>'
'<li> <a href = "https://www.nimh.nih.gov/health/find-help"> National Institute of Mental Health </a> </li>'
'<li> <a href = "https://www.nami.org/"> National Alliance on Mental Illness </a> </li>'
' </ul>', unsafe_allow_html=True )
st.markdown('<p> All the resources above are free to access but cannot replace professional help. <p>', unsafe_allow_html=True)
