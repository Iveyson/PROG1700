"""
import time
# Simple counting machine
count = 10
while count >= 1:
    print("Launching in:", count)
    time.sleep(1)
    count -= 1
print("Lift Off!")
"""
"""
import random

secret = random.randint(1, 10)
guess = 0
count = 0
attempts = 0
score = 10 - attempts
play = "Y"
while play == "Y":
    if play == "Y":
        while guess != secret:
            guess = int(input("Guess a number between 1 and 10: "))
            count += 1
            attempts +1
            if count == 3:
                print("You are out of guesses. Game Over 😢")
                play = input("Press Y for yes and N for no")
                play = play.upper
            elif guess < secret:
                print("Too low! 📉", " Your guess count is: ", count)
            elif guess > secret:
                print("Too high! 📈", " Your guess count is: ", count)
            else:
                print("You got it! 🎉", " Your guess count is: ", count, " You scored", score, " points!")
                print("Would you like to play again?")
                play = input("Press Y for yes and N for no: ")
                play = play.upper
    else:
        break
"""
##ran into issues attempting to install pygame to add sound effects. File Path issues
"""
import pygame
pygame.init()
pygame.mixer.init()
import time
import random
player1_score = 0
player2_score = 0

while player1_score < 3 and player2_score < 3:
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    print(f"Player1:{roll1} | Player2:{roll2}")
    if roll1 > roll2:
        player1_score += 1
        playsound('dice-142528.mp3')
        time.sleep(1)
    elif roll2 > roll1:
        player2_score += 1
        time.sleep(1)
print("Winner:", "Player 1" if player1_score > player2_score else "Player 2")
"""

# Reflection:
# 1. What bug or mistake caused your first infinite loop today?
# I did not have any infinite loops today but I did run into some issues importing a few python modules due to a file pathing error that went unresolved
# 2. How did you fix it?
# I did not fix it I went into the CLI and reset the file pathing for my userprofile and still couldn't use pip install
# 3. Which loop activity did you enjoy most, and why?
# I enjoyed the loop activity with the dice battle simulator since its the one I spent the most time on problem solving to attempt to get audio working
# 4. How might while loops be useful in a game or app you’d build someday?
# while loops are useful for any counter based loops or repeating until conditions change. For example an atm machine is a good example.
