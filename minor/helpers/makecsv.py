import pandas as pd
import os

# Directory containing the CSV files
directory = './output_columns'

# List of CSV files to combine
csv_files = ['date.csv','energy_production.csv']

# Read and combine the CSV files
combined_df = pd.DataFrame()

for file in csv_files:
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], axis=1)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(os.path.join(directory, 'total.csv'), index=False)