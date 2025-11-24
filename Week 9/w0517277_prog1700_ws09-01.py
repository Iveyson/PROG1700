#A) Modular Calculator
"""
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error Division by 0"
    return a/b

c=0
d=0
operand=""
while True:
    c=input("Please Insert a Number or type done: ")
    if c.lower()=="done":
        break
    elif c.isdigit():
        c=float(c)
        print(f"Your first number is {c}")
    else:
        print("Error: Please Input number: ")
        continue
    d=input("Please Input a Second Number: ")
    if d.isdigit():
        d=float(d)
        print(f"Your Second number is {d}")
    else:
        print("Error: Please Input number: ")
        continue
    operand=input("Please Insert an Operator: ")
    if operand=="+":
        answer=(add(c,d))
        print(f"{answer:.2f}")
    elif operand=="-":
        answer=(subtract(c,d))
        print(f"{answer:.2f}")
    elif operand=="*":
        answer=(multiply(c,d))
        print(f"{answer:.2f}")
    elif operand=="/":
        answer=(divide(c,d))
        print(f"{answer:.2f}")
    else:
        print("Please Input a valid Operator")
        continue
"""
#B) Unit Converter
"""
def km_to_m(km):
    return (km*0.621371)
def m_to_km(m):
    return (m*1.60934)
def c_to_f(c):
    return (c * 9/5) + 32
def f_to_c(f):
    return ((f-32)*5/9)
def lb_to_kg(lb):
    return(lb*0.453592)
def kg_to_lb(kg):
    return(kg*2.20462)
#I made a list of the useable strings in my user input 1 and if it is not in this list it will print an error and restart loop
conv_list=["km","m","c","f","lb","kg"]
func_list=[km_to_m,m_to_km,c_to_f,f_to_c,lb_to_kg,kg_to_lb]
while True:
    user_input1=input("______________________________________\n Select Km for Km to Miles\n Select M for Miles to Km\n Select C for Celcius to farenheit\n Select F for Farenheit to Celcius\n Select Lb for for Pound to Kg\n Select kg for Kg to Pound\n______________________________________\n(Or enter exit):")
    user_input1=user_input1.lower()
    if user_input1=="exit":
        break
    elif user_input1 not in conv_list:
        print("Invalid Input Try again")
        continue
    user_input2=input("Pleaset enter the Number to be converted: ")
    for i in range (len(conv_list)):
        if conv_list[i]==user_input1:
            result = func_list[i] 
            print(f"Result: {result:.2f}")
            break
            
"""
#the above code was my original code that I couldnt get to work. The below code is the code i got working after using AI and w3 schools research

# Conversion functions
"""
def km_to_m(km):
    return km * 0.621371

def m_to_km(miles):
    return miles * 1.60934

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def lb_to_kg(pounds):
    return pounds * 0.453592

def kg_to_lb(kg):
    return kg * 2.20462

# Mapping user input to functions
conversion_map = {
    "km": km_to_m,
    "m": m_to_km,
    "c": c_to_f,
    "f": f_to_c,
    "lb": lb_to_kg,
    "kg": kg_to_lb
}
while True:
    print("______________________________________")
    print(" Select Km for Km to Miles")
    print(" Select M for Miles to Km")
    print(" Select C for Celsius to Fahrenheit")
    print(" Select F for Fahrenheit to Celsius")
    print(" Select Lb for Pound to Kg")
    print(" Select Kg for Kg to Pound")
    print("______________________________________")
    user_input1 = input("(Or enter 'exit' to quit): ").lower()

    if user_input1 == "exit":
        break
    elif user_input1 not in conversion_map:
        print("Invalid Input. Try again.")
        continue

    user_input2 = input("Please enter the number to be converted: ")
    try:
        value = float(user_input2)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    conversion_function = conversion_map[user_input1]
    result = conversion_function(value)
    print(f"Result: {result:.2f}")
"""
#C) Validation Functions
"""
def is_positive(num):
    return num > 0

def is_integer(value):
    return value.isdigit()
invalid_count=0
while True:
    user_input = input("Please Enter a Positive Integer (or press done to exit): ")
    if user_input.isdigit():
        if is_integer(user_input):
            num = int(user_input)
            positive = is_positive(num)
            print("Is positive:", positive)
            print("Is integer:", True)
        else:
            print("Invalid input. Not an integer.")
            print("Is positive: False")
            print("Is integer: False")
    elif user_input.lower()=="done":
        break
    else:
        invalid_count += 1
        print(f"Error enter a valid input #{invalid_count}")
        continue
"""
# Reflection:
# 1. How did using functions change the structure of your code?
#The functions allow for you to automate a lot of process.
#instead of typing it out every time you can store it in a function and call to it.
# 2. Which task (calculator, converter, validation) felt most useful?
#the converter was the one I enjoyed the most and found the most useful at least from a learning perspective
# 3. How might modular code help on larger projects?
#Modular coding is more organized and structured and the functions are reusable making it convenient
# 4. One real-world example where you would use functions in the future.
#Functions are like building blocks. You need all the individual pieces then you stack them together to build
