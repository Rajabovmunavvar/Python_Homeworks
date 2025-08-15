# Homework Assignment 1: Analyzing Sales Data

# You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

# Date: Date of the sale.
# Product: Name of the product sold.
# Category: Category to which the product belongs.
# Quantity: Number of units sold.
# Price: Price per unit.


# Tasks:

import pandas as pd

sales_df = pd.read_csv('sales_data.csv')
print(sales_df)
category = sales_df.groupby('Category')
print(category)


# Group the data by the Category column
category = sales_df.groupby('Category')
print(category.size())

# Total quantity sold.
print(category['Quantity'].sum())

# Average price per unit.
print(category['Price'].mean())

# Maximum quantity sold in a single transaction.
print(category['Quantity'].max())

# Identify the top-selling product in each category based on the total quantity sold.

grouped = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

# Find the top-selling product in each category
top_products = grouped.loc[grouped.groupby('Category')['Quantity'].idxmax()]

# Display the results
print(top_products[['Category', 'Product', 'Quantity']])

#Find the date on which the highest total sales (quantity * price) occurred.

sales_df['sum'] = sales_df['Quantity'] * sales_df['Price']
dated = sales_df.pivot_table(values='sum', index='Date').sort_values('sum', ascending=False)
print(dated.head(1))


# Homework Assignment 2: Examining Customer Orders

# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.


import pandas as pd

df = pd.read_csv('customer_orders.csv')

# Group the data by CustomerID and filter out customers who have made less than 20 orders.

customer_stats = df.groupby('CustomerID').agg(
    OrderCount=('OrderID', 'nunique')
    
).reset_index()

# Filter for 20+ orders
frequent_customers_stats = customer_stats[customer_stats['OrderCount'] >= 20]

print(customer_stats)


# Identify customers who have ordered products with an average price per unit greater than $120.

df['UnitPrice'] = df['Price'] / df['Quantity']

customer_avg_unitprice = df.groupby('CustomerID')['UnitPrice'].mean().reset_index()
result = customer_avg_unitprice[customer_avg_unitprice['UnitPrice'] > 120]
print(result)


#Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

product_stats = df.groupby('Product')[['Quantity', 'Price']].sum().reset_index()
filtered_products = product_stats[product_stats['Quantity'] >= 5]
print(filtered_products)


# Homework Assignment 3: Population Salary Analysis

# "task\population.db" sqlite database has population table.
# "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;
# Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.


import sqlite3 as sq
import pandas as pd

with sq.connect('population.db') as conn:
    population=pd.read_sql_query("Select * from population", conn)
    
def band_cat(salary):
    if salary < 200000:
        return "till $200,000"
    elif salary > 200000 and salary <=400000:
        return "$200,001 - $400,000"
    elif salary > 400000 and salary <=600000:
        return "$400,001 - $600,000"
    elif salary > 600000 and salary <=800000:
        return "$600,001 - $800,000"
    elif salary > 800000 and salary <=1000000:
        return "$800,001 - $1,000,000"
    elif salary > 1000000 and salary <=1200000:
        return "$1,000,001 - $1,200,000"
    elif salary > 1200001 and salary <=1400000:
        return "$1,200,001 - $1,400,000"
    elif salary > 1400001 and salary <=1600000:
        return "$1,200,001 - $1,400,000"
    elif salary > 1600001 and salary <=1800000:
        return "$1,600,001 - $1,800,000"
    elif salary >= 1800001:
        return "$1,800,001 and over"
    
population['Salary Band'] = population['salary'].apply(band_cat)
print(population)
grouped_by_salary = population.groupby("Salary Band").agg(
    avg_salary=("salary", "mean"),
    median_salary=('salary','median'),
    number_of_population=("salary", "count"),
)
grouped_by_salary["avg_salary"] = grouped_by_salary["avg_salary"].apply(lambda x: f"{x:,.2f}")
grouped_by_salary["median_salary"] = grouped_by_salary["median_salary"].apply(lambda x: f"{x:,.2f}")
grouped_by_salary["percent_of_total"] = (
    grouped_by_salary["number_of_population"] / population.shape[0] * 100
).apply(lambda x: f"{x:.2f}%")

print(grouped_by_salary)

# Calculate the same measures in each State :

import sqlite3 as sq
import pandas as pd



with sq.connect('population.db') as conn:
    population=pd.read_sql_query("Select * from population", conn)
    

    
grouped_by_state = population.groupby("state").agg(
    avg_salary=("salary", "mean"),
    median_salary=('salary','median'),
    number_of_population=("salary", "count"),
)
grouped_by_state["avg_salary"] = grouped_by_state["avg_salary"].apply(lambda x: f"{x:,.2f}")
grouped_by_state["median_salary"] = grouped_by_state["median_salary"].apply(lambda x: f"{x:,.2f}")
grouped_by_state["percent_of_total"] = (
    grouped_by_state["number_of_population"] / population.shape[0] * 100
).apply(lambda x: f"{x:.2f}%")

print(grouped_by_state)


with pd.ExcelWriter("population_salary_analysis.xlsx") as file:
    grouped_by_salary.to_excel(file, sheet_name="Filtered_by_salary")
    grouped_by_state.to_excel(file, sheet_name="Filtered_by_state")
