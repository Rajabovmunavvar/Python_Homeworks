import pandas as pd
import sqlite3 as sq
import numpy as np
import matplotlib.pyplot as plt


data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.

df1['Avg_score'] = round(df1[['Math','English','Science']].mean(axis=1),2)

print(df1)

# Exercise 2: Find the student with the highest average grade.

top_student_idx = df1['Avg_score'].idxmax()
top_student = df1.loc[top_student_idx]

print(top_student['Student_ID'], 'Has the highest average score: ', top_student['Avg_score']) 

#Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total']  =df1[['Math','English','Science']].sum(axis=1)
print(df1)

# Exercise 4: Plot a bar chart to visualize the average grades in each subject.

subject_avgs = df1.drop(['Student_ID','Avg_score','Total'], axis=1).mean()

subject_avgs.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Grades by Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()



data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)


# Calculate the total sales for each product.

total_sale_per_product = df2[['Product_A','Product_B','Product_C']].sum().to_frame('Total_Sales').T
total_sale_per_product


# Find the date with the highest total sales.

df2['Total_sales'] = df2[['Product_A','Product_B','Product_C']].sum(axis=1)
top_date_index = df2['Total_sales'].idxmax()
top_date = df2.loc[top_date_index].to_frame('Date').T
top_date

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df2['Product_A_change'] = round((df2['Product_A'] - df2['Product_A'].shift(1))/(df2['Product_A'].shift(1) / 100),2)  # shifts values down by 1 row
df2['Product_B_change'] = round((df2['Product_B'] - df2['Product_B'].shift(1))/(df2['Product_B'].shift(1) / 100),2)  # shifts values down by 1 row
df2['Product_C_change'] = round((df2['Product_C'] - df2['Product_C'].shift(1))/(df2['Product_C'].shift(1) / 100),2)  # shifts values down by 1 row
theframe = df2[['Date','Product_A_change','Product_B_change','Product_C_change']].fillna('No Previous Date')
theframe

#Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

df2.plot(x='Date', y=['Product_A','Product_B','Product_C'],kind='line',
            title='Sales Trend For Each Product',
            figsize=(10, 6),
            color=['green','blue','red'],
            linestyle='-',
            marker='o')


#DataFrame 3: Employee Information:

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
dep_avg = df3.groupby('Department')['Salary'].mean().to_frame('Avg_Sal_Per_Dep').round(2)
dep_avg

# Exercise 2: Find the employee with the most experience.
top_exp_emp_index = df3['Experience (Years)'].idxmax()
most_experienced = df3.loc[top_exp_emp_index]
most_experienced.to_frame().T

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
minimum_salary = df3['Salary'].min()
df3["Salary Increase"] = round(minimum_salary / (df3['Salary'] - minimum_salary),2)
df3['Salary Increase'] = df3['Salary Increase'].astype(str) + '%'
df3

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
df3
emp_distriution = df3.groupby('Department')['Employee_ID'].count().to_frame('Employee Count')

emp_distriution.plot(kind='bar', title='distribution of employees across different departments')

# DataFrame 4: Customer Orders:

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)


# Exercise 1: Calculate the total revenue from all orders.
total_ravenue = df4['Total_Price'].sum()
print(f'Total revenue from all orders: ${total_ravenue}')

# Exercise 2: Find the most ordered product.
product_g = df4.groupby('Product')['Quantity'].sum().to_frame('total_qnt_ordered')
most_ordered_index = product_g['total_qnt_ordered'].idxmax()
most_ordered_prod = product_g.loc[most_ordered_index]
print(f'The most ordered product is {most_ordered_index} with total of  {most_ordered_prod['total_qnt_ordered']} orders' )

# Exercise 3: Calculate the average quantity of products ordered.
avg_quantity = df4['Quantity'].mean()
print(f'average quantity of products ordered: {avg_quantity}')
