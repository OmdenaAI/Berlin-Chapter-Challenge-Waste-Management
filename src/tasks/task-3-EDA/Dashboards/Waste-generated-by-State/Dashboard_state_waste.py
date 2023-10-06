import streamlit as st
import pandas as pd
import pygwalker as  pyg


# Set page Configurations
st.set_page_config(
  page_title='PyGWalker Demo',
  page_icon=':snake:',
  layout='wide',
  initial_sidebar_state='expanded'
)

# Load data
@st.cache_data
def load_data(url):
  df = pd.read_csv(url,sep=',',encoding='latin1')
  return df

df = load_data('Amount-of Waste-Generated-By-State 32121-0003.csv',)

# Dispay PygWalker 
def load_config(file_path):
  with open(file_path,'r') as config_file:
    config_str = config_file.read()
  return config_str

config = load_config('config.json')
pyg.walk(df,env ='Streamlit',dark='dark',spec=config)