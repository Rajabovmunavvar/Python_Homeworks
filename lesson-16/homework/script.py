# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
import numpy as n
original_list = [12.23, 13.32, 100, 36.32]

num_array = n.array(original_list)

print(type(num_array))

# 2)Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]
import numpy as n

matrix = n.arange(2, 11).reshape(3, 3) 
print(matrix)

# 3)Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
import numpy as n 

n_null = n.zeros(10) 

n_null[6] = 11

print(n_null)

# 4)Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as n 

n_values =n.arange(12, 38)

print(n_values)


# 5)Write a NumPy program to convert an array to a floating type.

# Sample output:

# Original array [1, 2, 3, 4]
import numpy as n 
original_array = n.arange(1,5)
float_array = original_array.astype(n.float64)
print(original_array)
print(float_array)

# 6)Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
import numpy as np  # Standard alias
arr_1_celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
arr_2_faren = np.round((arr_1_celsius * 1.8) + 32, 2) 
np.set_printoptions(suppress=True)
print(arr_2_faren)


# 7)Write a NumPy program to append values to the end of an array.

# Expected Output:

# Original array: [10, 20, 30]

# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

import numpy as n

original_array = n.array([10, 20, 30])
appended_array = n.append(original_array, [40, 50, 60, 70, 80, 90])
print(appended_array)

# 8)Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
import numpy as np  # Standard convention is to use 'np' as the alias

# Create random array of 10 integers between 5 and 50
random_array = np.random.randint(5, 50, size=10)

print("Random Array:", random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array))

# 9)Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np  

random_matrix = np.random.randint(5, 50, size=(10, 10))
print(f"Random matrix: {random_matrix}")
min_row = np.min(random_matrix, axis=1)
max_row = np.max(random_matrix, axis=1)
min_col = np.min(random_matrix, axis=0)
max_col = np.max(random_matrix, axis=0)
print(f"Minimum Row-Wise Values: {min_row}")
print(f"Maximum Row-Wise Values: {max_row}")
print(f"Minimum Column-Wise Values: {min_col}")
print(f"Maximum Column-Wise Values: {max_col}")

#10)Create a 3x3x3 array with random values.
import numpy as np

random_array = np.random.randint(5, 50, size=(3,3,3))

print(random_array)
