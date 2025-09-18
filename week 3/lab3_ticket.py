x = int(input("Insert age: "))
age = x
if age < 5:
    print("Your ticket is free")
elif age == 5 or age < 13:
    print ("Your ticket is $8")
elif age ==13 or age <65:
    print("Your ticket is $12")
else:
    print("You are a senior! Your ticket is $6")