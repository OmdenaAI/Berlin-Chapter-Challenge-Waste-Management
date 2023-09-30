# Hazardous Waste Classification Model

## Overview

This repository contains a machine learning model for classifying hazardous waste into distinct categories based on their characteristics. The model is designed to assist in efficient waste management and regulatory compliance.

## Contents

- `Data`: This directory contains the dataset used for training and testing the model.
- `classification_model.pkl`: Serialized version of the trained Random Forest Classifier model.
- `Waste Classification.ipynb`: Notebook used to train and tune the models.

## Getting Started

1. **Environment Setup**:

    - Ensure you have Python 3.x installed.
    - Install the necessary dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

2. **Training the Model**:

    - Run the `Waste Classification.ipynb` script to train and tune the Random Forest Classifier. The best model will be serialized as `classification_model.pkl`.

    ```bash
    python train_model.py
    ```


## Additional Information

- The dataset used for training and testing can be found in the `Data` directory. It consists of waste characteristics and corresponding waste categories.
- The classification model is a Random Forest Classifier, hyperparameter tuned using GridSearchCV.
- Additional models like Decision Tree Classifier and XGBoost Classifier were also explored and evaluated.
- The project is structured with modularity in mind, making it easy to extend or incorporate different models in the future.

## Contributors

- Abhinash (GitHub: (https://github.com/abhinash-bhagat))
