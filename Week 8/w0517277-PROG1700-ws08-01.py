#A) Weather Report
"""
temperatures = [14, 16, 18, 17, 20, 19, 15]
restart_program=True
while restart_program ==True:
    add_temp=""
    while True:
        add_temp=input("Please Enter a temperature or enter quit: ")
        if add_temp.lower() == "quit":
            restart_program=False
            break
        elif add_temp.isdigit():
            temperatures.append(float(add_temp))
        else:
            continue
highest_value = 0
lowest_value = 100000
total = 0
count = 0
for temp in temperatures:
    if highest_value < temp:
        if temp >= 18:
            count+=1
        highest_value = temp
    elif lowest_value > temp:
        lowest_value = temp
    elif temp >= 18:
        count +=1
    total += temp

avg = total / len(temperatures)
temperature_set = set(temperatures)
print(f"This is the temperatures with no duplicates: {temperature_set}")
print(f"Average temperature: {avg}. The highest value is: {highest_value}. The lowest value is: {lowest_value}. These many days were above 18 {count}")
"""
#B) Library checkout log
"""
books = {
    "Python Basics": 3,
    "Web Design 101": 2,
    "Networking Made Easy": 1
}

while True:
    user_book=input("Enter the name of the book you would like to add (or type quit to continue): ")
    if user_book.lower()=="quit":
        break

    user_qty=input("Enter the ammount of that book you have: ")

    if user_qty.isdigit():
        user_qty=int(user_qty)
        if user_qty < 0:
            print("Invalid please input a positive number: ")
            continue
        books[user_book] = user_qty
    else:
        print("Invalid Input try again")
        continue
lowest_qty=float('inf')
least_book=""
total_books=0
for title, qty in books.items():
    if qty < lowest_qty:
        lowest_qty=qty
        least_book=title
    print(f"{title:25} copies: {qty}")
    total_books+= qty
print(f"and the book with the lowest on hand is {least_book} with {lowest_qty} copie(s).")
print(f"The total ammount of books in circulation is {total_books}")
"""
#C) Campus Cafe Sales
"""
items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]
while True:
    add_item=input("Please enter your item(or input quit to finish): ")
    if add_item.lower() == "quit":
        break
    add_sale=input("Please Input the price of the item: ")
    if add_sale.isdigit():
        add_sale=float(add_sale)
        if add_sale<0:
            print("Invalid Input try again")
            continue
        items.append(add_item)
        sales.append(add_sale)
    else:
        print("Invalid Input try again")
        continue
print(f"_______________________")
print("{:<10} → {:>10}".format("Items","Sales"))
for i in range(len(items)):
    print("{:<10} → {:>10}".format(items[i], sales[i]))
total=0
big_sale=0

max_sale = max(sales)
max_index = sales.index(max_sale)
best_selling_item = items[max_index]

for i in sales:
    total+=i
average=total/len(items)
unique_items=set(items)
print(f"the average of your sales is ${average} and your total is ${total}.The best selling item is {best_selling_item} The unique items are {unique_items}")
"""
#D) Pet Adoption Tracker
"""
adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2
}
while True:
    user_animal=input("Insert Animal(or press Done if finished):  ")
    if user_animal.lower() == "done":
        break
    user_count=input("Enter the Ammount of that Adoptions: ")
    if user_count.isdigit() and int(user_count) < 1:
        print("Invalid Input please enter a positive interger")
        continue
    if user_count.isdigit():
        adoptions[user_animal] = int(user_count)
    else:
        print("Invalid input. Please enter a number.")
        continue
popPet=0
popPetName=""
totAdop=0
myset=set(adoptions)
for species, count in adoptions.items():
    totAdop+=count
    if count > popPet:
        popPet=count
        popPetName=species
    print(f"{species:10} adopted: {count}")
print(f"Them most Popular animal is {popPetName} and the total adoption count is {totAdop}")
print(myset)
"""
# Reflection:
# 1. Which dataset (weather, library, café, or pets) was easiest to work with, and why?
#The easiest one to work with was pets. It was just a dictionary
# 2. How do loops make repetitive tasks faster in programming?
#Loops automate the process
# 3. Which collection type (list, set, or dict) felt most useful today?
#All of the collection types serve different purposes. In context to today I found Dictionaries more useful due to the scnearios provided
# 4. Describe one improvement you would make if this lab continued next week.
# I would add another optional challenge