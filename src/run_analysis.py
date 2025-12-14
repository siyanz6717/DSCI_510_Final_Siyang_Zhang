import pandas as pd
import os
from scipy import stats

# Clearing up the directory
current_folder = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(current_folder)
processed_dir = os.path.join(project, "data", "processed")
results_dir = os.path.join(project, "results")

# Read data
data_path = os.path.join(processed_dir, "geo_arbitrage_data.csv")
df = pd.read_csv(data_path)
report_content = "Geo-Arbitrage Analysis Report\n\n"

# Correlation analysis (Rentvs. Safety index)
if 'Rent_Index' in df.columns and 'Safety_Index' in df.columns:
    corr_rent_safety = df['Rent_Index'].corr(df['Safety_Index'])
    report_content += "Correlation Analysis (Rent vs. Safety)\n"
    report_content += f"Correlation Coefficient: {corr_rent_safety:.4f}\n"
    if abs(corr_rent_safety) < 0.3:
        interpretation = "Weak correlation."
    elif corr_rent_safety > 0.0:
        interpretation = "Positive correlation."
    else:
        interpretation = "Negative correlation."
    report_content += f"Interpretation: {interpretation}\n\n"

# Regional Analysis
if 'Region' in df.columns:
    region_stats = df.groupby('Region')['Geo_Arbitrage_Score'].mean().sort_values(ascending=False)
    report_content += "Regional Analysis (Average Geo-Arbitrage Score)\n"
    report_content += region_stats.to_string() + "\n\n"

# Outlier Analysis (Residuals)
if 'Cost_Index' in df.columns and 'Quality_Index' in df.columns:
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Cost_Index'], df['Quality_Index'])
    
    # Calculating residuals
    df['Predicted_Quality'] = slope * df['Cost_Index'] + intercept
    df['Residual'] = df['Quality_Index'] - df['Predicted_Quality']

    top_undervalued = df.sort_values(by='Residual', ascending=False).head(5)
    top_overvalued = df.sort_values(by='Residual', ascending=True).head(5)

    report_content += "Outlier Analysis (Residuals)\n"
    report_content += "Top 5 'Undervalued' Cities (High Quality for the Price):\n"
    for idx, row in top_undervalued.iterrows():
        report_content += f"{row['City']} (Region: {row.get('Region', 'N/A')}): Score {row['Geo_Arbitrage_Score']:.2f}\n"

    report_content += "Top 5 'Overvalued' Cities (Low Quality for the Price):\n"
    for idx, row in top_overvalued.iterrows():
        report_content += f"{row['City']} (Region: {row.get('Region', 'N/A')}): Score {row['Geo_Arbitrage_Score']:.2f}\n"

# Save analysis results
output_txt_path = os.path.join(results_dir, "analysis_summary.txt")
with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write(report_content)
f.close()

# Save data with residuals
output_csv_path = os.path.join(processed_dir, "geo_arbitrage_with_residuals.csv")
df.to_csv(output_csv_path, index=False)