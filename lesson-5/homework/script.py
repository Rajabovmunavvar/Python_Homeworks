# 1)
# A year is a leap year if:
# - It is divisible by 4, and
# - It is NOT divisible by 100, unless it is also divisible by 400.

# Parameters:
# year (int): The year to be checked.

# Returns:
# bool: True if the year is a leap year, False otherwise.
# """
# if not isinstance(year, int):
#     raise ValueError("Year must be an integer.")

# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

leap_year = input("insert year here:")
       
if leap_year.isdigit():
    leap_year = int(leap_year)
    if (leap_year%4 == 0 and leap_year%100 != 0) or (leap_year%400 == 0):
        print("True")
    else:
        print("False")
else:
    print("Year must be an integer")
#  2)Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n = int(input("Insert a number here:"))

if n % 2 == 1:
    print("Weird")
else:  # n is even
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
# 3)Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

a = int(input("insert a: "))
b = int(input("insert b: "))

# first solution (with if-else):
start = a if a % 2 == 0 else a + 1
end = b if b % 2 == 0 else b - 1

even_numbers = list(range(start, end + 1, 2))
print(even_numbers)


# second solution (without if-else):

a = int(input("insert a: "))
b = int(input("insert b: "))

start = a + (a % 2)
end = b - (b % 2)

even_numbers = list(range(start, end + 1, 2))
print(even_numbers)
