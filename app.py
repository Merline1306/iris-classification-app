import streamlit as st
import joblib
import numpy as np

# Load pipeline model
model = joblib.load("iris_pipeline.pkl")

species_names = {
    0: "🌱 Iris Setosa",
    1: "🌿 Iris Versicolor",
    2: "🌸 Iris Virginica"
}

st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸"
)

st.title("🌸 Iris Flower Classification App")

st.markdown(
"""
Predict the species of an Iris flower using Machine Learning.
"""
)

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=4.0,
        max_value=8.0,
        value=5.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=2.0,
        max_value=5.0,
        value=3.5
    )

with col2:
    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=1.0,
        max_value=7.0,
        value=1.4
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.1,
        max_value=3.0,
        value=0.2
    )

if st.button("Predict Species"):

    sample = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediction = model.predict(sample)[0]

    st.success(
        f"Prediction: {species_names[prediction]}"
    )
