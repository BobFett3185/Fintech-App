import streamlit as st
import joblib
import numpy as np
import statsmodels.api as sm

# Load the trained model
model = joblib.load("model.pkl")

# Streamlit app
st.title("Fintech Project")
st.write("This app uses a machine learning model to make predictions about the projected price of an Airbnb given its features.")

# User input form
st.sidebar.header("Input Features")
feature_1 = st.sidebar.number_input("Feature 1", min_value=0.0, max_value=50.0, value=0.0)
feature_2 = st.sidebar.number_input("Feature 2", min_value=0.0, max_value=10.0, value=0.0)
feature_3 = st.sidebar.number_input("Feature 3", min_value=0.0, max_value=10.0, value=0.0)
feature_4 = st.sidebar.slider("Feature 4", 0.0, 10.0, 0.0)
feature_5 = st.sidebar.slider("Feature 5", 0.0, 10.0, 0.0)
feature_6 = st.sidebar.slider("Feature 6", 0.0, 10.0, 0.0)
feature_7 = st.sidebar.slider("Feature 7", 0.0, 10.0, 0.0)
feature_8 = st.sidebar.slider("Feature 8", 0.0, 10.0, 0.0)
feature_9 = st.sidebar.slider("Feature 9", 0.0, 10.0, 0.0)
feature_10 = st.sidebar.slider("Feature 10", 0.0, 10.0, 0.0)
feature_11 = st.sidebar.slider("Feature 11", 0.0, 10.0, 0.0)
feature_12 = st.sidebar.slider("Feature 12", 0.0, 10.0, 0.0)
feature_13 = st.sidebar.slider("Feature 13", 0.0, 10.0, 0.0)
feature_14 = st.sidebar.slider("Feature 14", 0.0, 10.0, 0.0)
feature_15 = st.sidebar.slider("Feature 15", 0.0, 10.0, 0.0)
feature_16 = st.sidebar.slider("Feature 16", 0.0, 10.0, 0.0)
feature_17 = st.sidebar.slider("Feature 17", 0.0, 10.0, 0.0)
feature_18 = st.sidebar.slider("Feature 18", 0.0, 10.0, 0.0)
feature_19 = st.sidebar.slider("Feature 19", 0.0, 10.0, 0.0)
feature_20 = st.sidebar.slider("Feature 20", 0.0, 10.0, 0.0)
feature_21 = st.sidebar.slider("Feature 21", 0.0, 10.0, 0.0)
feature_22 = st.sidebar.slider("Feature 22", 0.0, 10.0, 0.0)
feature_23 = st.sidebar.slider("Feature 23", 0.0, 10.0, 0.0)
feature_24 = st.sidebar.slider("Feature 24", 0.0, 10.0, 0.0)
feature_25 = st.sidebar.slider("Feature 25", 0.0, 10.0, 0.0)
feature_26 = st.sidebar.slider("Feature 26", 0.0, 10.0, 0.0)
feature_27 = st.sidebar.slider("Feature 27", 0.0, 10.0, 0.0)
feature_28 = st.sidebar.slider("Feature 28", 0.0, 10.0, 0.0)
# Prepare data for prediction

input_data = np.array([[feature_1, feature_2, feature_3, feature_4,feature_5,feature_6,feature_7,feature_8, 
                        feature_9,feature_10,feature_11,feature_12,feature_13,feature_14, feature_15, feature_16, feature_17, 
                        feature_18, feature_19, feature_20, feature_21, feature_22, feature_23, feature_24, feature_25, 
                        feature_26, feature_27, feature_28]])

# Make predictions
import math

if st.button("Predict"):
    prediction = model.predict(input_data)
    
    st.success(f"The predicted value is: {prediction[0]}")

