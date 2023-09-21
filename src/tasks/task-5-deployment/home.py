import streamlit as st

# Set the title and page icon
st.set_page_config(
    page_title="Omdena Berlin Chapter",
    page_icon=":chart_with_upwards_trend:",
)

# Title
st.title("Omdena Berlin Chapter")

# Header
st.header("Developing a Data-Driven Model for Waste Management Optimization")

# Button to open GitHub repository

    
if st.button("GitHub Repository"):
    website_url = "https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management"  # Replace with the URL you want to open
    webbrowser.open(website_url, new=2)
    

# Tabs for Dashboards
tabs = ["Dashboard 1", "Dashboard 2", "Dashboard 3"]
selected_tab = st.selectbox("Select a Dashboard", tabs)

if selected_tab == "Dashboard 1":
    # Insert code to display Dashboard 1 here
    st.write("Placeholder for Dashboard 1")

elif selected_tab == "Dashboard 2":
    # Insert code to display Dashboard 2 here
    st.write("Placeholder for Dashboard 2")

elif selected_tab == "Dashboard 3":
    # Insert code to display Dashboard 3 here
    st.write("Placeholder for Dashboard 3")
