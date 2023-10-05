import streamlit as st
import webbrowser

st.header("This is Geospatial menu.")
st.write(
                    "Clear and concise route information is presented to users, ensuring they have a comprehensive understanding of selected paths. "
                    "Moreover, users can conveniently download visualizations in .png format, facilitating seamless sharing and integration into various reports and presentations."
                )


# GitHub Repository Button
github_button = st.sidebar.button("View GitHub Repository", help="View GitHub Repository")
if github_button:
    webbrowser.open("https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management", new=2)
