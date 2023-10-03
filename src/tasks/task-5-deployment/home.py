import streamlit as st
import webbrowser

# Set the title and page icon
st.set_page_config(
    page_title="Waste Management Optimization",
    page_icon=":recycle:",
    layout="wide"
)

# Define feature buttons with unique keys
feature_buttons = {
    "Homepage": st.sidebar.button("Homepage", key="homepage"),
    "Data Visualizations": st.sidebar.button("Dashboards", key="data_visualizations"),
    "Geospatial Data Analytics": st.sidebar.button("Geospatial Data", key="geospatial_data_analytics"),
    "Machine Learning Models": st.sidebar.button("Machine Learning Models", key="machine_learning_models"),
    "User Feedback/Community Engagement": st.sidebar.button("Community", key="user_feedback_community_engagement"),
    "Research Repository": st.sidebar.button("Repository", key="research_repository"),
    "Chatbot for Actionable Insights": st.sidebar.button("Chatbot", key="chatbot_for_actionable_insights"),
}

# Check if no feature button is selected or "Homepage" is selected
selected_feature = None
for feature, button in feature_buttons.items():
    if button:
        selected_feature = feature
        break

# Homepage Layout
if selected_feature is None or selected_feature == "Homepage":
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

# Problem Statements
if selected_feature and selected_feature != "Homepage":
    for feature, button in feature_buttons.items():
        if button and feature != selected_feature:
            st.title("")  # Empty title
            st.write("")  # Empty text
        elif button and feature == selected_feature:
            if feature == "Data Visualizations":
                st.header("Data Visualizations - Dashboards")
                st.write(
                    "Explore interactive dashboards created by the EDA team, along with inferences from the data. "
                    "Gain valuable insights into waste management trends and patterns."
                )

                # Dashboard 1
                if st.button("Open Dashboard 1"):
                    st.write("Placeholder for Dashboard 1")
                    # Insert code to display Dashboard 1 here

                # Dashboard 2
                if st.button("Open Dashboard 2"):
                    st.write("Placeholder for Dashboard 2")
                    # Insert code to display Dashboard 2 here

                # Dashboard 3
                if st.button("Open Dashboard 3"):
                    st.write("Placeholder for Dashboard 3")
                    # Insert code to display Dashboard 3 here

            # Add similar sections for the other project features
            elif feature == "Geospatial Data Analytics":
                st.header("Geospatial Data Analytics")
                st.write(
                    "Clear and concise route information is presented to users, ensuring they have a comprehensive understanding of selected paths. "
                    "Moreover, users can conveniently download visualizations in .png format, facilitating seamless sharing and integration into various reports and presentations."
                )
                # Add more content specific to this feature

            elif feature == "Machine Learning Models":
                st.header("Machine Learning Models")
                st.write(
                    "To show models created by the modeling team."
                )
                # Add more content specific to this feature

            elif feature == "User Feedback/Community Engagement":
                st.header("User Feedback/Community Engagement")
                st.write(
                    "Let users report issues, provide feedback about waste-related problems they encounter, and share initiatives, stories, and best practices."
                )
                # Add more content specific to this feature

            elif feature == "Research Repository":
                st.header("Research Repository")
                st.write(
                    "A repository of research, case studies, best practices, and educational resources on waste management."
                )
                # Add more content specific to this feature

            elif feature == "Chatbot for Actionable Insights":
                st.header("Chatbot for Actionable Insights")
                st.write(
                    "This chatbot is designed to understand user queries and provide valuable information and guidance, ensuring that users can make informed decisions and effectively address waste management challenges."
                )
                # Add more content specific to this feature

# GitHub Repository Button
github_button = st.sidebar.button("View GitHub Repository", help="View GitHub Repository")
if github_button:
    webbrowser.open("https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management", new=2)

# Sidebar note
st.sidebar.success("Select a page above.")
