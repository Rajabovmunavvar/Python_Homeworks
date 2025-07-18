# Homework 1. ToDo List Application

# Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
# Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.


class TaskClass:
    def __init__(self, task_id: int, task_title: str, description: str, due_date):
        self.task_id = task_id
        self.task_title = task_title
        self.description = description  
        self.due_date = due_date
        self.status = "Not Done Yet"
    
    def __str__(self):
        return (f"ID: {self.task_id}\n"
                f"Title: {self.task_title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n"
                "------------------")

class ToDoListClass:
    def __init__(self):
        self.task_lists = []

    def add_task(self, task_id: int, task_title: str, description: str, due_date):
        new_task = TaskClass(task_id, task_title, description, due_date)
        self.task_lists.append(new_task)   

    def task_done(self, task_id):
        for task in self.task_lists:
            if task.task_id == task_id:
                task.status = "Completed"
                print(f"\nTask with ID {task_id} has been completed!")
                return
        print(f"\nTask with ID {task_id} not found!")

    def display_all_tasks(self):
        print("\n=== ALL TASKS ===")
        if not self.task_lists:
            print("No tasks found!")
            return
        for task in self.task_lists:
            print(task)

    def display_incomplete(self):  
        print("\n=== INCOMPLETE TASKS ===")
        incomplete_tasks = [task for task in self.task_lists if task.status == "Not Done Yet"]
        if not incomplete_tasks:
            print("No incomplete tasks!")
            return
        for task in incomplete_tasks:
            print(task)

# Testing the application
if __name__ == "__main__":
    todo = ToDoListClass()
    
    # Add tasks
    todo.add_task(1, 'Cleaning The Room', "Floor must be mopped and set things in order", '2025-08-19')
    todo.add_task(2, 'Washing The Dishes', "Especially wash those pots from last month!!", '2025-03-09')
    todo.add_task(3, 'Change Your car oil', "Do not buy cheap stuff", '2025-12-19')
    todo.add_task(4, 'Go to Groceries', "Don't forget to buy eggs and meat", '2025-10-08')
    
    # Mark some tasks as done
    todo.task_done(1)
    todo.task_done(2)
    
    # Display all tasks
    todo.display_all_tasks()
    
    # Display incomplete tasks
    todo.display_incomplete()


# #2)
# Define Post Class:
# Create a Post class with attributes like title, content, and author.
# Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
# Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
# Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
# Test the Application:
# Create instances of posts and test the functionality of your Blog system.


class PostClass:
    def __init__(self, post_id: int,  post_title: str, content: str, author):
     
        self.post_id = post_id
        self.post_title = post_title
        self.content = content  
        self.author = author
        
    
    def __str__(self):
        return (f"ID: {self.post_id}\n"
                f"Title: {self.post_title}\n"
                f"Content: {self.content}\n"
                f"author: {self.author}\n"
                "------------------")

def menu():
    post_bank = BlogClass()
    
    while True:
        print("\nBlog System")
        print("1. Add post")
        print("2. View all posts")
        print("3. View posts by author")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post_bank.add_post(title, content, author)
            print("Post added successfully!")
            
        elif choice == "2":
            posts = post_bank.display_all_posts()
            for post in posts:
                print(post)
                
        elif choice == "3":
            author = input("Enter author name to search: ")
            posts = post_bank.search_by_author(author)
            for post in posts:
                print(f"\nTitle: {post['title']}\nContent: {post['content']}")
                
        elif choice == "4":
            break
            
        else:
            print("Invalid choice, please try again.")

class BlogClass:
    def  __init__(self):
        self.all_posts = []
        self.next_id = 1 
    
    def add_post(self, post_title: str, content: str, author):
        new_post = PostClass( post_id=self.next_id, post_title=post_title, content=content, author=author)
        self.all_posts.append(new_post)
        self.next_id += 1

    def display_all_posts(self):
        if not self.all_posts:
            print("No Posts found!")
        for post in self.all_posts:
            print("\n=== All posts ===")
            print(post)

    def  search_by_author(self, author: str):
        for post in self.all_posts:
            if post.author == author:
                print(f"\n=== All posts by {author} ===")
                print(post)


        


post_bank = BlogClass()

post_bank.add_post("Dying creatures", "apgh wah f w aoieh hawoihfe fwklh awu  rhaw hfjeaa lawh","Ac Talib")
post_bank.add_post("The Sea", "apgh wah f w aoieh hawoihfe fwklh awu  rhaw hfjeaa lawh","Hatum Bino")
post_bank.add_post("Why we sleep ?", "apgh wah f w aoieh hawoihfe fwklh awu  rhaw hfjeaa lawh","La Akbariy")
post_bank.add_post("Retriving lost items", "apgh wah f w aoieh hawoihfe fwklh awu  rhaw hfjeaa lawh","Ac Talib")
print(post_bank.display_all_posts())
print(post_bank.search_by_author("Ac Talib"))


