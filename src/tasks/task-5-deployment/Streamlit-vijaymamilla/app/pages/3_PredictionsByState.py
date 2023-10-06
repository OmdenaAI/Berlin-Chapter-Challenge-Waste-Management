import pickle
import streamlit as st
import pandas as pd

def header():
    st.header("WM Forecasting")

@st.cache_data
def load_data():
    df = pd.read_csv('artifactory/Processed_DatasetsAmount-of-Waste-Generated-By-State 32121-0003.csv')
    return df
@st.cache_data
def states():
    data = load_data()
    s_df = data['States'].unique()
    return s_df.tolist()

@st.cache_resource
def load_model():
    model = pickle.load(open('artifactory/wm-model.pkl','rb'))
    return model


def show_search_state_query():
    query_year = st.number_input("Enter Year  ",min_value=2022,max_value=2026,value=2022,step=1)
    state = st.selectbox("Select the State",(states()))

    if query_year:
        df = predict_by_year_state(query_year,state)
        df['Year'] = df['Year'].astype(int)
        st.write(df)
def predict_by_year_state(year,state):

    data = load_data()
    model = load_model()

    uni_waste = data['Types of Waste'].unique()
    df_input = pd.DataFrame(uni_waste,columns=['Types of Waste'])
    df_input['Year'] = year
    df_input['States'] = state
    output = model.predict(df_input)
    df_predicted = pd.DataFrame(output, columns=['Total Household Waste Generated (Tons)','Household Waste Generated per Inhabitant (kg)'])
    df_final = pd.concat([df_input,df_predicted],axis=1)
    df_final.index = df_final.index+1

    return df_final


def main():
    header()
    show_search_state_query()

main()