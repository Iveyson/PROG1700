
#Step 1: Create your first list
"""
movies = ["The Matrix", "Blade Runner", "Bullet Train", "Good Will Hunting",  "Saving Private Ryan"]
print(movies)
print(movies[0],", ", movies[4])

#challenge
movies[2] = "The Green Mile"
print(movies)
"""
#Step 2: Reading and Accessing Data
"""""
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
print(numbers[3:])
print(len(numbers))
x=0
y=0
while y == 0:
    print(numbers[x])
    x = x + 1
    if x == len(numbers):
        y = y+1
    else:
        pass
"""

#Step 3: Real-World Example- Grocery Inventory
""""
inventory = ["milk", "bread", "eggs"]
inventory.append("butter")
inventory.append("cheese")
print(inventory)
inventory.insert(0, "apples")
print(inventory)
inventory[2] = "whole grain bread"
print(inventory)
#inventory.remove("eggs")
inventory.pop(3)
print(inventory)
print(len(inventory))
"""
#Step 4: To-Do List Manager (Mini Exercise)
""""
tasks = []
x = 0
y = 0
z = "0"
while y == 0:
    print("What would the user like to do to the list")
    print("Enter 1 to add a task")
    print("Enter 2 to remove a task")
    print("Enter 3 to view tasks")
    print("Enter 4 to exit")
    x=int(input("Enter Here: "))
    if x == 1:
        z=input("Enter The Task you would like added to the list: ")
        tasks.append(z)
        print(tasks)
        print("Is there anything else you would like to do?")
    elif x == 2:
        print("What would you like to remove from the list?")
        z = int(input("Enter the position of the item you would like removed: "))
        tasks.pop(z)
        print(tasks)
        print("Is there anything else you would like to do?")
    elif x == 3:
        print(tasks)
        print("Is there anything else you would like to do?")
    elif x == 4:
        print("Have a great day and good luck on those tasks!")
        y= y+1
    else:
        print("Invalid input Try again")
"""

"""
Reflection:
1. What is one real-world use of lists you can think of in your life or work?
   A good real world use of lists would be like a spotify play list. You can add and remove songs and order them.

2. Which list operation (Create, Read, Update, Delete) do you find easiest or hardest, and why?
   I find the delete to be the most difficult since you have a couple different ways to do it that are completely different from eachother.

3. How would you explain the concept of indexing to someone new to Python?
   Indexing is like counting and then subtracting 1 from it to get the correct number.
"""       