menu()



# Homework 3. Simple Banking System

# Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.
# Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
# Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.
# Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# Test the Application:
# Create instances of accounts and test the functionality of your Banking system.


class Account:
    def __init__(self, account_number: int, holder_name: str, balance: int):
        self.account_number = int(account_number)
        self.holder_name = holder_name
        self.balance = float(balance)

    def __str__(self):
        return (f"\n=== Account Details ==="
                f"\nAccount Number: {self.account_number}"
                f"\nHolder's Name: {self.holder_name}"
                f"\nAccount Balance: {self.balance:.2f}") 
    
    def __repr__(self):
        return self.__str__()  

class Bank:
    def __init__(self):
        self.all_accounts = []
    
    def add_account(self, account_number: int, holder_name: str, balance: int):  
        new_account = Account(int(account_number), holder_name, float(balance))
        self.all_accounts.append(new_account)
        print("New account has been added successfully!")
    
    def check_balance(self, holder_name: str, account_number: int):
        return [
            account for account in self.all_accounts
            if (account.holder_name.lower().strip() == holder_name.lower().strip() and  account.account_number == account_number)
        ]
    
    def deposit(self, holder_name: str, account_number: int, deposit_amount):
     for account in self.all_accounts:
        if account.holder_name.lower().strip() == holder_name.lower().strip() and account.account_number == account_number:
            print("\n=== DEPOSIT ===")
            print(f"\nHolder's Name: {account.holder_name}"
                  f"\nBalance Before: {account.balance: .2f}"
                  f"\nAdded Amount: {deposit_amount}")
            account.balance += float(deposit_amount)
            print(f"Balance After: {account.balance: .2f}")

    def withdraw(self, holder_name: str, account_number: int, withdraw_amount):  # Fixed parameter name
     for account in self.all_accounts:
        if account.holder_name.lower().strip() == holder_name.lower().strip() and account.account_number == account_number:
            if account.balance >= withdraw_amount:
                print("\n=== WITHDRAWAL ===")
                print(f"\nHolder's Name: {account.holder_name}"
                    f"\nBalance Before: {account.balance: .2f}"
                    f"\nWithdrawed Amount: {withdraw_amount}") 
                account.balance -= float(withdraw_amount)
                print(f"Balance After: {account.balance: .2f}")
            else:
                print("Withdrawal is decline! Unsufficiant Funds!")
    

def menu():
    bank = Bank()  

    bank.add_account(1001, "Ergashev Ravshan", 200.50)
    bank.add_account(1002, "Ergasheva Laylo", 150.70)
    bank.add_account(1003, "Botirov Qodir", 799.10)

    while True:
        print("\n=== Bank System ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n[Add New Account]")
            try:
                account_number = int(input("Account Number: "))
                holder_name = input("Holder's Name: ")
                balance = float(input("Balance: "))
                bank.add_account(account_number, holder_name, balance)
            except ValueError:
                print("Invalid input! Please enter numbers for account number and balance.")
        
        elif choice == "2":
            holder_name = input("Holder's Name: ")
            try:
                account_number = int(input("Account Number: "))
                accounts = bank.check_balance(holder_name, account_number)
                if accounts:
                    print("\n=== Account Found ===")
                    for account in accounts:
                        print(account)  
                else:
                    print("\nAccount not found!")
            except ValueError:
                print("Invalid account number!")
        
        elif choice == "3":
            holder_name = input("Holder's Name: ")
            try:
                account_number = int(input("Account Number: "))
                deposit_amount = float(input("Deposit Amount Here: "))
                accounts = bank.deposit(holder_name, account_number, deposit_amount)
                if accounts:
                    print("\n=== Account Found ===")
                    for account in accounts:
                        print(account)  
                
            except ValueError:
                print("Invalid account number!")

        elif choice == "4":
            holder_name = input("Holder's Name: ")
            try:
                account_number = int(input("Account Number: "))
                deposit_amount = float(input("Deposit Amount Here: "))
                accounts = bank.withdraw(holder_name, account_number, deposit_amount)
                if accounts:
                    print("\n=== Account Found ===")
                    for account in accounts:
                        print(account)  
                
            except ValueError:
                print("Invalid account number!")
        

        elif choice == "5":
            print("Goodbye! Qulpiddin :)")
            break
menu()




        
