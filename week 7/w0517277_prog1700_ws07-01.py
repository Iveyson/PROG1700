#Step 1: Tuple Basics: Airline Ticket
"""
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

Departure, Arival, Plane, Cost = ticket
print(f"From {Departure} to {Arival} on flight {Plane} costing ${Cost}")
"""
#Step 2: Tuple Collections: Travel Itinerary
"""
flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]
counter = 0
total_cost = 0
while True:
    for origin, destination, price in flights:
        print(f"{origin} → {destination}: ${price}")
        total_cost= total_cost + price
    print(f"The total is {total_cost}")    
    total_cost= total_cost/3
    print(f"Average Is: {total_cost}")
    break
"""
"""        
        if price < 150:
            print(f"{origin} → {destination}: ${price}")
            total_cost= total_cost + price
            print(f"The total is {total_cost}")
    break
"""        
#Step 3: Simulating Updates
#Do Not Do
#Step 4: Real World Mini Challenge: Pizza Orders
orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]

for name, size, toppings in orders:
    toppings_str=""
    for i in toppings:
        toppings_str += i + " "
    
    print(f"{name} ordered a {size} pizza with {toppings_str} on top")

# Reflection:
# 1. Why are tuples useful if you can’t modify them?
#Tuples are useful if left unmodifiable because of values that will never change like grid coordinates
# 2. In which step did immutability cause you to think differently?
#during the mini challenge having to find a way to restore the list that is inside the tuple to unpack it was a very unique way of/
#problem solving
# 3. Which exercise did you enjoy most, and why?
#I enjoyed the pizza orders one the most because it gave me the most trouble and it was the most interesting.
# 4. Give one example in real life where tuples make sense (e.g., coordinates, database records).
#A good example would be storing color values. Something like an RGB scale will always have the same numbers associated with the same colour
    
