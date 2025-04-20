
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Fashion Product Recommender", page_icon="🛍️")

st.title("👟 Fashion Product Recommendation System")
st.write("Upload a CSV of fashion products to get predicted ratings using your pre-trained XGBoost model.")

# Upload the CSV file
uploaded_file = st.file_uploader("📁 Upload your fashion_products.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Preview of Uploaded Data")
    st.write(df.head())

    try:
        # Drop identifier and target if present
        input_df = df.drop(columns=["Product ID", "Rating"], errors="ignore")

        # Load the model
        with open("model_xgBoost.pkl", "rb") as f:
            model = pickle.load(f)

        # Predict
        predictions = model.predict(input_df)
        df["Predicted Rating"] = predictions

        st.subheader("🔮 Predicted Ratings")
        st.write(df[["Product Name", "Predicted Rating"]])

        # Option to download
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", data=csv, file_name="predicted_ratings.csv", mime="text/csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
