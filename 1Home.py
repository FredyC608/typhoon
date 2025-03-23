import streamlit as st

# Title
st.markdown(
    '<p style=" text-align:center; font-size:4em;">Mental Health on Campus</p>', 
    unsafe_allow_html=True
)

# Purpose Section
st.subheader("Purpose")
st.write(
    "Mental health is a crucial aspect of overall well-being, yet it is often overlooked—especially among college students. "
    "The transition to college brings new challenges, including academic pressure, social adjustments, and financial stress, "
    "all of which can impact mental health. The purpose of this initiative is to raise awareness, identify students who may be struggling, "
    "and provide resources for support. By participating in this questionnaire, students can reflect on their mental health and explore potential next steps "
    "toward seeking help if needed."
)

# Problem Section
st.subheader("Problem")
st.write(
    "Mental health is a significant issue for college students, as this is a major transitional period in their lives. "
    "Not only are students adapting to a new environment, but some may also struggle academically or financially in ways they haven't before. "
    "Studies show that between 27% and 41% of students report experiencing depression. "
    "This questionnaire along with the accompanying data visualizations aims to identify potential mental health concerns and provide helpful resources. "
)

# Emergency Resources
st.write(
    "**If you believe you need immediate mental health support, please reach out:**\n\n"
    "- **National Suicide Hotline:** Dial **988**\n"
    "- **Texas A&M Student Mental Health Assistance:** Call **(979) 458-4584**"
)

# Link to Questionnaire
st.page_link("pages/2Questionnaire.py", label="To Survey")

st.image(caption="Age correlation with depression", image="Graphs/Age_Depression.png")
st.image(caption="Academic Pressure correlation with depression", image="Graphs/APress_Depression.png")
st.image(caption="Diet correlation with depression", image = "Graphs/Diet_Depression.png")
st.image(caption = "Job Satisfaction correlation with depression", image = "Graphs/JobSat_Depression.png")
st.image(caption = "Sleep Duration correlation with depression", image = "Graphs/SleepDur_Depression.png")
st.image(caption = "Study Satisfaction correlation with depression", image = "Graphs/StudySat_Depression.png")
st.image(caption = "Work and Study Hours correlation with depression", image = "Graphs/WorkStudyHours_Depression.png")
st.image(caption = "Work Pressure correlation with depression", image = "Graphs/WPress_Depression.png")
