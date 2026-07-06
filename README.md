<div align="center">

# 🌱 Crop Yield Prediction & Analysis 🚜

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*A data-driven approach to understanding agricultural resilience and predicting crop output based on climate and farming indicators.*

</div>

## 📌 Project Overview
Climate change and agricultural practices drastically affect crop output. This project explores the FAO/World Bank dataset to analyze how **Rainfall**, **Temperature**, and **Pesticide/Fertilizer use** impact crop yields—with a specific focus on regional crops like **Potatoes in India**. 

By cleaning raw data, conducting exploratory data analysis (EDA), and building a **Multiple Linear Regression Model**, we can simulate real-world economic impacts (such as a 10% drop in rainfall) and measure agricultural vulnerability.

## 🚀 Key Features
- **Automated Data Pipeline:** Uses `kagglehub` to seamlessly fetch the dataset.
- **Data Cleaning & Transformation:** Handles missing values and standardizes units for statistical modeling.
- **Exploratory Data Analysis (EDA):** Generates correlation heatmaps and scatterplots to visualize relationships between climate and yield.
- **Predictive Modeling:** Implements `scikit-learn` linear regression to predict agricultural output.
- **Impact Simulation:** Built-in scenario functions to measure output vulnerability (*"What happens to the yield if rainfall drops by 10%?"*).

## 🛠️ Tech Stack
- **Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn
- **Visualization:** Matplotlib, Seaborn
- **Data Source:** [FAO/World Bank Crop Yield Dataset](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset)

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/Shaik-Hafsa29/-crop-yield-prediction-capstone.git
cd -crop-yield-prediction-capstone
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**
```bash
python download_data.py
```

**4. Run the analysis pipeline**
```bash
python analysis.py
```

## 📊 Outputs & Findings
Running the analysis pipeline generates:
- `correlation_heatmap.png`: Showing the strongest predictors for crop yield.
- `scatter_plots.png`: Visualizing trends between yield, temperature, and rainfall.
- **Console Outputs**: R-squared model metrics, Feature Coefficients, and Economic Simulation results.

*(Check out the `report.md` for a detailed write-up of the statistical logic and domain-specific insights!)*

---
<div align="center">
<b>AkaSOHO Capstone Submission</b> 🎓
</div>
