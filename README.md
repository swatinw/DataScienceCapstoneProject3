# DataScienceCapstoneProject3

📌 Overview

With the rise of fashion e-commerce, customers are often overwhelmed by the sheer volume of choices. This project develops a personalized recommendation system to improve the shopping experience, increase engagement, and drive sales by delivering accurate and user-centric product suggestions.

🎯 Objectives

Build a recommendation engine using various machine learning approaches.
Analyze product attributes to assess their influence on customer ratings.
Segment customers to better understand spending behavior and rating patterns.
Deliver Top-N product recommendations per user.
📁 Dataset Description

The dataset contains user interactions with fashion products and includes:

Numerical Features: User ID, Product ID, Price, Rating
Categorical Features: Product Name, Brand, Category, Color, Size
🧹 Data Preprocessing

✅ No missing values or outliers found in numeric data.
📊 Visualized feature distributions; confirmed multi-modal nature of numerical data.
🔍 Explored categorical data to reveal popular brands, categories, sizes, and colors.
📊 Exploratory Data Analysis

Created a correlation heatmap — no strong correlations found between features and the target (Rating).
Boxplots and distribution plots used to validate data quality and diversity.
📈 Modeling Approaches

1. Random Forest Regression
Identified key features: Product ID, Price, and certain User IDs
Useful for determining feature importance
2. XGBoost Regression
Validated Random Forest results
Highlighted Size M, Color Yellow, and Men’s Fashion as important
3. CatBoost Regression ✅ Final Model
Chosen for best performance: RMSE = 1.23
Handles categorical features efficiently
Used for generating Top-N product recommendations based on predicted ratings
4. SVD (Collaborative Filtering)
Built a user-item matrix for predicting ratings
Achieved excellent accuracy: RMSE = 0.2666
Combined with content-based features for hybrid recommendations
🧠 User Segmentation

Segmented users into:

High Spenders: Avg. spend > 70
Low Spenders: Avg. spend ≤ 70
Compared rating behaviors across segments to derive actionable marketing insights.

🛠 Tech Stack

Languages: Python
Libraries: Pandas, NumPy, Scikit-learn, CatBoost, XGBoost, Surprise (SVD), Seaborn, Matplotlib
🧪 Future Improvements

Integrate time-based features for seasonal trends
Use time decay to prioritize recent interactions
Include external data (e.g., marketing campaigns, trend data)
Continuously retrain the model with new data
Explore deep learning-based recommender systems
✅ Conclusion

This project demonstrates the end-to-end pipeline of building and evaluating both content-based and collaborative recommender systems, supported by robust data analysis and model selection techniques. The CatBoost + SVD hybrid model offers a powerful approach to personalizing fashion product recommendations.
