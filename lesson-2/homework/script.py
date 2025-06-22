# 1)Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

username = input("Name :" )

year_of_birth = input("Birth year :")
import datetime
now = datetime.datetime.now().year
age = int(now) - int(year_of_birth)

print("Name :",username)
print("Age :",age)

# 2)xtract car names from the following text: txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'

firs_car_name = txt[0::2]
second_car_name = txt[1::2]
print("first car :",firs_car_name)
print("second car :",second_car_name)

# 3)Extract car names from the following text: txt = 'MsaatmiazD'

txt = 'MsaatmiazD'

firs_car_name1 = txt[::2]
second_car_name2 = txt[-1::-2]
print(firs_car_name1)
print(second_car_name2)

# 4)Extract the residence area from the following text: txt = "I'am John. I am from London"

txt = "I'am John. I am from London"

# Second Method :
residence_area = txt[txt.find('from')+5:]

print(residence_area)

# Second Method :
residence_area = txt.split('from ')[1]
print(residence_area)


#5)Write a Python program that takes a user input string and prints it in reverse order.

user_input = input("Insert here :")

print(user_input[::-1])

# 6)Write a Python program that counts the number of vowels in a given string.

# First Method :
txxt=input("Enter a sentence: ")
low = txxt.lower()
a_cnt = low.count("a")
e_cnt = low.count("e")
i_cnt = low.count("i")
o_cnt = low.count("o")
u_cnt = low.count("u")

total_vowel_cnt = a_cnt+e_cnt+i_cnt+o_cnt+u_cnt
print(total_vowel_cnt)

# Second method:
text = input("Enter a word or sentence: ")

total_vowels = sum([text.count(vowel) for vowel in "aeiouAEIOU"])

print(f"Total number of vowels: {total_vowels}")


# 7)Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = input("Enter numbers separated by spaces: ")

num_list = [int(num) for num in numbers.split()]

max_value = max(num_list)

print(f"The maximum value is: {max_value}")

# 8)Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Enter a word: ")

word = word.lower()

if word == word[::-1]:
 print("The word is a palindrome!")
else:
 print("The word is not a palindrome.")

#9)Write a Python program that extracts and prints the domain from an email address provided by the user.   

email = input("Email here:")

domain = email.split("@")[1]

print(domain)

#10)Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

# Fixed password length
password_length = 10

# Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for _ in range(password_length))

print(f"Your random password is: {password}")
