import streamlit as st
import pickle as p

# Custom CSS for styling
st.markdown("""
    <style>
        .title {text-align: center; font-size: 32px; font-weight: bold; color: #3c6382;}
        .info {color: #555; font-size: 16px; text-align: center;}
        .input-container {border-radius: 10px; padding: 15px; background-color: white; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">📝 Mental Well-being Questionnaire</p>', unsafe_allow_html=True)
st.markdown('<p class="info">Help us assess potential risk factors for depression. Your responses are not recorded.</p>', unsafe_allow_html=True)

# Options for dropdowns
options = [0,1,2,3,4,5]
financial_options = [1,2,3,4,5]
#gender_options = ['Select', 'Female', 'Male']
less_options = [0,2,5]
more_options = list(range(13))
job_options = [0,1,2,3,4]
#sleep_options = ['Less than 5 hours', '5-6 hours', '6-7 hours', '7-8', 'More than 8 hours', 'Others']
#diet_options = ['Unhealthy', 'Moderate', 'Healthy', 'Others']
yes_no = ['No', 'Yes']

# Input Fields
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)

    academic_pressure = st.selectbox("📚 Academic Pressure", options, index=0)
    work_pressure = st.selectbox("💼 Work Pressure", less_options, index=0)
    gpa = st.number_input("📊 GPA (0 - 4 scale)", min_value=0.0, max_value=4.0, step=0.1, value=0.0)
    study_satisfaction = st.selectbox("📖 Study Satisfaction", options, index=0)
    job_satisfaction = st.selectbox("👨‍💼 Job Satisfaction", job_options, index=0)
    #sleep = st.selectbox("😴 Hours of Sleep", sleep_options, index=0)
    #diet = st.selectbox("🥗 Diet Quality", diet_options, index=0)
    suicidal_thoughts = st.selectbox("⚠️ Ever had suicidal thoughts?", yes_no, index=0)
    work_study_hours = st.selectbox("⏳ Study/Work Hours", more_options, index=0)
    financial_stress = st.selectbox("💰 Financial Stress Level", financial_options, index=0)
    #mental_health_history = st.selectbox("🧠 Mental Health History", yes_no, index=0)
    age = st.number_input("🎂 Age", min_value=1, max_value=122, value=18)
    #gender = st.selectbox("⚧ Gender", gender_options, index=0)

    st.markdown('</div>', unsafe_allow_html=True)  # End input container

# Save responses if gender is selected
if age != '1':
    data = [age, academic_pressure, work_pressure, gpa, study_satisfaction, job_satisfaction, suicidal_thoughts, work_study_hours, financial_stress]
    with open('pickle.pkl', 'wb') as file:
        p.dump(data, file)

    st.success("✅ Data saved successfully!")

    # Navigation Buttons
    col1, col2 = st.columns(2)
    with col1:
        st.page_link("pages/3Prediction.py", label="🔮 View Prediction", help="Check your results")
    with col2:
        st.page_link("1Home.py", label="🏠 Home", help="Go back to home page")

else:
    st.warning("⚠️ Please select your age before proceeding.")
