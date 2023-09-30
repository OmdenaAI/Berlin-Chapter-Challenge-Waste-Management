Implemented the Machine learning model using the Regression model and predicted the Waste by Year, State, and Waste.

Use case -1

How to test the model - Forecast Waste by Year and Waste


model = pickle.load(open('wm-model.pkl','rb'))

data = pd.read_csv('../data/Processed_DatasetsAmount-of Waste-Generated-By-State 32121-0003.csv')

states = data['States'].unique()

df_input = pd.DataFrame(states,columns=['States'])

df_input['Year'] = 2022

df_input['Types of Waste'] = 'Residual household and bulky wastes'

df_input

output = model.predict(df_input)

df_predicted = pd.DataFrame(output, columns=['Total Household Waste Generated (Tons)','Household Waste Generated per Inhabitant (kg)'])

df_final_bulk = pd.concat([df_input,df_predicted],axis=1)

df_final_bulk.index = df_final_bulk.index+1

df_final_bulk

Use case -2 

How to test the model - Forecast Waste by Year and State

uni_waste = data['Types of Waste'].unique()

df_input = pd.DataFrame(uni_waste,columns=['Types of Waste'])

df_input['Year'] = year

df_input['States'] = state

output = model.predict(df_input)

df_predicted = pd.DataFrame(output, columns=['Total Household Waste Generated (Tons)','Household Waste Generated per Inhabitant (kg)'])

df_final = pd.concat([df_input,df_predicted],axis=1)

df_final.index = df_final.index+1


df_final

