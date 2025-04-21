import streamlit as st
import pandas as pd
import pickle
import os

# --- CONFIG ---
MODEL_PATH = "best_model_cat.pkl"
DATA_PATH = "fashion_products.csv"

# --- PAGE SETUP ---
st.set_page_config(page_title="Fashion Recommender", layout="centered")
st.title("🛍️ AI Fashion Product Recommender")

# --- LOAD MODEL ---
if not os.path.exists(MODEL_PATH):
    st.error(f"❌ `{MODEL_PATH}` not found. Please upload it to the app folder.")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# --- LOAD DATA ---
if not os.path.exists(DATA_PATH):
    st.error(f"❌ `{DATA_PATH}` not found. Please upload it to the app folder.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# --- SIDEBAR USER INPUT ---
user_id = st.sidebar.number_input("Enter User ID", min_value=int(df["User ID"].min()), max_value=int(df["User ID"].max()), step=1)
category = st.sidebar.selectbox("Choose Product Category", sorted(df["Category"].dropna().unique()))

# --- FILTER DATA ---
filtered_df = df[df["Category"] == category].copy()

if filtered_df.empty:
    st.warning("No products available in this category.")
    st.stop()

# --- PREPARE FEATURES ---
# Ensure same columns used in training are here:
features = ["User ID", "Brand", "Price", "Color", "Size"]
X = filtered_df[features].copy()
X["User ID"] = user_id  # personalize by user

# --- MAKE PREDICTIONS ---
filtered_df["Predicted Rating"] = model.predict(X)
top_recommendations = filtered_df.sort_values(by="Predicted Rating", ascending=False).head(5)

# --- DISPLAY RESULTS ---
st.subheader(f"🎯 Top Picks in {category}")

for _, row in top_recommendations.iterrows():
    st.markdown(f"### 👗 {row['Product Name']} ({row['Brand']})")
    st.markdown(f"- **Color:** {row['Color']}")
    st.markdown(f"- **Size:** {row['Size']}")
    st.markdown(f"- **Price:** ${row['Price']}")
    st.markdown(f"- ⭐ Predicted Rating: {round(row['Predicted Rating'], 2)}")
    st.markdown("---")
