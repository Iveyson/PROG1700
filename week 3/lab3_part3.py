temp = float(input("Enter the temperature (°C): "))
weather = str(input ("Is it raining?"))

if temp < 0 and weather == "yes":
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")