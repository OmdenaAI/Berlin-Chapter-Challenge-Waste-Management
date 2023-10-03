import streamlit as st
import pandas as pd
import os

# Check if the CSV file exists, if not, create one
csv_file_path = 'feedback.csv'

if not os.path.isfile(csv_file_path):
    df = pd.DataFrame(columns=['Name', 'Email', 'Subject', 'Feedback'])
    df.to_csv(csv_file_path, index=False)

# Streamlit App
st.title("📨User Community and Feedback!")

# Input Form
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name:")
with col2:
    email = st.text_input("Email:")

subject = st.text_input("Subject:")
feedback = st.text_area("Feedback:")

if st.button("Submit"):
    if name and email and subject and feedback:
        # Load existing data from CSV
        df = pd.read_csv(csv_file_path)
        
        # Append new entry
        new_entry = {'Name': name, 'Email': email, 'Subject': subject, 'Feedback': feedback}
        df = df.append(new_entry, ignore_index=True)
        
        # Save updated data to CSV
        df.to_csv(csv_file_path, index=False)
        
        st.success("Thank you for the feedback!")
    else:
        st.warning("Please fill out all fields.")

