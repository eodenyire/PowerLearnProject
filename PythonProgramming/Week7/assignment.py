# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Task 1: Load and Explore the Dataset
# Loading the Iris dataset using sklearn
iris = load_iris()

# Converting the dataset into a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Checking the data types and missing values
print("\nData Types and Missing Values:")
print(df.info())

# Task 2: Basic Data Analysis
# Compute the basic statistics of the numerical columns
print("\nBasic Statistics of the Numerical Columns:")
print(df.describe())

# Perform groupings on the 'species' column and compute the mean of each numerical column
grouped_data = df.groupby('species').mean()
print("\nMean of Numerical Columns by Species:")
print(grouped_data)

# Task 3: Data Visualization

# 1. Line chart showing trends over time (let's simulate a trend)
# Simulating some time-series data for the demonstration
time = pd.date_range(start='1/1/2020', periods=50, freq='M')
sales = np.random.randint(100, 500, size=50)

# Create a DataFrame for this simulated data
sales_df = pd.DataFrame({'Date': time, 'Sales': sales})

# Line Chart for Sales over Time
plt.figure(figsize=(10, 6))
plt.plot(sales_df['Date'], sales_df['Sales'], marker='o', linestyle='-', color='b', label='Sales')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 2. Bar Chart comparing the average petal length per species
plt.figure(figsize=(10, 6))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color='green')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()

# 3. Histogram for the distribution of Sepal Length
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, color='orange', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], color='purple', label='Sepal vs Petal Length')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# Task 4: Error Handling for Missing Data (if any)
try:
    # Check for missing data and fill it if necessary
    if df.isnull().any().any():
        df.fillna(df.mean(), inplace=True)  # Filling missing values with mean
        print("\nMissing values found and filled.")
    else:
        print("\nNo missing values in the dataset.")
except Exception as e:
    print(f"\nError occurred: {e}")

# Save the modified dataset to a new CSV file
df.to_csv('modified_iris_dataset.csv', index=False)
print("\nModified dataset saved to 'modified_iris_dataset.csv'.")
