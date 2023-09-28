import streamlit as st

st.set_page_config(
    page_title="Proactive Financial Planning for Lung Cancer Patients through Machine Learning-based Cost Prediction",
    page_icon="👋",
)

st.title("Home Page")
st.image("app/artifactory/Home.png", caption='', use_column_width=True)

st.header("The Problem")
st.write("""The local problem we are trying to solve is the suboptimal waste management practices and the lack of data-driven decision-making in our community. We aim to tackle issues such as inefficient waste treatment, limited recycling rates, and environmental impact caused by improper waste disposal. By harnessing the potential of data science, we can identify opportunities for improvement, optimize waste treatment methods, and ultimately enhance the sustainability of our local waste management system.""")

st.header("Want to know more?")
st.markdown("* [https://omdena.com/chapter-challenges/data-driven-waste-management-optimization/)")

st.sidebar.success("Select a page above.")
