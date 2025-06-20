#Given a side of square. Find its perimeter and area.

side_of_square = float(input("side_length : "))

parameter = 4 * side_of_square
area = side_of_square ** 2

print(parameter)
print(area)

#Given diameter of circle. Find its length.

diameter = float(input('diameter : '))

length = diameter * 3.1416

print(length)

#Given two numbers a and b. Find their mean.

a = float(input('a : '))
b = float(input('b : '))

mean = (a+b)/2

print(mean)

#Given two numbers a and b. Find their sum, product and square of each number.

a = float(input('a : '))
b = float(input('b : '))

sum_of_numbers = a + b
product_of_numbers = a * b
square_of_a = a ** 2
square_of_b = b ** 2


print("Sum:", sum_of_numbers)
print("Product:", product_of_numbers)
print("Square of a:", square_of_a)
print("Square of b:", square_of_b)
