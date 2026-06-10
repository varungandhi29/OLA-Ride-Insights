import pandas as pd

df = pd.read_excel("data/OLA_DataSet (1).xlsx")

df['Canceled_Rides_by_Customer'] = df['Canceled_Rides_by_Customer'].fillna('Not Cancelled')
df['Canceled_Rides_by_Driver'] = df['Canceled_Rides_by_Driver'].fillna('Not Cancelled')
df['Incomplete_Rides'] = df['Incomplete_Rides'].fillna('No')
df['Incomplete_Rides_Reason'] = df['Incomplete_Rides_Reason'].fillna('Not Applicable')
df['Payment_Method'] = df['Payment_Method'].fillna('Not Applicable')
df['Driver_Ratings'] = df['Driver_Ratings'].fillna(0)
df['Customer_Rating'] = df['Customer_Rating'].fillna(0)
df['V_TAT'] = df['V_TAT'].fillna(0)
df['C_TAT'] = df['C_TAT'].fillna(0)
df['Date'] = pd.to_datetime(df['Date'])

print(df.isnull().sum())
print(df.shape)

df.to_csv("data/ola_cleaned.csv", index=False)
print("Cleaned data saved successfully")