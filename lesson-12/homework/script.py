# Homework:

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.


import threading

def find_primes_in_range(start, end, result_list):
    """Finds primes between `start` and `end` and appends to result_list."""
    primes = []
    for num in range(max(2, start), end + 1):
        if num > 2 and num % 2 == 0:
            continue
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    result_list.extend(primes)  # Add found primes to shared list

# Shared list to store results
prime_results = []

# Create threads with shared result list
task_1 = threading.Thread(target=find_primes_in_range, args=(1, 100, prime_results))
task_2 = threading.Thread(target=find_primes_in_range, args=(101, 200, prime_results))
task_3 = threading.Thread(target=find_primes_in_range, args=(201, 300, prime_results))

# Start threads
task_1.start()
task_2.start()
task_3.start()

# Wait for all threads to complete
task_1.join()
task_2.join()
task_3.join()

# Print sorted results
print(sorted(prime_results))


# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading


def occurance_finder(file_name: str, start: int, end: int, word_keeper: dict, lock ):
    dict = {}
    with open(file_name, "r") as f:
        content = f.readlines()
        for line_number,line in enumerate(content):
            if (start-1) <= line_number <= (end-1):
                for word in line.split():
                    if word not in dict:
                        dict[word] = 1
                    else:
                        dict[word] += 1
                        
    with lock:
        for word, count in dict.items():
            word_keeper[word] = word_keeper.get(word, 0) + count
            
lock = threading.Lock()  
word_keeper = {}

task_one = threading.Thread(target=occurance_finder, args=("text.txt", 1, 150, word_keeper, lock))
task_two = threading.Thread(target=occurance_finder, args=("text.txt", 151, 300, word_keeper, lock))
task_three = threading.Thread(target=occurance_finder, args=("text.txt", 301, 450, word_keeper, lock))
task_four = threading.Thread(target=occurance_finder, args=("text.txt", 451, 600, word_keeper, lock))

task_one.start()
task_two.start()
task_three.start()
task_four.start()

task_one.join()
task_two.join()
task_three.join()
task_four.join()

print(word_keeper)



