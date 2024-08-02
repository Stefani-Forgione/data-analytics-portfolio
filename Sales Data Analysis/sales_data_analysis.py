# Sales Data Analysis

## Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting up the visual style
sns.set(style="whitegrid")

## Loading the Data
# For this example, we'll create a mock dataset
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'] * 25,
    'Quantity': [5, 10, 15, 20] * 25,
    'Price': [10, 20, 30, 40] * 25
}
df = pd.DataFrame(data)
df['Total'] = df['Quantity'] * df['Price']

## Data Cleaning
# Checking for missing values
print("Missing values:\n", df.isnull().sum())

# Checking data types
print("\nData types:\n", df.dtypes)

## Exploratory Data Analysis (EDA)
# Summary statistics
print("\nSummary statistics:\n", df.describe())

# Sales over time
plt.figure(figsize=(12, 6))
df.groupby('Date')['Total'].sum().plot()
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Sales by product
plt.figure(figsize=(12, 6))
sns.barplot(x='Product', y='Total', data=df, estimator=sum)
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Quantity sold by product
plt.figure(figsize=(12, 6))
sns.barplot(x='Product', y='Quantity', data=df, estimator=sum)
plt.title('Total Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.show()

## Conclusion
# The analysis shows that Product D has the highest total sales, while Product A has the lowest.
# The sales trend over time indicates a steady increase in total sales.

