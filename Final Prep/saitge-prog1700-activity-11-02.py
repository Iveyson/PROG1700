userinput = input("Enter a file name(filename.txt or 0 to to exit): ")
if userinput=="0":
   print("Exiting the program. Goodbye!")

if validatefilename(userinput):
    print(f"Valid filename: {userinput}")
else:
    print(f"Invalid filename: {userinput}. Ensure format is 'filename.txt' with only")