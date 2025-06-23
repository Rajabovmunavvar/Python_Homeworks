# 1)Create a list containing five different fruits and print the third fruit.

fruits = ['apple', 'banana','lemon','coconut','orange']

print(fruits[2])   # since the index starts with 0 , lemon is the third fruit 


# 2)Create two lists of numbers and concatenate them into a single list.

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

# first method : 
print(list_1+list_2)

# second method :
list_1.extend(list_2)
print(list_1)

# 3)Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers = [5, 8, 12, 20, 25, 30, 35, 55, 65]

first = numbers[0] #first element
mid = numbers[len(numbers)//2] # mid element
last = numbers[-1] # last element

new_list = [first,mid,last]
print(new_list)

# 4)Create a list of your five favorite movies and convert it into a tuple.

movielist = ['breaking bad', 'shawshank redemtion', 'fight club']

movie_tuple = tuple(movielist)
 
print(movie_tuple)

#5)Given a list of cities, check if "Paris" is in the list and print the result.

city_list = ['berlin','tashkent','warsawa','Paris']

if 'Paris' in city_list:
 print("Paris exists in the list")
else:
 print("Paris does not exist in the list")

# 6)Create a list of numbers and duplicate it without using loops.

my_list = [1, 2,3, 4, 5, 6, 7]

# first method:
copy_list = my_list[:]
print(copy_list)

# second method:

copy_list_2 = list(my_list)

print(copy_list_2)

#third method: 

copy_list_3 = my_list.copy()

print(copy_list_3)

# 7)Given a list of numbers, swap the first and last elements.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print(my_list)


# 8) Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tuple_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tuple_list[3:7])

# 9)Create a list of colors and count how many times "blue" appears in the list.

colors = ["blue","yellow","red","purple","blue"]

print(colors.count("blue"))

# 10)Given a tuple of animals, find the index of "lion".

animals = ("giraffe","rabbit", "wolf","deer","lion")

print(animals.index("lion"))

# 11)Create two tuples of numbers and merge them into a single tuple.

tuple_1 = (1, 2, 3, 4)
tuple_2 = (5, 6, 7, 8)

single_tup = tuple_1+tuple_2

print(single_tup)

# 12)Given a list and a tuple, find and print their lengths.

tup = (1, 2, 3, 4, 5)
lis = [9, 8, 7, 6, 5, 10]

print("length of tuple:",len(tup),"\nlength of list:",len(lis))

# 13)Create a tuple of five numbers and convert it into a list.

tuple_list = (1, 2, 3, 4, 5)

list_converted = list(tuple_list)
print(list_converted)


# 14)Given a tuple of numbers, find and print the maximum and minimum values.

tuple_list = (1, 2, 3, 4, 5)

print("Maximum value:",max(tuple_list),"\nMinimum value:",min(tuple_list))

# 15)Create a tuple of words and print it in reverse order.

words = ("animal","banana","circus","dolphin")
reverse_words = words[::-1]
print(reverse_words)
