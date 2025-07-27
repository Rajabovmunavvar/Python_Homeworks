# 1)write a Python script that reads the students.jon JSON file and prints details of each student.

import json

with open("students.json") as f:
    data = json.load(f)
    
    print("Student Details:")
    print("=" * 50)
    
    for student in data['students']:
        print(f"\nID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        
        
        print("\nSubjects:")
        for subject in student['subjects']:
            print(f"  - {subject}")
            
        print("\nAddress:")
        address = student['address']
        print(f"  Street: {address['street']}")
        print(f"  City: {address['city']}")
        print(f"  Zipcode: {address['zipcode']}")
        
        print("=" * 50)


# 2)Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).



import requests
city = 'Tashkent'
api_key = '7cdd4fbcdc0b83002f014c277e5cbb15'
units = 'metric'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'

response = requests.get(url)

my_data = response.json()
name = my_data['name']
temperature = my_data['main']['temp']
humidity = my_data['main']['humidity']
print(f"in {name}, temperature is {temperature} and humidity is {humidity}")


# 3)Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json
book_id = int(input("Kitobni idsini kiriting: "))
name = input("Kitobni nomini kiriting: ")
author = input("Muallif nomini kiriting: ")

my_dict = {'book_id':book_id, 'name':name, 'author_name':author}

with open('library.json') as f:
    my_data = json.load(f)
    
for ls in  my_data.values():
    ls.append(my_dict)

with open('library.json','w') as f:
   json.dump(my_data, f, indent=2)


# 4)Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random
user_input = input("Kino nomini bir qismini kiriting")
api_key = 'f5d43806'
url = f'http://www.omdbapi.com/?apikey={api_key}&s={user_input}'

response = requests.get(url)

data = response.json()

for movie in data['Search']:
    title = movie['Title']
    year = movie['Year']
    type = movie['Type']
    print(f'Title: {title}, Year: {year}, Type: {type}')


    
