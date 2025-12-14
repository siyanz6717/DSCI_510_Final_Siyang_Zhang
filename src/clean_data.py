import pandas as pd
import os

# Clearing up the directory
current_folder = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(current_folder)
raw_dir = os.path.join(project, "data", "raw")
processed_dir = os.path.join(project, "data", "processed")

# Read the raw dataframes
df_cost = pd.read_csv(os.path.join(raw_dir, "cost_of_living.csv"))
df_qual = pd.read_csv(os.path.join(raw_dir, "quality_of_life.csv"))

# Since both dataframes contain col index, we choose to drop one to avoid key error
if 'Cost of Living Index' in df_qual.columns:
    df_qual = df_qual.drop(columns=['Cost of Living Index'])

# Normalize the city name variable to avoid mismatches due to different spellings
df_cost['city_join'] = df_cost.iloc[:, 1].astype(str).str.lower().str.strip()
df_qual['city_join'] = df_qual.iloc[:, 1].astype(str).str.lower().str.strip()

# Merge two dataframe
merged = pd.merge(df_cost, df_qual, on='city_join', suffixes=('_cost', '_qual'))

# Select the columns we need
final_df = pd.DataFrame()
final_df['City'] = merged['City_cost'] 
final_df['Cost_Index'] = merged['Cost of Living Index']
final_df['Rent_Index'] = merged['Rent Index']
final_df['Quality_Index'] = merged['Quality of Life Index']
final_df['Safety_Index'] = merged['Safety Index']

# Setting up the region
def get_region(city):
    city = str(city).lower()
    if any(x in city for x in ['usa', 'united states', 'canada', 'new york', 'angeles', 'chicago']): return 'North America'
    if any(x in city for x in ['china', 'japan', 'korea', 'tokyo', 'beijing', 'shanghai', 'singapore', 'thailand', 'vietnam', 'india']): return 'Asia'
    if any(x in city for x in ['germany', 'france', 'uk', 'united kingdom', 'london', 'paris', 'italy', 'spain', 'sweden', 'netherlands', 'switzerland']): return 'Europe'
    if any(x in city for x in ['australia', 'new zealand', 'sydney', 'melbourne']): return 'Oceania'
    if any(x in city for x in ['brazil', 'argentina', 'colombia', 'mexico']): return 'South/Latin America'
    if any(x in city for x in ['egypt', 'south africa', 'nigeria']): return 'Africa'
    return 'Other' # To make sure each city has a region belonging to

final_df['Region'] = final_df['City'].apply(get_region)

# Cleansing and calculation
# We only want to take effective data so we drop the rows with None values
final_df = final_df.dropna()
final_df = final_df[final_df['Cost_Index'] > 0]
final_df['Geo_Arbitrage_Score'] = final_df['Quality_Index'] / final_df['Cost_Index']

# Save the processed data
save_path = os.path.join(processed_dir, "geo_arbitrage_data.csv")
final_df.to_csv(save_path, index=False)