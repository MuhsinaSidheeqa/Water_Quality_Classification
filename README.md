# Water_Quality_Classification
Water Quality Classification Using Machine Learning! 🌍
In this project, I applied supervised machine learning techniques to classify whether water is safe for consumption — based on its chemical and microbial composition. 

📊 Dataset Overview

The dataset includes over 20 features such as:
aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, flouride , bacteria, viruses, lead , nitrates, nitrites, mercury, perchlorate, radium, selenium, silver, uranium.

🎯 Target: is_safe (0 = Not safe, 1 = Safe)


🛠️ Project Workflow
✅Data Cleaning
Identified and handled missing values using mean/mode imputation
✅Exploratory Data Analysis
Visualized distributions & correlations between contaminants and target
✅Feature Engineering
Scaled numeric data
🤖Algorithms used:
RandomForest,XGBoost,AdaBoosting,GradientBoosting,DecisionTree ,SVC, Naive Bayes ,KNeighbors.

Evaluation
XGBoost Classifier gave the best results 🌟 with ~98% accuracy
Analyzed precision, recall, F1-score, and feature importance

📚Packages used:
#sklearn
#pandas
#seaborn
#matplotlib
#plotly
