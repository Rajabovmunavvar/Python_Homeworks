# 1)Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.


text = "abcabcabcdeabcdefabcdefgll"
# abc_abcab_cdeabcd_efabcdef_g

i = 2

used_chars = ['a', 'e', 'i', 'o', 'u']

while i < len(text) - 1:
    if text[i] not in used_chars:
        text = text[:i+1] + '_' + text[i+1:]
        used_chars.append(text[i])
        i += 4
    else:
        i += 1
        
print(text)
             
        
            
            
        

print("".join(result))


# 2)The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.



n = input("insert here: ")
count = 0
if n.isdigit() == True:
    n = int(n)
    if 1 <= n <= 20:
        while count <= n -1:
            
            print(count ** 2)
            count += 1
    else:
        print("the number is out of range")
else:
    print("please insert a digit")

# 3)Loop-Based Exercises:

# ex no 1:Print first 10 natural numbers using a while loop

count = 1 

while count <= 10:
    print(count)
    count += 1


#Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

count = 1
result = []
while count <= 5:
    result.append(count)
    count += 1
    print(" ".join(str(num) for num in result))

# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Example:

# Enter number 10
# Sum is: 55

num = 10
count = 1
total = 0

while count <= num:
    total += count
    count += 1

print("Sum is:", total)


# Exercise 4: Print multiplication table of a given number
# Example:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

m_number = 2
count = 1 


while True:
    result = m_number * count
    print(result)
    count += 1
    if result == 20:
        break




# Exercise 5: Display numbers from a list using a loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected Output:

# 75
# 150
# 145

number = [12, 75, 150, 180, 145, 525, 50]
for item in number:
    if 75 <= item <= 150:
        print(item) 
    
# Exercise 6: Count the total number of digits in a number
# Example:

# 75869
# Output: 5

number = input("insert the number here: ")
count = 0
    
for item in number:
    if item.isdigit(): # in case there are letters or signs in the input
        count += 1

print(count)

# Exercise 7: Print reverse number pattern
#  Example:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

num = [5, 4, 3, 2, 1]
count = len(num)

while count >= 1:
    print(" ".join(str(num1) for num1 in num[:count]))
    count -= 1


# Exercise 8: Print list in reverse order using a loop
# Given:

# list1 = [10, 20, 30, 40, 50]
# Expected Output:

# 50
# 40
# 30
# 20
# 10


list1 = [10, 20, 30, 40, 50]

for item in reversed(list1):
    print(item)


# Exercise 9: Display numbers from -10 to -1 using a for loop
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
  
number = range(-10,0)

for item in number:
    print(item)
    
    
# Exercise 10: Display message “Done” after successful loop execution
# Example:

# 0
# 1
# 2
# 3
# 4
# Done!

nums = range(5)

for item in nums:
    print(item)
else:
    print("Done!")
    


         
# Exercise 11: Print all prime numbers within a range
# Example:

# Prime numbers between 25 and 50:
# 29
# 31
# 37
# 41
# 43
# 47

num_list = range(25, 50)

for num in num_list:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# Exercise 12: Display Fibonacci series up to 10 terms
# Example:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

num_1 = 0
num_2 = 1

list_fibo = [0, 1]

while len(list_fibo) < 10:
    fib_num = list_fibo[num_1] + list_fibo[num_2]
    num_1 += 1
    num_2 += 1
    list_fibo.append(fib_num)
   

print(list_fibo)

    
# Exercise 13: Find the factorial of a given number
# Example:

# 5! = 120

number = 5
fac_numb = number - 1
while fac_numb >= 1:
    number = number * fac_numb
    fac_numb -= 1

print(number)


# Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.

# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]

# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]


list1 = [1, 1, 2]
list2 = [2, 3, 4]
output = []

for item in list1:
    if item not in list2:
        output.append(item)

for item in list2:
    if item not in list1:
        output.append(item)

print(output) 




    
    
