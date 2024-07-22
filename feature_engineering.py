import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

# Load data
df = pd.read_csv('data.csv')

# Delete rows with NaN in 'lead_time'
df = df.dropna(subset=['lead_time'])

# Delete columns ['sku']
df = df.drop(['sku'], axis=1)

# Initialize label encoder
le = LabelEncoder()

# Encode categorical columns
categorical_cols = ['potential_issue', 'deck_risk', 'oe_constraint', 'ppap_risk', 'stop_auto_buy', 'rev_stop', 'went_on_backorder']
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Check for missing values and drop them
df = df.dropna()

# Balance 'went_on_backorder' using SMOTE
smote = SMOTE(random_state=42)
df['went_on_backorder'] = le.fit_transform(df['went_on_backorder'])
df_resampled, _ = smote.fit_resample(df.drop('went_on_backorder', axis=1), df['went_on_backorder'])
df = pd.concat([df_resampled, df['went_on_backorder']], axis=1)

# Save the cleaned dataframe
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head())