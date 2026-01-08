import streamlit as st
import pickle
import numpy as np

# Load model and columns
model = pickle.load(open("house_price_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

def predict_price(location, sqft, bath, balcony, bhk):
    x = np.zeros(len(columns))

    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk

    if location in columns:
        loc_index = columns.get_loc(location)
        x[loc_index] = 1

    return model.predict([x])[0]

#UI
st.title("🏠 House Price Prediction")

location = st.selectbox("Location", sorted(columns[4:]))
sqft = st.number_input("Total Sqft", min_value=300)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balcony", min_value=0)
bhk = st.number_input("BHK", min_value=1)

if st.button("Predict Price"):
    price = predict_price(location, sqft, bath, balcony, bhk)
    st.success(f"Estimated Price: ₹ {round(price, 2)} Lakhs")