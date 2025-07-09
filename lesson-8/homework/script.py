# 1)Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

num = 3
devid = int(input("insert the number here: "))

try:
    result = num/devid
    print(result)
except ZeroDivisionError:
    print("you cannot insert number 0, it gives an error !")
else:
    print("Done successfully !")


# 2)Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.


num = 3

try:
    devid = int(input("insert the number here: "))
    result = num/devid
    print(result)
except ValueError:
    print("you cannot insert str , it gives an error !")
else:
    print("Done successfully !")

# 3)Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open('new.txt') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file you looking for does not exist !")
else:
    print("file found successfully !")


# 4)Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    n_1 = input("n1 : ")
    n_2 = input("n2 : ")
    
    # Try converting both to numbers
    try:
        n_1 = float(n_1)
        n_2 = float(n_2)
    except ValueError:
        raise TypeError("Non-numeric input")
    
    result = n_1 + n_2
    print(result)
    
except TypeError:
    print("Error: Both inputs must be numbers!")
except ValueError:
    print("Error: Invalid number format (use digits like 5 or 3.14)")
else:
    print("Done successfully!")

# 5)Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open('new.txt') as needed_file:
        data_inside = needed_file.read()
        print(data_inside)
except PermissionError:
    print("The file('new.txt') is not accessible, you got no permission to open it !")
else:
    print("Has opened the file successfully !")

# 6) Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

lst =[1, 5, 8, 9, 11]

try:
    print(lst[5]+10)
except IndexError:
    print(f"Index you entered is out of range - valid indices are 0 to {len(lst)-1} for this list")

# 7)Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:

    number_1 = int(input("insert the first number here: "))
    number_2 = int(input("insert the second number here: "))
    print(number_1 + number_2)

except KeyboardInterrupt:
    print("\nyou manually interrupted the loop")

# 8)Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    result = 9 * 9 / (0 * 0) 
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ArithmeticError:
    print("An arithmetic error occurred!")

# 9)Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    with open('new.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    print("Error: Failed to decode with UTF-8. Trying fallback encoding...")

#10)Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    i = 31413
    i.append(5)
except AttributeError:
    print(f"Error: {type(i)} objects don't support 'append' operations")

# Python File Input Output: Exercises, Practice, Solution

# 1)Write a Python program to read an entire text file.

try:
    with open('new.txt', 'r') as needed_file:
        content = needed_file.read()

    print(content)
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")

# 2)Write a Python program to read first n lines of a file.
 
try:
    with open('new.txt', 'r') as needed_file:
        n = int(input("Enter number of lines to read: "))
        if n <= 0:
            print("Error: 'n' must be a positive integer")
        else:
            cnt = 0
            for line in needed_file:  # Reads line-by-line (memory efficient)
                print(line.strip())
                cnt += 1
                if cnt == n:
                    break
            if cnt < n:
                print(f"Warning: File has only {cnt} lines (requested {n})")

except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")
except ValueError:
    print("Error: Please enter a valid integer for 'n'")

# 3)Write a Python program to append text to a file and display the text.


try:
    with open('new.txt', 'a') as thefile:
        thefile.write("\nThe new line here")
    with open('new.txt', 'r') as thefile:
        text_ =thefile.read()
        print(text_)

except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")

# 4)Write a Python program to read last n lines of a file.

try:
    with open('new.txt', 'r') as needed_file:
        n = int(input("Enter number of lines to read: "))
        if n <= 0:
            print("Error: 'n' must be a positive integer")
            
        else:
            window = []  # Stores the last N lines
            for line in needed_file:
                window.append(line)
                if len(window) > n:  # Remove the oldest line
                    window.pop(0)
        for line in window:
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")
except ValueError:
    print("Error: Please enter a valid integer for 'n'")


# 5)Write a Python program to read a file line by line and store it into a list.

try:
    lst = []
    with open('new.txt', 'r') as needed_file:
        for line in needed_file:
            lst.append(line.strip())
    print(lst)
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")


# 6)Write a Python program to read a file line by line and store it into a variable.

try:
    with open('new.txt', 'r') as file:
        file_content = file.read()  # Stores ALL text in one string
    print("File content stored in variable:")
    print(file_content)  # \n marks line breaks
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")

# 7)Write a Python program to read a file line by line and store it into an array.

import array
try:
    empty_array = array.array('i')
    with open('new.txt', 'r') as file:
        for items in file:
            items = int(items)
            empty_array.append(items)
        print(empty_array)
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Could not read file")


# 8)Write a Python program to find the longest words in the file

