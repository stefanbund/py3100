import csv
import pandas as pd

# Read the original CSV file into a pandas DataFrame
df = pd.read_csv("ProductList.csv")

# Split the DataFrame into 20 smaller DataFrames
dfs = [df[i:i + len(df) // 20] for i in range(0, len(df), len(df) // 20)]

# Write each smaller DataFrame to a separate CSV file
for i, df in enumerate(dfs):
    df.to_csv(f"ProductList_{i}.csv", index=False)

print("The 'ProductList.csv' file has been divided into 20 smaller CSV files.")
