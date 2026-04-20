import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Retail Store Sales Analysis\Retail-Sales-Analysis\sales_data.csv")

print(df.head())

print(df.info())
print(df.describe())

df['total_sales'] = df['quantity'] * df['price']

# Total revenue
total_revenue = df['total_sales'].sum()
print("Total Revenue:", total_revenue)

# Most sold product
top_product = df.groupby('product')['quantity'].sum().idxmax()
print("Top Product:", top_product)

# Revenue by city
city_sales = df.groupby('city')['total_sales'].sum()
print(city_sales)

# Summary stats
print(df.describe())

# Bar chart
df.groupby('product')['total_sales'].sum().plot(kind='bar')
plt.title("Product vs Sales")
plt.show()

# Pie chart
df.groupby('category')['total_sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Distribution")
plt.show()

# Line chart
df.groupby('order_date')['total_sales'].sum().plot(kind='line')
plt.title("Sales Over Time")
plt.show()