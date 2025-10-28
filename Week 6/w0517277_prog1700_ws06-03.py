#Step 1 Number Guesser
"""
import random
secret = random.randint(1, 10)
guess = 0
count = 0
while guess != secret:
    if count == 5:
        print(f"You have guessed {count} times! You are out of guesses")
        break
    guess = input("Guess a number (1–10): ")
    if guess.isdigit():
        guess=int(guess)
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("You got it!")
    else:
        print("invalid try again")
        continue
"""
#Step 2 Coin Flipper
"""
import random

heads = 0
tails = 0
count = 0
user_input = None
user_input = int(input("How many flips would you like? "))
while count < user_input:
    flip = random.choice(["Heads", "Tails"])
    print(flip)
    if flip == "Heads":
        heads += 1
    else:
        tails += 1
    count += 1
    tails_percent = (tails/user_input)*100
    if tails_percent == 70:
        break
    heads_percent = (heads/user_input)*100
    if heads_percent == 70:
        break
    tails_percent = None
    heads_percent = None
print(f"Heads: {heads}, Tails: {tails}")
print(f"The percent of tales rolled is {tails_percent}% and the percent of heads rolled is {heads_percent}%")
"""
#Step 3 Countdown timer
"""
import time
cloud = "💨"
count=int(input("Pick the starting number to count down from"))
while count >= 0:
    print(cloud)
    print(count)
    time.sleep(1)
    count -= 1
    cloud = cloud+"💨"
print("Blast off! 🚀")
"""
#Step 4 Pattern Generator
"""
rows = 1
x = 0
size=int(input("How big would you like the pattern? "))
symbol=str(input("What Symbol would you like? "))
while rows <= size:
    print(f"{symbol}" * rows)
    rows += 1
while rows >= 0:
    print("💫" * rows)
    rows -= 1
"""
# Reflection:
# 1. Which challenge did you find most fun or surprising?
#I liked the last challenge I had fun messing around with the loops to try and invert it.
# 2. What is one common mistake that caused infinite loops today?
#Using the incorect operator like a > when you need a <
# 3. How could while loops be used in a real-world app?
#while loops are great for input validation
# 4. Which activity helped you best understand “loop conditions”?
#the final one did