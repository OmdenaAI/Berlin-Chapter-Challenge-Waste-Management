import streamlit as st
import webbrowser

st.header("This is Dashboard menu.")

st.write(
        "Explore interactive dashboards created by the EDA team, along with inferences from the data. "
        "Gain valuable insights into waste management trends and patterns."
        )

#Creating tabs
tab1, tab2, tab3= st.tabs(['Dashboard 1','Dashboard 2','Dashboard 3'])

with tab1:
    st.header("Dashboard 1")
    #Add more charts here.

with tab2:
    st.header("Dashboard 2")
    #Add more charts here.

with tab3:
    st.header("Dashboard 3")
    #Add more charts here.


# GitHub Repository Button
github_button = st.sidebar.button("View GitHub Repository", help="View GitHub Repository")
if github_button:
    webbrowser.open("https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management", new=2)
