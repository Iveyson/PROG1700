temp = float(input("Enter the temperature (°C): "))
weather = bool(input ("Is it raining? True/False: "))

if temp < 0 and weather == True:
    print("Warning: Extreme temperature!")
else:
    print("Temperature is normal.")