import pandas as pd

# Load the CSV file
df = pd.read_csv('./combined.csv')

# Drop rows with any null values
df.dropna(inplace=True)

# Replace zero values with the mean of their respective columns
df.replace(0, pd.NA, inplace=True)
df.fillna(df.mean(), inplace=True)

# Save the cleaned data to a new CSV file
df.to_csv('./cleaned_combined.csv', index=False)