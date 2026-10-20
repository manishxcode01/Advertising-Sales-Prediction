import streamlit as st
import numpy as np
import joblib
from pathlib import Path

# Configure the Streamlit page
st.set_page_config(
    page_title="Sales Predictor",
    page_icon="📊"
)

# Load the trained model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "sales_model.pkl"

model = joblib.load(MODEL_PATH)

weights = model["weights"]
bias = model["bias"]
scaler = model["scaler"]

# App title and description
st.title("📊 Advertising Sales Prediction")
st.write(
    "Enter your advertising budgets to estimate sales "
    "using a trained machine learning model."
)

# Advertising budget inputs
tv = st.number_input(
    "TV Advertising Budget",
    min_value=0.0,
    value=None,
    placeholder="Enter your TV advertising budget"
)

radio = st.number_input(
    "Radio Advertising Budget",
    min_value=0.0,
    value=None,
    placeholder="Enter your Radio advertising budget"
)

newspaper = st.number_input(
    "Newspaper Advertising Budget",
    min_value=0.0,
    value=None,
    placeholder="Enter your Newspaper advertising budget"
)

# Prediction
if st.button("Predict Sales"):
    if tv is None or radio is None or newspaper is None:
        st.warning("Please enter all three advertising budgets.")
    else:
        inputs = np.array([[tv, radio, newspaper]])
        scaled_inputs = scaler.transform(inputs)

        prediction = float(
            (scaled_inputs @ weights + bias).item()
        )

        st.success(f"Predicted Sales: {prediction:.2f}")
