{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import pickle\
\
# Load your trained model\
with open("best_model.pkl", "rb") as f:\
    model = pickle.load(f)\
\
# Load product data\
df = pd.read_csv("fashion_products.csv")\
\
st.set_page_config(page_title="Fashion Recommender", layout="centered")\
st.title("\uc0\u55357 \u57037 \u65039  AI Fashion Product Recommender")\
\
# Sidebar - input section\
user_id = st.sidebar.number_input("Enter your User ID:", min_value=int(df["User ID"].min()), max_value=int(df["User ID"].max()), step=1)\
category = st.sidebar.selectbox("Choose a Category", sorted(df["Category"].dropna().unique()))\
\
# Filter by category\
filtered_df = df[df["Category"] == category].copy()\
\
# Input features (MUST match model training order!)\
X = filtered_df[["User ID", "Brand", "Price", "Color", "Size"]].copy()\
X["User ID"] = user_id  # personalize for current user\
\
# Predict ratings\
filtered_df["Predicted Rating"] = model.predict(X)\
\
# Show top 5 recommended items\
top_items = filtered_df.sort_values(by="Predicted Rating", ascending=False).head(5)\
\
st.subheader(f"\uc0\u55356 \u57263  Top Recommendations for Category: \{category\}")\
\
for _, row in top_items.iterrows():\
    st.markdown(f"### \uc0\u55358 \u56805  \{row['Product Name']\} (\{row['Brand']\})")\
    st.markdown(f"- **Color:** \{row['Color']\}")\
    st.markdown(f"- **Size:** \{row['Size']\}")\
    st.markdown(f"- **Price:** $\{row['Price']\}")\
    st.markdown(f"- \uc0\u11088  **Predicted Rating:** \{round(row['Predicted Rating'], 2)\}")\
    st.markdown("---")\
}