# 👗 Product Rating & Recommendation ML App

Enhancing fashion e-commerce with smart, personalized product recommendations using machine learning.

---

## 📌 Overview

With the rise of fashion e-commerce, customers are often overwhelmed by the sheer volume of choices.  
This project develops a **personalized recommendation ** to:

- Improve shopping experience  
- Increase engagement  
- Drive conversions through accurate and user-centric suggestions

---

## 🎯 Objectives

- 🤖 Build a recommendation engine using ML techniques  
- 📊 Analyze product features to determine impact on ratings  
- 👥 Segment users to explore spend behavior and preferences  
- 🛍️ Deliver **Top-N product recommendations per user**

---

## 📁 Dataset Description

The dataset includes customer-product interaction data:

| Feature Type     | Columns                                       |
|------------------|-----------------------------------------------|
| 🧮 Numerical      | User ID, Product ID, Price, Rating            |
| 🏷️ Categorical    | Product Name, Brand, Category, Color, Size     |

---

## 🧹 Data Preprocessing

- ✅ No missing values or outliers in numerical data  
- 📊 Confirmed multimodal distributions in numeric features  
- 🔍 Explored popular brands, sizes, colors using bar plots & counts

---

## 📊 Exploratory Data Analysis (EDA)

- 🔥 Correlation heatmaps — no strong feature-target correlations  
- 📦 Boxplots to explore price and rating distributions  
- 📈 Distribution plots to verify diversity in categorical values

---

## 📈 Modeling Approaches

### ✅ CatBoost Regressor (Final Model)
- Best performing model: **RMSE = 1.23**  
- Natively handles categorical features  
- Used for predicting product ratings for recommendations

### 🌲 Random Forest Regressor
- Identified key drivers: Product ID, Price  
- Helped understand feature importance

### ⚡ XGBoost Regressor
- Validated Random Forest results  
- Highlighted **Size M**, **Color Yellow**, and **Men’s Fashion**

### 📉 SVD (Collaborative Filtering)
- Matrix factorization model from `surprise` library  
- Achieved RMSE = **0.2666**  
- Combined with content-based methods for **hybrid recommendations**

---

## 🧠 User Segmentation

Segmented users based on average spend:

- 💸 High Spenders: Avg. spend > 70  
- 💳 Low Spenders: Avg. spend ≤ 70  

Compared average ratings across segments to reveal actionable insights for product targeting and promotions.

---

## 🛠 Tech Stack

| Category       | Tools / Libraries                              |
|----------------|--------------------------------------------------|
| Languages      | Python                                           |
| ML Libraries   | Pandas, NumPy, Scikit-learn, CatBoost, XGBoost   |
| Recommenders   | Surprise (SVD)                                   |
| Visualization  | Matplotlib, Seaborn                              |

---

## 🧪 Future Improvements

- 🕐 Add time-based features to detect seasonal demand  
- 🧠 Use time-decay to weight recent user interactions  
- 🌐 Integrate external data (ads, trends, campaign events)  
- 🤖 Explore **deep learning** (e.g., DeepFM, AutoRec)

---

## ✅ Conclusion

This project demonstrates an **end-to-end recommendation pipeline** including:

- 📊 Data analysis  
- 🤖 Model selection  
- 📈 Evaluation & visualization  
- 🔁 User segmentation  

## 🌐 Live Demo

👉 https://app-kvhehbbmkzeuwzd6vqkkpq.streamlit.app/

---

## 🙋‍♀️ Author

**Swati Sharma**  
🔗 [LinkedIn](https://www.linkedin.com/in/swati-sharma-17s50s01/)  
📂 [GitHub](https://github.com/swatinw)

---

📬 _Want to collaborate on NLP or AI projects? Let’s connect!_
