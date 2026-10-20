
import streamlit as st
import numpy as np
import joblib

# Load the trained model
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "sales_model.pkl"

model = joblib.load(MODEL_PATH)

weights = model["weights"]
bias = model["bias"]
scaler = model["scaler"]

st.set_page_config(page_title="Sales Predictor", page_icon="📊")

st.title("📊 Advertising Sales Prediction")
st.write(
    "Enter your advertising budgets to estimate sales "
    "using a trained machine learning model."
)

tv = st.number_input("TV Advertising Budget", min_value=0.0, value=150.0)
radio = st.number_input("Radio Advertising Budget", min_value=0.0, value=30.0)
newspaper = st.number_input(
    "Newspaper Advertising Budget", min_value=0.0, value=20.0
)

if st.button("Predict Sales"):
    inputs = np.array([[tv, radio, newspaper]])
    scaled_inputs = scaler.transform(inputs)
    prediction = float((scaled_inputs @ weights + bias).item())

    st.success(f"Predicted Sales: {prediction:.2f}")
    st.caption("This is a model estimate, not a guarantee of actual sales.")
