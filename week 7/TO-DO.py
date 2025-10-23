toppings = ["Pepperoni", "Mushroom", "Hot Peppers", "Cheese"]
t_str = "The toppings on the pizza are: "
# Build the string manually
for i in range(len(toppings)):
    # Add the space for all items except the last in the list
    if i < len(toppings) - 1:
        t_str += toppings[i] + " and "
    # If last item in the list, do not add the space
    elif i == len(toppings) -1:
        t_str += toppings[i]
t_str += "."
print(f"{t_str}")