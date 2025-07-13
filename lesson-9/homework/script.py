# 1)Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class CircleClass:
    
    def __init__(self, radius=int):
        self.radius = float(radius)
    
    def perimeter(self):
        result  = 2 * math.pi * self.radius
        print(f"Perimeter of the circle is {result: .2f}")
    
    def area_of_circle(self):
        result = math.pi * (self.radius * self.radius)
        print(f"The area of circle is {result: .2f}")

circle = CircleClass(5)

circle.area_of_circle()
circle.perimeter()


# 2)Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime, date
class Person:
    def __init__(self, name , country, DOB):
        self.name = name
        self.country = country

        if isinstance(DOB, date):
            self.DOB = DOB
        elif isinstance(DOB, str):
            try:
                self.DOB = datetime.strptime(DOB, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("DOB must be in YYYY-MM-DD format")
        else:
            raise TypeError("DOB must be a date object or string (YYYY-MM-DD)")
    def get_age(self):
        today = date.today()
        age = today.year - self.DOB.year

        if (today.month, today.day) < (self.DOB.month, self.DOB.day):
          age -= 1
          return age

person_1 = Person('Anna', 'USA', '2000-12-23')

print(person_1.name)
print(person_1.country)
print(person_1.DOB)
print(person_1.get_age())

# 3)Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
   def __init__(self, first_num: int, second_num: int):
       self.first_num = int(first_num)
       self.second_num = int(second_num)
   def addition(self):
       result = self.first_num + self.second_num
       return result
   def substraction(self):
       result = self.first_num - self.second_num
       return result
   def multiplication(self):
       result = self.first_num * self.second_num
       return result
   def devision(self):
       result = self.first_num / self.second_num
       return result
   def floor_devision(self):
       result = self.first_num // self.second_num
       return result 
   def modulus(self):
       result = self.first_num % self.second_num
       return result
   def exponentiation(self):
       result = self.first_num ** self.second_num
       return result

instance_ = Calculator(10, 3)

print(instance_.addition())
print(instance_.substraction())
print(instance_.multiplication())
print(instance_.devision())
print(instance_.floor_devision())
print(instance_.modulus())
print(instance_.exponentiation())

# 4)Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
import math

class Shapes:
    def __init__(self):
        pass


class Circle(Shapes):  # Fixed typo in class name
    def __init__(self, radius):  # Removed unused shape parameter        
        self.radius = float(radius)
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shapes):
    def __init__(self, side_a, side_b, side_c):  # Removed unused shape parameter
        self.side_a = float(side_a)
        self.side_b = float(side_b)
        self.side_c = float(side_c)            
    
    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s-self.side_a) * (s-self.side_b) * (s-self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Square(Shapes):
    def __init__(self, side):  # Removed unused shape parameter
        self.side = float(side)
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4


# Testing
circle_1 = Circle(4)
circle_2 = Circle(5)
triangle_1 = Triangle(5, 5, 6)
triangle_2 = Triangle(10, 7, 9)
square_1 = Square(5)
square_2 = Square(3)

print("Circle 1 Area:", circle_1.area())  # 50.26548245743669
print("Circle 1 Perimeter:", circle_1.perimeter())  # 25.132741228718345
print("Circle 2 Area:", circle_2.area())  # 78.53981633974483
print("Circle 2 Perimeter:", circle_2.perimeter())  # 31.41592653589793
print("Triangle 1 Area:", triangle_1.area())  # 12.0
print("Triangle 1 Perimeter:", triangle_1.perimeter())  # 16.0
print("Triangle 2 Area:", triangle_2.area())  # 30.59411708155671
print("Triangle 2 Perimeter:", triangle_2.perimeter())  # 26.0
print("Square 1 Area:", square_1.area())  # 25.0
print("Square 1 Perimeter:", square_1.perimeter())  # 20.0
print("Square 2 Area:", square_2.area())  # 9.0
print("Square 2 Perimeter:", square_2.perimeter())  # 12.0


# 5) Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.count = 1  # Track duplicates
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value == node.value:
            node.count += 1  # Duplicate found: increment count
        elif value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def print_tree(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(f"{node.value} (count={node.count})", end=" -> ")
            self._print_inorder(node.right)

# Test the BST
bst = BST()
numbers = [10, 15, 9, 16, 13, 20, 26, 30, 1, 43, 8, 7, 7]  # Note: 7 is inserted twice

for num in numbers:
    bst.insert(num)

print("In-order traversal (with counts):")
bst.print_tree()  # Output: 1 (count=1) -> 7 (count=2) -> 8 (count=1) -> ... 

print("\n\nSearch for 7:", bst.search(7))  # Output: True
print("Search for 99:", bst.search(99))  # Output: False


# 6)Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []  # Start with an empty list

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove from the top 
        else:
            print("Can't pop! Stack is empty.")  # No books left!

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Look at the top book
        else:
            print("Stack is empty!")  # Nothing to see

    def is_empty(self):
        return len(self.items) == 0  # Are there books? True/False

    def size(self):
        return len(self.items)  # Count how many books
    
elements = Stack()

elements.push('stone')
elements.push('paper')
elements.push('lemon')
elements.push('money')

print(elements.peek())
elements.pop()
print(elements.peek())

#7)Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("Stop")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

# Let's play!
hunt = LinkedList()
hunt.insert_at_start("Check the garden")
hunt.insert_at_start("Look under the tree")
hunt.insert_at_start("Dig near the rock")
hunt.display()  # Dig → Look → Check → Stop
hunt.delete("Look under the tree")
hunt.display()  # Dig → Check → Stop

#8)Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Format: {"item": {"quantity": X, "price": Y}}
    
    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"quantity": quantity, "price": price}
    
    def remove_item(self, item, quantity = 1):
        if item in self.items:
            self.items[item]["quantity"] -= quantity
            if self.items[item]["quantity"] <= 0:
                del self.items[item]
        else:
            print("this item is not in your shopping cart")

    def total_price(self):
        total = 0
        for item_data in self.items.values():
            total += item_data["quantity"] * item_data["price"]
        return total  # Returns 5.5

# Usage
cart = ShoppingCart()
cart.add_item("apple", price=1.5, quantity=3)
cart.add_item("banana", price=0.5, quantity=2)
cart.add_item("orange", price=1.5, quantity=5)
cart.add_item("orange", price=1.5, quantity=2)
cart.add_item("baking soda", price=3.5, quantity=5)
cart.add_item("pre-workout", price=0.2, quantity=3)
cart.remove_item('pre-workout',3)
print(f"Total: ${cart.total_price():.2f}")  

# 9)Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.



class Stack:
    def __init__(self):
        self.items = []  # Start with an empty list

    def push(self, item):
        self.items.append(item)  

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove from the top 
        else:
            print("Can't pop! Stack is empty.")  # No books left!

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Look at the top book
        else:
            print("Stack is empty!")  # Nothing to see

    def is_empty(self):
        return len(self.items) == 0  # Are there books? True/False

    def display_items(self):
        return self.items    
elements = Stack()

elements.push('stone')
elements.push('paper')
elements.push('lemon')
elements.push('money')
elements.pop()
print(elements.display_items())


# 10)Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
        
    def enqueue(self, person):
        if not  person in self.items:
            self.items.append(person)
        else:
            print(f"This person ({person}) is already in the queue !")
    
    def dequeue(self):
        served_customer = self.items.pop(0)
        print(f"{served_customer} has been served")
        return served_customer
    
    def display(self):
        return(self.items)
    
new_restaurant_queue = Queue()

print(new_restaurant_queue.display())
new_restaurant_queue.enqueue('Bobur')
new_restaurant_queue.enqueue('Xonzoda')
new_restaurant_queue.enqueue('Xorazshoh')
new_restaurant_queue.enqueue('Ozoda')
new_restaurant_queue.dequeue()
print(new_restaurant_queue.display())


#11)Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

from datetime import datetime
class BankAccount:
    
    def __init__(self, customer_id, first_name: str, last_name: str, balance: int = 0):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.transactions = []  # Stores transaction history

    def __str__(self):
        return f"Account(ID={self.customer_id}, Name={self.first_name} {self.last_name}, Balance=${self.balance})"

    def add_transaction(self, amount, description):
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "description": description,
            "balance_after": self.balance + amount
        }
        self.transactions.append(transaction)
        self.balance += amount  # Update balance

    def deposit(self, amount):
            if amount > 0:
                self.add_transaction(amount, "Deposit")
            else:
                raise ValueError("Deposit amount must be positive!")

    def withdraw(self, amount):
            if amount > 0:
                if self.balance >= amount:
                    self.add_transaction(-amount, "Withdrawal")
                else:
                    raise ValueError("Insufficient funds!")
            else:
                raise ValueError("Withdrawal amount must be positive!")

