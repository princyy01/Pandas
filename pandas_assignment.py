import pandas as pd

# Load the dataset
df = pd.read_csv('Used_Bikes.csv')

# 1. Find out the number of records for each ownership type
ownership_counts = df['owner'].value_counts()
print("Number of records for each ownership type:")
print(ownership_counts)

# 2. Find out the number of bikes with "First Owner" and age <= 5
first_owner_young_bikes = df[(df['owner'] == 'First Owner') & (df['age'] <= 5)]
first_owner_young_count = first_owner_young_bikes.shape[0]
print("\nNumber of bikes with 'First Owner' and age <= 5:")
print(first_owner_young_count)

# 3. Find out the bikes at Jaipur location, price under 60K
jaipur_bikes_under_60k = df[(df['location'] == 'Jaipur') & (df['price'] < 60000)]
print("\nBikes at Jaipur location with price under 60K:")
print(jaipur_bikes_under_60k)

# 4. Find out the KTM brand bikes with minimum and maximum price
ktm_bikes = df[df['brand'] == 'KTM']
min_price_bike = ktm_bikes.loc[ktm_bikes['price'].idxmin()]
max_price_bike = ktm_bikes.loc[ktm_bikes['price'].idxmax()]

print("\nKTM brand bike with minimum price:")
print(min_price_bike)

print("\nKTM brand bike with maximum price:")
print(max_price_bike)
