import streamlit as st
import pandas as pd
import pickle as p
# st.markdown(
#     """<style>
#         section[data-testid="stSidebar"] {display: none;}
#     </style>""",
#     unsafe_allow_html=True
# )
st.header("Questionaire")
st.write("The following questions were picked as key factors in the mental wellbeing of college students. A machine learning algorithm was developed to "
"identify people who are at risk of experiencing depression based on this key information. Please fill these out as honestly as possible. These responses are not recorded"
" and are only taken as parameters to display whether you are at risk of depression.")
options = pd.DataFrame({
    'first column': [0,1,2,3,4,5]
})

financialoptions = pd.DataFrame({
    'first column': [1,2,3,4,5]
})

genderoptions = pd.DataFrame({
    'first column': ['Select', 'Female', 'Male']
})

lessoptions = pd.DataFrame({
    'first column':[0,2,5]
})
moreoptions = pd.DataFrame({
    'first column':[0,1,2,3,4,5,6,7,8,9,10,11,12]
})

joboptions = pd.DataFrame({
    'first column':[0,1,2,3,4]
})

sleepoptions = pd.DataFrame({
    'first column': ['Less than 5 hours', '5-6 hours', '6-7 hours', '7-8', 'More than 8 hours', 'Others']
})

dietoptions = pd.DataFrame({
    'first column':['Unhealthy' , 'Moderate', 'Healthy', 'Others']
})

yesno = pd.DataFrame({
    'first column' : ['No', 'Yes']
})

academicpressure = st.selectbox(
    "How much academic pressure do you feel", financialoptions['first column'], key="acpres",
    index = 0
)

workpressure = st.selectbox(
    "How much work pressure do you feel", financialoptions['first column'], key="wrkpres",
    index = 0
)

gpa = st.number_input("What is your GPA (4.0 Scale)?", key = "gpa", value = 0, min_value=0, max_value=4) 

studysatisfaction = st.selectbox(
    "How satisfied are you with your studies?", financialoptions['first column'], key="stdysat",
    index = 0
)

jobsatisfaction = st.selectbox(
    "How satisfied are you with your job?", financialoptions['first column'],
    index = 0
)

# sleep = st.selectbox(
#     "How many hours of sleep do you get?", sleepoptions['first column'],
#     index = 0
# )

# diet = st.selectbox(
#     "How would you describe your diet?", dietoptions['first column'],
#     index = 0
# )

suicidalthoughts = st.selectbox(
    "Have you ever had suicidal thoughts?", yesno['first column'],
    index = 0
)

workstudy = st.selectbox(
    "How many hours do you spend studying and/or working?", moreoptions['first column'],
    index = 0
)

financialstress = st.selectbox(
    "How much financial stress do you experience?", financialoptions['first column'],
    index = 0
)

# history = st.selectbox(
#     "Do you have a history of mental illness?", yesno['first column'],
#     index = 0
# )
age = 0
age = st.number_input("What is your age?", min_value=1, max_value=122, value = 1)

# gender = st.selectbox(
#     "Gender:" , genderoptions['first column'],
#     index = 0
# )

# Save results of query into a pickle
data = [age, academicpressure, workpressure, gpa, studysatisfaction, jobsatisfaction
        ,suicidalthoughts, workstudy, financialstress]
# for i in range(0,12):
#     if data[i] == False:
#         if type(data[i]) == int:
#             data[i]=1
#         else:
#             data[i].append("Female")
#     else:
#         continue


if (age != 1):
    with open('pickle.pkl', 'wb') as file:
        #empty_data = {}
        #p.dump(empty_data, file)
        p.dump(data,file)
    st.page_link("pages/3Prediction.py", label = "View Prediction")
    st.page_link("1Home.py", label = "To Home")

# else:
#     st.markdown(
#         # """<style>
#         #     section[data-testid="stSidebar"] {display: none;}
#         #     .stApp{
#         #         #background-image: linear-gradient(red,orange)
#         #     }
#         #     background{

#         #     }
            
#         # </style>""",
#         unsafe_allow_html=True
#     )
