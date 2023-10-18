
# Waste Management Model

In this project, we harness the power of data science and machine learning algorithm to predict various aspects of waste management. Waste management is a critical concern in our modern world, as the amount of waste generated continues to grow. To address this issue efficiently and sustainably, predictive modeling plays a vital role. This predictive model aims to revolutionize waste management by leveraging data-driven insights to predict future waste.


## Problem Statement
Forecast future waste generation: Develop predictive models using time series analysis or machine learning algorithms to forecast future waste generation trends, aiding in capacity planning and resource allocation.


![App Screenshot](https://omdena.com/wp-content/uploads/2023/07/Data-Driven-Waste-Management-Optimization.jpg)


##  Dataset
Collected And Cleaned Dataset: 
[Processed_DatasetsAmount-of Waste-Generated-By-State 32121-0003](https://github.com/OmdenaAI/Berlin-Chapter-Challenge-Waste-Management/blob/main/src/tasks/task-4-modelling%26evaluation/Model_Akash/Processed_DatasetsAmount-of%20Waste-Generated-By-State%2032121-0003.csv)


## Techniques:
* Random Forest
* Linear Regression

## Conclusion
Model Performance: Two models were trained on the data – the Linear Regression Model and the Random Forest Regression Model. Their performance scores were as follows:

   - Regression Model Score: 79 %
   - Random Forest Model Score: 99 %
Cross-Validation: The Random Forest Model underwent cross-validation, assessing its consistency across different data subsets. Average Cross-Validation Score is 0.987. This underscores the model's robustness and its capacity to generalize effectively to new data.

Fine Tuning: To enhance the Random Forest Model's performance, a grid search was conducted to fine-tune its hyperparameters. This optimization process, guided by negative mean squared error, aims to enhance the model's accuracy and predictive power.

The Random Forest Regression Model is a suitable choice for predicting the output, based on the provided features. It has demonstrated excellent performance, generalization capabilities and potential for further improvement through hyperparameter tuning.