try:
    longest = None
    with open("new.txt", 'r') as file:
        for line in file:
            words = line.strip().split()  # Split into words, remove \n
            if not words:  # Skip empty lines
                continue
            # Find shortest word in current line
            current_longest = max(words, key=len, default=None)
            # Update global shortest
            if (longest is None) or (len(current_longest) > len(longest)):
                longest = current_longest
    print(longest)
except FileNotFoundError:
    print("Error: File not found")
    
# 9)Write a Python program to count the number of lines in a text file.

try:
    with open("new.txt", 'r') as file:
        number_of_lines = sum(1 for line in file)
        print(f"Number of lines in the file: {number_of_lines}")

except FileNotFoundError:
    print("Error: File not found")

# 10)Write a Python program to count the frequency of words in a file.

try:
    import string
    word_counts = {}
    with open('new.txt', 'r') as thefile:
        for line in thefile:
            words = line.strip().split()
            for word in words:
                word = word.lower().strip(string.punctuation)
                if word in word_counts:
                      word_counts[word] += 1
                else:
                      word_counts[word] = 1
        print(word_counts)

except FileNotFoundError:
    print("Error: File not found")



# 11)Write a Python program to get the file size of a plain file.

import os

file_path = 'new.txt'

if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    print(f"File size: {size} bytes")
else:
    print("File not found")

# 12)Write a Python program to write a list to a file.

try:
    lst = ['ABUBAKR', 'LILOLA', 'AHMED']
    with open('new.txt', 'w') as thefile:
        for words in lst:
            thefile.write(words + '\n')
    with open('new.txt') as thefile:
        content = thefile.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found")

# 13)Write a Python program to copy the contents of a file to another file.

try:
    with open('new.txt') as thebase_file:
        content = thebase_file.read()
    with open('copy.txt', 'w') as copy_file:
        copy_file.write(content)
    with open('copy.txt', 'r') as copy_file:
        copy_content = copy_file.read()
    print(copy_content)

except FileNotFoundError:
    print("Error: File not found")

# 14)Write a Python program to combine each line from the first file with the corresponding line in the second file.

try:
    with open('new.txt') as thebase_file:
        content = thebase_file.readlines()
    with open('copy.txt') as copy_file:
        copy_content = copy_file.readlines()
    for line, copy_line in zip(content, copy_content):
        print(line.strip() + ' ' + copy_line.strip())

except FileNotFoundError:
    print("Error: File not found")

# 15)Write a Python program to read a random line from a file.

import random

try:
    with open('new.txt') as f:
        lines = f.readlines()

    if lines:
        random_line = random.choice(lines)
        print("Random line:", random_line.strip())
    else:
        print("The file is empty.")

except FileNotFoundError:
    print("Error: File not found")


# 16)Write a Python program to assess if a file is closed or not.

try:
    with open('new.txt') as f:
        print(f.closed)  #  False (inside block)

    print(f.closed)  #  true (outside the block)

except FileNotFoundError:
    print("Error: File not found")

# 17)Write a Python program to remove newline characters from a file.

try:
    with open('new.txt') as f:
        line = f.read().replace('\n',' ')
        print(line)

except FileNotFoundError:
    print("Error: File not found")

# 18)Write a Python program that takes a text file as input and returns the number of words in a given text file.
import re

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            # Use regex to find all word-like patterns
            words = re.findall(r"[a-zA-Z0-9'-]+", text)
            return len(words)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"

# Example usage
filename = input("Enter file path: ")
print(f"Total words: {count_words(filename)}")

# 19)Write a Python program to extract characters from various text files and put them into a list.

def files_combine_list(*args):
    try:
        with open('firstfile.txt') as file_1:
            content = file_1.read()
            line_1 = list(content)
        with open('secondfile.txt') as file_2:
            content2 = file_2.read()
            line_2 = list(content2)
        needed_list = line_1 + line_2     
        return needed_list
    except FileNotFoundError:
        print("Error: File not found")    

print(files_combine_list('firstfile.txt', 'secondfile.txt'))


# 20)Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
a_z = map(chr, range(65, 91))
txt = '.txt'

for letter in a_z:
    new_file = letter + txt
    open(new_file, 'w').close()

# 21)Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

a_z = list(map(chr, range(65, 91)))

try:
    spec_num = int(input('inser a number here: '))
    with open('new_file.txt', 'w') as n_f:
        cnt = 0
        for letter in a_z:
            n_f.write(letter+' ')
            cnt += 1
            if cnt == spec_num:
                n_f.write('\n')
                cnt = 0

except FileNotFoundError:
    print("Error: File not found")

    
