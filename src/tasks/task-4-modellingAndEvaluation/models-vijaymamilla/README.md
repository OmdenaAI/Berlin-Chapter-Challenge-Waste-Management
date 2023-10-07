# Vijay Mamilla

Developed Maachine Learning model to forecast Waste Management by Year, State and Waste Type

We have implemented the following

- Developed Machine Learning model using RandomForestRegressor
- Included Data Pipeline with Preprocessing, Cross Validation and Grid Search CVsteps.
- Built Model file using pickle

## Features
- Forecast Waste by Year and Waste Type
- Forecast Waste by Year and State

## Installation
Requires [https://jupyter.org/] to run Jupyter notebooks and sklearn 1.30

## How to test the Forecast Waste by Year and Waster Type

```sh
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
	
```
## How to test the Forecast Waste by Year and State 

```sh
    uni_waste = data['Types of Waste'].unique()
	df_input = pd.DataFrame(uni_waste,columns=['Types of Waste'])
	df_input['Year'] = year
	df_input['States'] = state
	output = model.predict(df_input)
	df_predicted = pd.DataFrame(output, columns=['Total Household Waste Generated (Tons)','Household Waste Generated per Inhabitant (kg)'])
	df_final = pd.concat([df_input,df_predicted],axis=1)
	df_final.index = df_final.index+1
	df_final
```