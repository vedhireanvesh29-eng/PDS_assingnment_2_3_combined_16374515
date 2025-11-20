import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/diabetes_Dataset_2.csv")
print(df.head())
print(df.isnull().sum())

# PART A: Take a random sample of 25 observations
sample = df.sample(25, random_state=42)

# Compare Glucose (Mean & Max) for sample vs population
print("\nSample Mean Glucose:", sample["Glucose"].mean())
print("Population Mean Glucose:", df["Glucose"].mean())

print("\nSample Max Glucose:", sample["Glucose"].max())
print("Population Max Glucose:", df["Glucose"].max())

# PART B: 98th percentile of BMI
print("\nSample 98th percentile BMI:", np.percentile(sample["BMI"], 98))
print("Population 98th percentile BMI:", np.percentile(df["BMI"], 98))

# PART C: Bootstrap (500 samples, n = 150)
bootstrap_means = []

for _ in range(500):
    boot = df.sample(150, replace=True)
    bootstrap_means.append(boot["BloodPressure"].mean())

print("\nBootstrap Average Mean BP:", np.mean(bootstrap_means))
print("Population Mean BP:", df["BloodPressure"].mean())

# Save histogram
plt.hist(bootstrap_means, bins=30)
plt.title("Bootstrap Mean Blood Pressure")
plt.xlabel("Mean Blood Pressure")
plt.ylabel("Frequency")
plt.savefig("../reports/dataset2_bootstrap_bp.png")

print("\nDataset 2 Analysis Completed Successfully!")
