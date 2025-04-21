import streamlit as st
import pandas as pd
import pickle

# Load your trained model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load product data
df = pd.read_csv("fashion_products.csv")

st.set_page_config(page_title="Fashion Recommender", layout="centered")
st.title("🛍️ AI Fashion Product Recommender")

# Sidebar - input section
user_id = st.sidebar.number_input("Enter your User ID:", min_value=int(df["User ID"].min()), max_value=int(df["User ID"].max()), step=1)
category = st.sidebar.selectbox("Choose a Category", sorted(df["Category"].dropna().unique()))

# Filter by category
filtered_df = df[df["Category"] == category].copy()

# Input features (MUST match model training order!)
X = filtered_df[["User ID", "Brand", "Price", "Color", "Size"]].copy()
X["User ID"] = user_id  # personalize for current user

# Predict ratings
filtered_df["Predicted Rating"] = model.predict(X)

# Show top 5 recommended items
top_items = filtered_df.sort_values(by="Predicted Rating", ascending=False).head(5)

st.subheader(f"🎯 Top Recommendations for Category: {category}")

for _, row in top_items.iterrows():
    st.markdown(f"### 🧥 {row['Product Name']} ({row['Brand']})")
    st.markdown(f"- **Color:** {row['Color']}")
    st.markdown(f"- **Size:** {row['Size']}")
    st.markdown(f"- **Price:** ${row['Price']}")
    st.markdown(f"- ⭐ **Predicted Rating:** {round(row['Predicted Rating'], 2)}")
    st.markdown("---")
