import streamlit as st
import webbrowser

st.title("Dashboards")

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


