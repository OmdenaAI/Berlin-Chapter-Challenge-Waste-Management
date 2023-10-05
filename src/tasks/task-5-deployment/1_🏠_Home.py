import streamlit as st
import webbrowser
# from feedback import display_feedback

# Set the title and page icon
st.set_page_config(
    page_title="Waste Management Optimization",
    page_icon=":recycle:",
    layout="wide"
)

# Homepage Layout
st.title("Omdena Berlin Chapter")
st.image("images/Home.png", caption='', use_column_width=True)

st.divider()
st.header("The Problem")
st.write(
    """The local problem we are trying to solve is the suboptimal waste management practices and the lack of data-driven decision-making in our community. We aim to tackle issues such as inefficient waste treatment, limited recycling rates, and environmental impact caused by improper waste disposal. By harnessing the potential of data science, we can identify opportunities for improvement, optimize waste treatment methods, and ultimately enhance the sustainability of our local waste management system."""
)

st.divider()
st.header("Want to know more?")
st.markdown("* [https://omdena.com/chapter-challenges/data-driven-waste-management-optimization/)")


# GitHub Repository Button
github_button = st.sidebar.button("View GitHub Repository", help="View GitHub Repository")
if github_button:
    webbrowser.open("https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management", new=2)

