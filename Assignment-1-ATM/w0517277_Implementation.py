#initializing the balance before the loop so they can re enter withdraw inputs.
balance = float(input("Insert current balance: "))

#set withdraw limit to 1000 so you can't withdraw more then 1000
limit=1000

#set the while loop up so they can redo withdrawl inputs
while True:
    withdraw = float(input("Insert withdraw ammount: "))

    #Check if withdraw is valid no 0 or negative ammount
    if withdraw <= 0:
        print ("Invalid withdrawl ammount please insert new ammount: ")

    #check to see if you are trying to take more money then possible
    elif balance < withdraw:
        print ("Invalid withdrawl ammount please insert new ammount: ")

    #checks if you withdrew more then the limit
    elif withdraw > 1000:
        print("Withdraw limit is 1000 please insert new ammount: within the constraints ")

    #break the loop and do the calculations
    else:
        break
    
#subtract the withdraw from the balance and daily limit and display the transaction and set the rounding to 2 decimal places
balance -= withdraw
limit -= withdraw
balance=(round(balance, 2))
withdraw=(round(withdraw, 2))
limit=(round(limit, 2))
print("You withdrew ", withdraw," you can withdraw ", limit," today and your new balance is ", balance)