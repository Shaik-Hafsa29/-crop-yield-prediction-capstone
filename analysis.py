import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# 1. DATA ACQUISITION & CLEANING
# ==========================================
def load_and_clean_data(filepath='yield_df.csv'):
    print("Loading data...")
    # yield_df.csv is the typical output file from the recommended Kaggle dataset
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please ensure the dataset is downloaded.")
        return None

    print(f"Initial shape: {df.shape}")
    
    # Check for missing values
    print("Missing values per column:\n", df.isnull().sum())
    
    # Drop rows with missing values
    df = df.dropna()
    
    # Rename columns for easier access
    df.rename(columns={
        'hg/ha_yield': 'Yield_hg_ha',
        'average_rain_fall_mm_per_year': 'Rainfall_mm',
        'pesticides_tonnes': 'Pesticides_tonnes',
        'avg_temp': 'Avg_Temp_C'
    }, inplace=True, errors='ignore')
    
    # Convert data types if necessary
    if 'Rainfall_mm' in df.columns:
        # Sometimes rainfall has non-numeric values in this dataset like '..'
        df['Rainfall_mm'] = pd.to_numeric(df['Rainfall_mm'], errors='coerce')
        df = df.dropna(subset=['Rainfall_mm'])
        
    print(f"Shape after cleaning: {df.shape}")
    return df

# ==========================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================
def perform_eda(df, target_country='India', target_crop='Potatoes'):
    print(f"\n--- EDA for {target_crop} in {target_country} ---")
    
    # Filter for the specific country and crop
    subset = df[(df['Area'] == target_country) & (df['Item'] == target_crop)]
    if subset.empty:
        print("No data available for the specified crop and region.")
        return None
        
    print(f"Data points for {target_crop} in {target_country}: {len(subset)}")
    
    # Correlation Matrix
    numeric_cols = ['Yield_hg_ha', 'Rainfall_mm', 'Pesticides_tonnes', 'Avg_Temp_C']
    corr = subset[numeric_cols].corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f'Correlation Matrix: Factors vs Yield ({target_crop} in {target_country})')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    print("Saved correlation heatmap to 'correlation_heatmap.png'.")
    
    # Scatter plots against Yield
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    sns.scatterplot(data=subset, x='Rainfall_mm', y='Yield_hg_ha', ax=axes[0])
    axes[0].set_title('Yield vs Rainfall')
    
    sns.scatterplot(data=subset, x='Avg_Temp_C', y='Yield_hg_ha', ax=axes[1])
    axes[1].set_title('Yield vs Temperature')
    
    sns.scatterplot(data=subset, x='Pesticides_tonnes', y='Yield_hg_ha', ax=axes[2])
    axes[2].set_title('Yield vs Pesticides')
    
    plt.tight_layout()
    plt.savefig('scatter_plots.png')
    print("Saved scatter plots to 'scatter_plots.png'.")
    
    return subset

# ==========================================
# 3. REGRESSION MODELING
# ==========================================
def train_model(subset):
    print("\n--- Training Regression Model ---")
    
    X = subset[['Rainfall_mm', 'Avg_Temp_C', 'Pesticides_tonnes']]
    y = subset['Yield_hg_ha']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"Model R-squared: {r2:.4f}")
    print(f"Model RMSE: {rmse:.4f}")
    
    print("\nFeature Coefficients:")
    for feature, coef in zip(X.columns, model.coef_):
        print(f"  {feature}: {coef:.4f}")
        
    return model, X

# ==========================================
# 4. ECONOMIC IMPACT SIMULATION
# ==========================================
def simulate_rainfall_drop(model, df_subset, drop_percentage=0.10):
    print(f"\n--- Simulating a {drop_percentage*100}% Drop in Rainfall ---")
    
    # Current averages
    avg_rainfall = df_subset['Rainfall_mm'].mean()
    avg_temp = df_subset['Avg_Temp_C'].mean()
    avg_pesticides = df_subset['Pesticides_tonnes'].mean()
    
    # Baseline Prediction
    baseline_features = pd.DataFrame({
        'Rainfall_mm': [avg_rainfall],
        'Avg_Temp_C': [avg_temp],
        'Pesticides_tonnes': [avg_pesticides]
    })
    baseline_yield = model.predict(baseline_features)[0]
    
    # Dropped Rainfall Prediction
    dropped_rainfall = avg_rainfall * (1 - drop_percentage)
    dropped_features = pd.DataFrame({
        'Rainfall_mm': [dropped_rainfall],
        'Avg_Temp_C': [avg_temp],
        'Pesticides_tonnes': [avg_pesticides]
    })
    dropped_yield = model.predict(dropped_features)[0]
    
    impact_hg_ha = baseline_yield - dropped_yield
    percent_change = (impact_hg_ha / baseline_yield) * 100 if baseline_yield != 0 else 0
    
    print(f"Baseline Yield (at avg conditions): {baseline_yield:.2f} hg/ha")
    print(f"Yield after {drop_percentage*100}% rainfall drop: {dropped_yield:.2f} hg/ha")
    print(f"Absolute Drop in Yield: {impact_hg_ha:.2f} hg/ha")
    print(f"Percentage Change in Yield: -{percent_change:.2f}%")

if __name__ == "__main__":
    df = load_and_clean_data()
    if df is not None:
        subset = perform_eda(df, target_country='India', target_crop='Potatoes')
        if subset is not None:
            model, X = train_model(subset)
            simulate_rainfall_drop(model, subset, drop_percentage=0.10)
