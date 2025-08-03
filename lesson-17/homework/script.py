# Homework 1:

# import pandas as pd

# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame


import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
        } 
df = pd.DataFrame(data)


# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
column_map = {'First Name': 'first_name','Age': 'age' }
df = df.rename(columns=column_map)

# Print the first 3 rows of the DataFrame
print(df.head(3))

# Find the mean age of the individuals
print(df['age'].mean())

# Select and print only the 'Name' and 'City' columns
print(df[['first_name','City']])

# Add a new column 'Salary' with random salary values
import random
import numpy as np

df['Salary'] = np.random.randint(10000, 20001, size=len(df))
print(df)

# Display summary statistics of the DataFrame
print(df.describe())




# Homework 2:

# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
# Month	Sales	Expenses
# Jan	5000	3000
# Feb	6000	3500
# Mar	7500	4000
# Apr	8000	4500
# Calculate and display the maximum sales and expenses.
# Calculate and display the minimum sales and expenses.
# Calculate and display the average sales and expenses.

import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Sales': [5000, 6000, 7500, 8000],
        'Expenses': [3000, 3500, 4000, 4500]
        } 

data_f = pd.DataFrame(data)

max_sale = data_f['Sales'].max()
min_sale = data_f['Sales'].min()
max_exp = data_f['Expenses'].max()
min_exp = data_f['Expenses'].min()
avg_sale = data_f['Sales'].mean()
avg_exp = data_f['Expenses'].mean()

print(f"\nMaximum Sales: {max_sale}"
      f"\nMaximum Expenses: {max_exp}"
      f"\nMinimum Sales: {min_sale}"
      f"\nMinimum Expenses {min_exp}"
      f"\nAverage Sales: {avg_sale}"
      f"\nAverage Expenses: {avg_exp}" 
      )

# Homework 3:

# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
# Category	January	February	March	April
# Rent	1200	1300	1400	1500
# Utilities	200	220	240	250
# Groceries	300	320	330	350
# Entertainment	150	160	170	180
# Calculate and display the maximum expense for each category.
# Calculate and display the minimum expense for each category.
# Calculate and display the average expense for each category.
# In this task, use .set_index method to make Category column as index.

# Try this code, learn it and use it in the task.

# expenses.set_index('Category')

import pandas as pd

# Create DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index (as required by the task)
expenses.set_index('Category', inplace=True)

# Calculate stats
stats = pd.DataFrame({
    'Max_Expense': expenses.max(axis=1),
    'Min_Expense': expenses.min(axis=1),
    'Avg_Expense': expenses.mean(axis=1)
})

print(stats)

