x = int(input("Insert age: "))
age = x
student = bool(input ("Are you a student? type anything if yes if no press enter: "))
if age < 5:
    print("Your ticket is free")
elif age < 13 and student == True:
    print("You get the student discount! $2 please")
elif age == 5 or age < 13:
    print ("Your ticket is $8")
elif age ==13 or age <65:
    print("Your ticket is $12")
else:
    print("You are a senior! Your ticket is $6")