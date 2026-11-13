import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
#'Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country',
#'Postal Code', 'Market', 'Region', 'Product ID', 'Category',
# 'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount',
# 'Profit', 'Shipping Cost', 'Order Priority'])


file_path = "GlobalSuperstore.xlsx"
df = pd.read_excel(file_path)
print(df.head())

# check the data types of the columns
print(df.dtypes)

# print all the column names
print(df.columns)


# check for missing values
print(df.isnull().sum())


#1. Clean column names and remove whitespace
# your code her
df = df.columms

#2. Aggregate sales by Region, Category, and Year


#3. Identify most profitable categories


#4. Merge customer and order tables


#5. Create bar and line plots to show revenue growth
#Task 5. Create bar and line plots to show revenue growth
import matplotlib.pyplot as plt
import seaborn as sns

# Plot total sales per year
sales_per_year = df.groupby('year')['sales'].sum().reset_index()

# Line Plot
plt.figure(figsize=(10,5))
sns.lineplot(x='year', y='sales', data=sales_per_year, marker='o')
plt.title('Total Sales Per Year')
plt.xlabel('Years')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Bar Plot for Sales by Region
plt.figure(figsize=(10,5))
sns.barplot(x='region', y='sales', data=df.groupby('region')['sales'].sum().reset_index())
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()