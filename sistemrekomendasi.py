# app.py

import streamlit as st
import pandas as pd
import pickle

# Load dataset
@st.cache_data
def load_data():
    df_food = pd.read_csv('data/food.csv')  # ganti sesuai file kamu
    df_rating = pd.read_csv('data/rating.csv')  # ganti sesuai file kamu
    return df_food, df_rating

# Load model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Aplikasi Utama
def main():
    st.title("🍽️ Sistem Rekomendasi Makanan")

    food_data, rating_data = load_data()
    model = load_model()

    user_id = st.number_input("Masukkan User ID Anda:", min_value=1, value=1)

    if st.button("Tampilkan Rekomendasi"):
        # Misal: sistem rekomendasi berbasis collaborative filtering
        recommended_foods = model.recommend(user_id)
        st.subheader("🍱 Rekomendasi Makanan untuk Anda:")
        for i, food in enumerate(recommended_foods):
            st.write(f"{i+1}. {food}")

if __name__ == '__main__':
    main()
