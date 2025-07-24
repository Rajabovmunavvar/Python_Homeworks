#Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days

import datetime


from datetime import datetime

def main():
    print("=== Age Calculator ===")
    
    
    while True:
        try:
            birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
            birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
            
            if birth_date > datetime.now():
                print("Error: Birthdate cannot be in the future!")
                continue
            
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD (e.g., 2000-12-31).")
    
    today = datetime.now()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1

        last_day_of_prev_month = (today.replace(day=1) - timedelta(days=1)).day
        days += last_day_of_prev_month
    
    if months < 0:
        years -= 1
        months += 12
    
    # Print result
    print(f"\nYour age is: {years} years, {months} months, and {days} days")

if __name__ == "__main__":
    from datetime import timedelta  # Only needed for days adjustment
    main()



# 2) Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
import datetime

def day_till_next_birthday():
    while True:
        try:
            str_birthday = input("Please enter your birthday in YYYY-MM-DD format: ")
            birthday = datetime.datetime.strptime(str_birthday, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD (e.g., 2000-12-31).")

    today = datetime.datetime.now()
    
    # Get day of year for both dates
    today_day = int(today.strftime("%j"))
    bday_day = int(birthday.strftime("%j"))
    
    # Calculate days remaining (fixed logic)
    if today_day < bday_day:
        days_left = bday_day - today_day
    else:
        # Handle leap year for the +365 part
        next_year = today.year + 1
        is_leap = (next_year % 400 == 0) or (next_year % 100 != 0 and next_year % 4 == 0)
        days_left = (366 if is_leap else 365) - today_day + bday_day
    
    print(f"{days_left} days left until your next birthday!")

day_till_next_birthday()

# 3)Meeting Scheduler: Ask the user to enter date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

def meeting_scheduler():
    while True:
        try:
            # Input meeting start date and time
            str_date = input("Enter the meeting date (YYYY-mm-dd): ")
            str_time = input("Enter the start time (HH:MM): ")
            
            # Input meeting duration
            str_duration = input("Enter the duration (HH:MM): ")
            
            # Parse inputs
            meeting_date = datetime.strptime(str_date, "%Y-%m-%d")
            start_time = datetime.strptime(str_time, "%H:%M")
            duration = datetime.strptime(str_duration, "%H:%M")
            
            # Combine date and start time
            start_datetime = datetime.combine(meeting_date.date(), start_time.time())
            
            # Create duration as timedelta
            duration_td = timedelta(hours=duration.hour, minutes=duration.minute)
            
            # Calculate end time
            end_datetime = start_datetime + duration_td
            
            # Format and print results
            print(f"\nMeeting starts at: {start_datetime.strftime('%Y-%m-%d %H:%M')}")
            print(f"Meeting ends at:   {end_datetime.strftime('%Y-%m-%d %H:%M')}")
            break
            
        except ValueError:
            print("Invalid format. Please use YYYY-mm-dd for date and HH:MM for time/duration.\n")

# Run the scheduler
meeting_scheduler()

# 4)Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.


import datetime
from zoneinfo import ZoneInfo
def timezone_converter():
    while True:
        try:
            # input section
            user_datetime =input("enter date and time in YYYY-mm-dd HH:MM format ")
            user_timezone = input("enter your time zone in Asia/Tokyo format ")
            wished_timezone = input("Enter the timezone you wish to see in Asia/Tokyo format")
            user_datetime = datetime.datetime.strptime(user_datetime, "%Y-%m-%d %H:%M")
            user_tz = ZoneInfo(user_timezone)
            localized_time_of_user = user_datetime.replace(tzinfo=user_tz)
            wished_tz = ZoneInfo(wished_timezone)
            user_wished_time = localized_time_of_user.astimezone(wished_tz)

            print(f"Original Time : {localized_time_of_user} in {user_timezone} timezone")
            print(f"Converted Time : {user_wished_time} in {wished_timezone} timezone")

            break

        except ValueError as e:
            print(f"\nError: {e}")
            print("Please check:")
            print("- Date format (YYYY-mm-dd HH:MM)")
            print("- Valid timezone names (e.g. 'Asia/Tokyo')")
            print("Try again...\n")
        except KeyError:  
            print("\nInvalid timezone. Use format like 'Asia/Tokyo'. See: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            print("Please try again...\n")
       
timezone_converter()



# 5 )Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

import datetime
import time

def countdown_timer():
    while True:  
        try:
            
            time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            target_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            
            
            while True:
                now = datetime.datetime.now()
                if target_time <= now:
                    print("\nCountdown finished! 🎉")
                    return  
                
                remaining = target_time - now
            
                print(f"Time remaining: {remaining}", end="\r", flush=True)
                time.sleep(1)
                
        except ValueError:
            print("\nInvalid format! Please use YYYY-MM-DD HH:MM format.")
        except KeyboardInterrupt:
            print("\nCountdown stopped by user.")
            return
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            return

countdown_timer()


# 6)Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

# Valid Email Example :

# bittrade2003@gmail.com

# all charracter are in lowercase
# email must start with letter , not number
# before @ sign, letter and numbers can be used
# after @ sign , there must be at one or more charters but not numbers or special characters 
# and there must a dot 
# and com/ru/net ....

import re
email = input("Please enter your email here: ")


if re.match("^[a-z0-9]+@[a-z]+[.][a-z]+$", email):
    print("ok")
    print(email)
else:
    print("not ok")


# 7)Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re


def formatter():
    while True:
        phone_num = input("enter your phone number here: ")
        if re.match("^[0-9]{10}$",phone_num) :
            new = re.sub("([0-9]{3})([0-9]{3})([0-9]{4})","(\\1) \\2-\\3",phone_num)
            print(new)
            break
        else:
            print("Please enter valid phone number !")


formatter()

# 8)Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

# minimum length : 8 

import re

def pass_checker():
    while True:
        password = input("Please enter your password here: ")

        if len(password) >=8 and re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search("[0-9]",password):
            print("Password is valid 1")
        else:
            print("Your password does not meet required creteries ! ")

pass_checker()

# 9)Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
import re

def word_finder():
    while True:
        word = input("Please enter the word you want to search for: ")
        word = word.lower()
        sample_text = "banana apple kiwi lemon hit kiwi lemon apple banana lemon qwerty apple look sin like peach love kiwi lemon"

        print(re.findall(word, sample_text.lower()))
        break

word_finder()

# 10)Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re 
def date_extractor():
    while True:
        given_text = input("Please enter your text here:")

        print(re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", given_text))
        break


date_extractor()
