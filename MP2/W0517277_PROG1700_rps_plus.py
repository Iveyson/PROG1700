import random
import math

valid_moves = ["rock", "paper", "scissors","lizard","spock"]
valid_set = {"rock", "paper", "scissors","lizard","spock"}
score = {"player": 0, "cpu": 0, "ties": 0}
history = []
player_streak = 0
cpu_streak = 0
max_player_streak = 0
max_cpu_streak = 0


def get_player_move():
    while True:
        user_input = input("Please Enter Rock, Paper, Scissors, Lizard or Spock: ").lower()
        if user_input not in valid_moves:
            print("Invalid move. Try again.")
        else:
            return user_input

def get_cpu_move():
    cpu_1=random.randint(1,5)
    if cpu_1==1:
        return "rock"
    elif cpu_1==2:
        return "scissors"
    elif cpu_1==3:
        return "paper"
    elif cpu_1==4:
        return "lizard"
    else:
        return "spock"

def decide_winner(player,cpu):
    if player==cpu:
        score["ties"]+=1
        return "Tie"
    #check all instances of player winning
    elif (player == "rock" and cpu=="scissors") or (player=="rock" and cpu=="lizard") or (player == "scissors"and cpu=="paper") or (player=="scissors" and cpu=="lizard") or (player=="paper" and cpu=="rock") or (player=="paper" and cpu=="spock") or (player=="lizard" and cpu=="paper") or (player=="lizzard" and cpu=="spock") or (player=="spock" and cpu=="scissors") or (player=="spock" and cpu=="rock"):
        score["player"]+=1
        return "Player Wins"
    else:
        score["cpu"]+=1
        return "Cpu Wins"
    
def print_scoreboard():
    print(f"Scoreboard: Player={score['player']} CPU={score['cpu']} Ties={score['ties']}")

def print_history():
    print("Game History:")
    for round_info in history:
        print(round_info)


while True:
    while True:
        try:
            total_games = int(input("Enter how many games to play (must be odd): "))
            if total_games % 2 == 0 or total_games <= 0:
                print("Please enter an odd positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


    wins_needed = math.ceil(total_games / 2)
    print(f"First to {wins_needed} wins will be the champion!")

    while score["player"] < wins_needed and score["cpu"] < wins_needed:
        player_move = get_player_move()
        cpu_move = get_cpu_move()
        print(f"CPU chose: {cpu_move}")
        result = decide_winner(player_move, cpu_move)
        if result == "Player Wins":
            player_streak += 1
            cpu_streak = 0
            if player_streak > max_player_streak:
                max_player_streak = player_streak
        elif result == "Cpu Wins":
            cpu_streak += 1
            player_streak = 0
            if cpu_streak > max_cpu_streak:
                max_cpu_streak = cpu_streak
        else:  # Tie
            player_streak = 0
            cpu_streak = 0
        print(result)
        history.append(f"Player: {player_move}, CPU: {cpu_move}, Result: {result}")
        print_scoreboard()

    play_again = input("Type Yes to play again. Anything else to end: ").lower()
    if play_again != "yes":
        for i in range(len(history)):
            print(f"Game {i}: {history[i]}")
        break

print(f"Longest Player Win Streak: {max_player_streak}")
print(f"Longest CPU Win Streak: {max_cpu_streak}")




# Reflection:
# 1) Which function was most useful to keep your code organized? Why?
#The most useful function in the code to keep it organized was decide player winner.
#The reason is was the most useful function is because it allows us to only have to write that check once
#and just call it in the future when needed.
# 2) What bug or edge case did you fix (describe inputs + expected vs actual)?
#I ran into a bug regarding the loop_count and I couldnt figure out what it was.
#Turns out I never added it into the loop to actually count it.
# 3) Which data structure (list/set/dict) felt best for each part (why)?
#the list was best for storing the valid moves since we just needed to check if the user had
#put in one of those items.
#I didn't use the set at all but its good to prevent duplicate data
#Dictionary was good at keeping track of the score since its a key value.
# 4) If you had one more hour, what improvement would you ship next?
#I would try and add sound affects when it displays who wins
