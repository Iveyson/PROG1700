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
    toppings_str = "&" .join(toppings)
    print(f"{name} ordered a {size} pizza with {toppings} on top")
    
