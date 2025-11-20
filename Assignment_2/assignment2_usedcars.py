import pandas as pd

# Load dataset
df = pd.read_csv("../data/train_Dataset_1.csv")
print(df.head())
print(df.isnull().sum())

# Drop New_Price column (more than 85% missing)
df = df.drop(columns=["New_Price"])

# Replace missing values in Seats using mode
df["Seats"] = df["Seats"].fillna(df["Seats"].mode()[0])

# MILEAGE – remove units ? numeric ? median imputation
df["Mileage"] = df["Mileage"].str.extract(r'(\d+\.?\d*)').astype(float)
df["Mileage"] = df["Mileage"].fillna(df["Mileage"].median())

# ENGINE – remove units ? numeric ? median imputation
df["Engine"] = df["Engine"].str.extract(r'(\d+)').astype(float)
df["Engine"] = df["Engine"].fillna(df["Engine"].median())

# POWER – remove units ? numeric ? median imputation
df["Power"] = df["Power"].str.extract(r'(\d+\.?\d*)').astype(float)
df["Power"] = df["Power"].fillna(df["Power"].median())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# PART C – One-hot encoding
df = pd.get_dummies(df, columns=["Fuel_Type", "Transmission"], drop_first=True)

# PART D – Create new features
df["Car_Age"] = 2025 - df["Year"]
df["Price_per_KM"] = df["Price"] / (df["Kilometers_Driven"] + 1)

# PART E – Data operations
selected = df[["Name", "Year", "Price", "Car_Age", "Kilometers_Driven"]]

recent_cars = df[df["Year"] >= 2015]
mid_price_cars = df[(df["Price"] >= 5) & (df["Price"] <= 15)]

df_renamed = df.rename(columns={
    "Name": "Car_Model",
    "Kilometers_Driven": "KM_Driven"
})

df["Age_Category"] = pd.cut(df["Car_Age"], bins=[-1, 3, 7, 100],
                            labels=["New", "Medium", "Old"])

sorted_by_price = df.sort_values("Price", ascending=False)

price_by_owner = df.groupby("Owner_Type")["Price"].agg(["count", "mean", "min", "max"]).round(2)

df.to_csv("../reports/Assignment2_cleaned_output.csv", index=False)
print("\nAssignment 2 completed successfully!")
