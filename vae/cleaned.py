import pandas as pd

# Load the CSV file
file_path = 'VAE.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand its structure and identify missing values
data.head(), data.info(), data.isnull().sum()
# Remove columns that are completely empty
cleaned_data = data.dropna(axis=1, how='all')

# Impute missing values for numeric columns with the median
numeric_cols = cleaned_data.select_dtypes(include=['float64']).columns
cleaned_data[numeric_cols] = cleaned_data[numeric_cols].fillna(cleaned_data[numeric_cols].median())

# Impute missing values for object columns with a placeholder
object_cols = cleaned_data.select_dtypes(include=['object']).columns
cleaned_data[object_cols] = cleaned_data[object_cols].fillna('Unknown')



# Display the cleaned dataframe info and check for any remaining missing values
cleaned_data.info(), cleaned_data.isnull().sum().sum()
