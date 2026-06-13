# Iris Flower Classification & Prediction System

## Overview

This project applies Machine Learning techniques to classify Iris flower species based on sepal and petal measurements. The project includes data preprocessing, exploratory data analysis (EDA), model comparison, performance evaluation, and deployment using Streamlit.

## Objectives

* Analyze the Iris dataset through exploratory data analysis.
* Perform data preprocessing and feature engineering.
* Train and compare multiple Machine Learning models.
* Evaluate model performance using classification metrics.
* Deploy the best-performing model as an interactive web application.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib

## Data Preprocessing

The following preprocessing steps were performed:

* Missing value analysis
* Duplicate record detection
* Outlier detection using the IQR method
* Feature scaling using StandardScaler
* Label encoding of target classes
* Train-test split for model evaluation

## Exploratory Data Analysis

EDA was conducted to understand the dataset and feature relationships through:

* Species distribution analysis
* Correlation heatmap
* Pair plots
* Feature distribution histograms
* Boxplots for outlier detection

## Machine Learning Models

The following classification algorithms were trained and evaluated:

* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Random Forest
* Decision Tree
* Logistic Regression

### Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| SVM                 | 96.67%   |
| KNN                 | 96.67%   |
| Random Forest       | 93.33%   |
| Decision Tree       | 93.33%   |
| Logistic Regression | 93.33%   |

SVM achieved the highest performance and was selected as the final deployment model.

## Model Evaluation

Performance was assessed using:

* Accuracy Score
* Confusion Matrix
* Classification Report
* Cross-Validation

## Streamlit Application

The trained model was deployed as an interactive Streamlit application where users can:

* Enter flower measurements
* Predict the Iris species in real time
* Explore a simple Machine Learning prediction workflow

## Project Structure

iris-flower-classification-app/

├── app.py

├── model.pkl

├── scaler.pkl

├── requirements.txt

├── Iris_Classification.ipynb

└── README.md

## Results

The project successfully classifies Iris flowers with an accuracy of 96.67% and demonstrates a complete Machine Learning workflow from data preprocessing and model development to deployment.



SASTRA Deemed University
