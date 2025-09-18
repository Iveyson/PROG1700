user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Wrong password.")
elif user == "joe":
    if password == "joe1":
        print("Access granted.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")
