import pandas as pd

# Load data from CSV file
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found. Please make sure the file 'data.csv' exists in the same directory as this script.")
    exit(1)
except pd.errors.ParserError:
    print("Error parsing CSV file. Please ensure the file is in the correct format.")
    exit(1)

# Perform some data transformation here.
# For the purpose of this example, let's just drop any rows with missing data.
data = data.dropna()

# Save the cleaned data to a new CSV file
try:
    data.to_csv('cleaned_data.csv', index=False)
except IOError:
    print("Error writing to file. Please ensure you have the necessary permissions.")
    exit(1)

# Print the top 5 rows of the cleaned dataframe
print(data.head(5))