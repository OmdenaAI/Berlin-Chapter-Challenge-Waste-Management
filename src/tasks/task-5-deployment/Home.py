import streamlit as st
import webbrowser
primaryColor="#395144"
backgroundColor="#f7f5ed"
secondaryBackgroundColor="#f0ebce"
textColor="#000000"
font="serif"

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {backgroundColor};
            padding: 0.5rem;
            border-radius: 10px;
        }}
        .section-header {{
            font-size: 35px;
            font-weight: bold;
            margin-bottom: 18px;
        }}
        .section-divider {{
            height: 5px;
            margin-bottom: 20px;
            background-color: {primaryColor};
        }}
        .section-content {{
            margin-bottom: 35px;
            background-color: {primaryColor};
        }}
        .section-table {{
            padding: 10px;
            border-radius: 10px;
        }}
        
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Omdena Berlin Chapter")
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.layout="wide"


# Homepage Layout

st.image("E:\\Berlin-Chapter-Challenge-Waste-Management\\src\\tasks\\task-5-deployment\\images\\Home.png", caption='', use_column_width=True)

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
st.header("Our Solution")
st.write(
    """

"""
)



