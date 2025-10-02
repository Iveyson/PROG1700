float variable balance = input of users current balance
set a daily limit variable
initiate a while loop
    float variable withdraw = input users ammount out
    if withdrawal > balance output
        output error: not enough money
    elsif withdraw <= 0
        output= invalid input
    elsif limit > 1000
        output withdraw limit is 1000
    else
        Break
balance -= withdraw
limit -= withdraw
output user has withdrawan (withdraw variable) from account. can withdraw (limit balance) and new balance is (balance variable)
