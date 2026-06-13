# 🌸 Iris Flower Classification & Prediction System

## Overview

The Iris Flower Classification & Prediction System is a Machine Learning web application that predicts the species of an Iris flower based on its physical measurements.

The application uses a trained Support Vector Machine (SVM) model and provides real-time predictions through an interactive Streamlit interface.

🔗 Live Demo: https://merline1306-nrs3j99v4wmgurikeypez2.streamlit.app/

---

## Problem Statement

Identifying Iris flower species manually can be time-consuming and prone to errors. This project automates the classification process using Machine Learning techniques.

The model predicts one of the following species:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

based on flower measurements provided by the user.

---

## Features

- Interactive web application built with Streamlit
- Real-time species prediction
- User-friendly interface
- Machine Learning-based classification
- End-to-end workflow from data preprocessing to deployment
- Cloud deployment using Streamlit Community Cloud

---

## Dataset

The project uses the famous Iris Dataset containing 150 flower samples with the following features:

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

Target Variable:

- Species

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Missing Value Analysis
5. Outlier Detection and Treatment
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Deployment using Streamlit

---

## Machine Learning Models Evaluated

The following classification algorithms were compared:

- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Random Forest Classifier
- Decision Tree Classifier
- Logistic Regression

### Model Performance

| Model | Accuracy |
|---------|---------|
| SVM | 96.67% |
| KNN | 96.67% |
| Random Forest | 93.33% |
| Decision Tree | 93.33% |
| Logistic Regression | 93.33% |

The SVM model was selected for deployment due to its superior performance.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- GitHub

---
## Conclusion
This project demonstrates an end-to-end Machine Learning workflow, from data preprocessing and model development to deployment as a live web application for real-time Iris flower species prediction.
