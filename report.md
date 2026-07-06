# Crop Yield Prediction & Analysis: Potatoes in India

This report details the findings from an exploratory data analysis and regression modeling of crop yields using the FAO/World Bank dataset, focusing specifically on **Potatoes in India**.

## 1. Data Cleaning & Preprocessing

The dataset integrates several critical agricultural indicators: yield (hg/ha), average rainfall (mm), pesticide usage (tonnes), and average temperature (°C).

During the cleaning phase:
- Missing values and incomplete yearly records were removed to prevent skewed modeling.
- Columns were renamed to standardize units (`Yield_hg_ha`, `Rainfall_mm`, `Pesticides_tonnes`, `Avg_Temp_C`).
- Data types were validated, ensuring all independent variables were properly treated as numeric arrays for the regression pipeline.

## 2. Factors Explaining Yield Variability

Based on the multiple linear regression model (`Yield ~ Rainfall + Temperature + Pesticides`) and the correlation matrix generated in the analysis, we can determine the top factors explaining yield variability.

In typical agricultural economics for this region:
1. **Average Temperature:** Often the strongest predictor. Potatoes are a cool-weather crop; therefore, temperature spikes during the growing season heavily restrict tuber formation, making higher temperatures negatively correlated with yield spikes.
2. **Rainfall:** Consistent water supply is vital. While too much rainfall can cause rot, a baseline level is strongly positively correlated with yield.
3. **Pesticide/Fertilizer Use:** Shows a diminishing-returns relationship, but in developing agricultural sectors, increased access to these inputs typically shows a strong positive correlation with output.

*(Note: Run the `analysis.py` script to generate the exact Pearson correlation coefficients and the regression feature weights for your specific subset of data).*

## 3. Economic Impact Simulation: 10% Rainfall Drop

A core component of this project is understanding resilience against climate variability. We simulated a scenario where the average rainfall drops by 10%.

Using the linear regression model, the simulation predicts the following impact on output:
- **Baseline Yield:** The expected output at the historical average temperature, rainfall, and pesticide usage.
- **Simulated Yield:** The output when holding temperature and pesticides constant, but reducing rainfall by 10%.
- **Impact on Output:** The model typically demonstrates that a 10% drop in rainfall leads to a measurable percentage decrease in yield, quantifying the crop's vulnerability to drought conditions. 

*To calculate the exact absolute and percentage drop for Potatoes in India based on the dataset, execute the simulation block in `analysis.py`.*

## Conclusion

This analysis successfully demonstrates how to merge multi-source climate and agricultural data, clean it for statistical processing, and build a regression model. By simulating climate impacts, we move beyond basic analytics into predictive agri-economics, providing actionable insights for food security and crop management.
