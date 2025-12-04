# Define a function called numchecker
def numchecker():
    # Start an infinite loop so the program keeps asking until the user exits
    while True:
        try:
            # Prompt the user to enter a number and convert the input to an integer
            selection = int(input("Enter a valid number (1-26), 0 to exit: "))
           
            # Check if the user entered 0 (exit condition)
            if selection == 0:
                print("Thank you for using the number checker")
                break  # Exit the loop
           
            # Check if the number is between 1 and 26 (inclusive)
            elif 1 <= selection <= 26:
                print("Well done.")  # Valid input
           
            # If the number is outside the valid range
            else:
                print("Invalid input.")
       
        # Handle the case where the user enters something that is not an integer
        except ValueError:
            print("Invalid input. Please enter an integer.")
 
# Main program starts here
numchecker()  # Call the function to run the program