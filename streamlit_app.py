import streamlit as st
import joblib
import numpy as np
import statsmodels.api as sm

# Load the trained model that is saved in model.pkl
model = joblib.load("model.pkl")


# Streamlit app
st.title("Fintech Real Estate Project 2024")
st.write("This app uses a machine learning model to make predictions about the price of an Airbnb given its features.")
st.write("Using the sidebar to the left, fill out the input fields, then click predict to view the price of the Airbnb per night.")

# User input form
st.sidebar.header("Input Features Of the Property")
feature_1 = st.sidebar.number_input("Number of Reviews", min_value=0.0, max_value=50.0, value=0.0)
feature_2 = st.sidebar.number_input("Number of Beds", min_value=0.0, max_value=10.0, value=0.0)
choice = st.sidebar.radio("Cleaning Fee?", ["No", "Yes"])
feature_3 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Apartment?", ["No", "Yes"])
feature_4 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Bed and Breakfast?", ["No", "Yes"])
feature_5 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Boutique Hotel ?", ["No", "Yes"])
feature_6 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Bungalow?", ["No", "Yes"])
feature_7 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Cabin?", ["No", "Yes"])
feature_8 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Camper/RV?", ["No", "Yes"])
feature_9 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Condo?", ["No", "Yes"])
feature_10  = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Dorm?", ["No", "Yes"])
feature_11  = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Guest Suite?", ["No", "Yes"])
feature_12 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Guesthouse?", ["No", "Yes"])
feature_13 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Hostel", ["No", "Yes"])
feature_14 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Inlaw?", ["No", "Yes"])
feature_15 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Loft?", ["No", "Yes"])
feature_16 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Other?", ["No", "Yes"])
feature_17  = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Timeshare?", ["No", "Yes"])
feature_18 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Townhouse?", ["No", "Yes"])
feature_19 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Villa?", ["No", "Yes"])
feature_20 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Couch?", ["No", "Yes"])
feature_21 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Futon?", ["No", "Yes"])
feature_22 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Pull out Sofa?", ["No", "Yes"])
feature_23 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Is it in Chicago?", ["No", "Yes"])
feature_24 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Is it in DC?", ["No", "Yes"])
feature_25= 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Is it in LA?", ["No", "Yes"])
feature_26 = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Is it in San Fransisco?", ["No", "Yes"])
feature_27  = 1 if choice == "Yes" else 0
choice = st.sidebar.radio("Is the property instantly bookable?", ["No", "Yes"])
feature_28= 1 if choice == "Yes" else 0
# Prepare data for prediction

input_data = np.array([[feature_1, feature_2, feature_3, feature_4,feature_5,feature_6,feature_7,feature_8, 
                        feature_9,feature_10,feature_11,feature_12,feature_13,feature_14, feature_15, feature_16, feature_17, 
                        feature_18, feature_19, feature_20, feature_21, feature_22, feature_23, feature_24, feature_25, 
                        feature_26, feature_27, feature_28]])




import math
if st.button("Predict"):
    prediction = model.predict(input_data)
    prediction = math.exp(prediction)
    roundedPrediction = round(prediction,2)
    st.success(f"The predicted value is: ${roundedPrediction}")

