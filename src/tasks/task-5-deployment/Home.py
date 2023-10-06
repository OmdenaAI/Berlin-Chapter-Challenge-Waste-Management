import streamlit as st
import webbrowser


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
st.header("The Problem Statement")
st.write(
    """
1. Optimize waste composition analysis: Develop data-driven models to categorize waste types and identify dominant categories, enabling targeted recycling and reduction strategies.

2. Forecast future waste generation: Develop predictive models using time series analysis or machine learning algorithms to forecast future waste generation trends, aiding in capacity planning and resource allocation.

3. Geospatial Analysis: Use geographic data to create maps that display waste collection points, disposal sites, and processing facilities. This can help in route optimization and site selection.
"""
)

st.divider()

github_button = st.button("View GitHub Repository", help="View GitHub Repository")
if github_button:
    webbrowser.open("https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management", new=2)

