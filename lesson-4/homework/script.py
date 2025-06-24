# 1)Write a Python script to sort (ascending and descending) a dictionary by value.
 
my_dict = {"val_1": 3,"val_2": 2,"val_3": 4,"val_4": 16,"val_5": 25,}

sorted_asc = sorted(my_dict.items(), key=lambda x: x[1])  # Sort by value (ascending)
sorted_desc = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)  # Descending

print("Ascending:", sorted_asc)
print("Descending:", sorted_desc)

# 2)Write a Python script to add a key to a dictionary.

#Sample Dictionary:

sample_dict = {0: 10, 1: 20}
#Expected Result:
# {0: 10, 1: 20, 2: 30}

# first method:
sample_dict.update([( 2, 30)])
print(sample_dict)

# second method:

sample_dict[2] = 30
print(sample_dict)

# 3)Write a Python script to concatenate the following dictionaries to create a new one.
#Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

#Expected Result:
#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#solution:
all_dict=dic1 | dic2 | dic3
print(all_dict)

# 4)Write a Python script to generate and print a dictionary that contains a number (between 1 and 5) in the form (x, x*x).

my_dict = {x: x*x for x in range(1, 6)}
print(my_dict)

# 5)Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

square_dict = {x: x*x for x in range(1, 16)}
print(square_dict)

# Set Exercises:

# 1)Write a Python program to create a set.

my_set = {"a", "a", "d", "c", "c","a"}
print(my_set)

#2)Write a Python program to iterate over sets.

my_set = {"a", "a", "d", "c", "c","a"}
for item in my_set:
    print(item) 

# 3)Write a Python program to add member(s) to a set.
my_set = {"a", "a", "d", "c", "c","a"}

# first method (for single entry):
my_set.add("h")
print(my_set)

# second method (for multiple entry):

my_set.update(["w", "qw", "qq", "z", "i"])
print(my_set)

# 4)Write a Python program to remove item(s) from a given set.


my_set = {"a", "a", "d", "c", "c","a"}
my_set.discard("w")
print(my_set)

# 5)Write a Python program to remove an item from a set if it is present in the set.

my_set = {"a", "a", "d", "c", "c", "a"}
if "w" in my_set:
    my_set.remove("w")
print(my_set)