class Bank:
    def __init__(self):
        self.accounts = []  # This will store BankAccount objects
    
    def add_account(self, customer_id, first_name: str, last_name: str, balance: int = 0):
        for account in self.accounts:
            if account.customer_id == customer_id:
                raise ValueError(f"ID {customer_id} exists!")

        new_account = BankAccount(customer_id, first_name, last_name, balance)
        self.accounts.append(new_account)
    
    def remove_account(self, customer_id):
        for i, account in enumerate(self.accounts):
            if account.customer_id == customer_id:
                removed_account = self.accounts.pop(i)
                print(f"Account with ID {customer_id} Has been removed !!")
        
    def get_account(self, customer_id):
        """Returns the account with the given ID or None if not found"""
        for account in self.accounts:
            if account.customer_id == customer_id:
                return account
        

# Usage
bank = Bank()  # Create one bank instance

bank.add_account(1, 'Hilola', "Abdug'aniyeva", 250)
bank.add_account(2, 'Halil', "Abdug'aniy", 7000)
bank.add_account(3, 'Lola', "Yuldasheva", 250)
bank.add_account(4, 'Ali', "Aliev", 7000)
bank.remove_account(1)
accountt = bank.accounts[2]

# Perform transactions
accountt.deposit(500)
accountt.withdraw(200)
accountt.deposit(1000)
accountt.balance

print(accountt)



