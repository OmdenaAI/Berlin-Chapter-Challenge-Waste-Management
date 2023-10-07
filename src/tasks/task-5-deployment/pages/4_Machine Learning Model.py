import streamlit as st
import webbrowser
import pandas as pd
import pickle

st.header("Harnessing ML for Greener Waste Solutions")
st.subheader("Predicting Waste Quantities by Year, State, and Waste Type")
# Introduction (initial paragraph)
intro_expander = st.expander("Learn More About the Model")

# Key Features
st.write(
    """
    **Key Features:**
    Our solution offers the following key features:
    - **Waste Forecasting by Year and Waste Type:** Users can make precise waste quantity predictions for specific years and waste types, aiding in long-term planning and resource allocation.
    - **Waste Forecasting by Year and State:** Our solution enables users to project waste quantities by year and state, facilitating regional waste management strategies and informed decision-making.
    """
)
with intro_expander:
    st.write(
        """
        In our solution, we have successfully developed a robust Machine Learning model for waste management forecasting, focusing on predicting waste quantities by year, state, and waste type. This achievement involved several key components:
        """
    )
    st.markdown("1. **Machine Learning Model:** We employed a powerful RandomForestRegressor model, harnessing its predictive capabilities to forecast waste quantities accurately.")
    st.markdown("2. **Data Pipeline:** To ensure data quality and model performance, we established a well-structured data pipeline. This pipeline encompasses essential steps such as data preprocessing, cross-validation, and hyperparameter tuning using Grid Search CV, enabling the model to learn from the data effectively.")
    st.markdown("3. **Model Serialization:** To facilitate seamless integration and deployment, we serialized the trained model into a file using the Pickle library, ensuring its accessibility for future predictions.")

#Creating tabs
tab1, tab2= st.tabs(['Prediction By Year','Prediction By State'])
with tab1:
    def header():
        st.header("WM Forecasting by Year")

    @st.cache_data
    def load_data():
        df = pd.read_csv('data/Processed_DatasetsAmount-of Waste-Generated-By-State 32121-0003.csv')
        return df

    def states():
        data = load_data()
        s_df = data['States'].unique()
        s_df.tolist()

    @st.cache_resource
    def load_model():
        model = pickle.load(open('models/wm-model.pkl','rb'))
        return model

    def show_search_query():
        query = st.number_input("Enter Year  ",min_value=2022,max_value=2026,value=2022,step=1, key="year")
        waste = st.selectbox("Select Waste Type",('Residual household and bulky wastes','Separately collected organic wastes',
                                                'Separately collected recyclables','Other wastes'))

        if query:
            df = predict_by_year_waste_type(query,waste)
            df['Year'] = df['Year'].astype(int)
            st.write(df)


    def predict_by_year_waste_type(year,waste):
        data = load_data()
        model = load_model()
        uni_states = data['States'].unique()
        df_input = pd.DataFrame(uni_states,columns=['States'])
        df_input['Year'] = year
        df_input['Types of Waste'] = waste
        output = model.predict(df_input)
        df_predicted = pd.DataFrame(output, columns=['Total Household Waste Generated (Tons)','Household Waste Generated per Inhabitant (kg)'])
        df_final = pd.concat([df_input,df_predicted],axis=1)
        df_final.index = df_final.index+1
        return df_final


    def main():
        header()
        show_search_query()
    main()

with tab2:
    def header():
        st.header("WM Forecasting by State")

    @st.cache_data
    def load_data():
        df = pd.read_csv('data/Processed_DatasetsAmount-of Waste-Generated-By-State 32121-0003.csv')
        return df
    
    @st.cache_data
    def states():
        data = load_data()
        s_df = data['States'].unique()
        return s_df.tolist()

    @st.cache_resource
    def load_model():
        model = pickle.load(open('models/wm-model.pkl','rb'))
        return model


    def show_search_state_query():
        query_year = st.number_input("Enter Year  ",min_value=2022,max_value=2026,value=2022,step=1, key="state")
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

# GitHub Repository Button
github_button = st.sidebar.button("View GitHub Repository", help="View GitHub Repository")
if github_button:
    webbrowser.open("https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management", new=2)
