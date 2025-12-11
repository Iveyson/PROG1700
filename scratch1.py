#Guessing Game
import random
def user_guess():
    while True:
        user_input=input("Please enter a number between 1-10: ")
        try:
            user_input=int(user_input)
            if user_input > 10 or user_input<1:
                print("Please enter an interger between 1 and 10")
            else:
                return user_input
        except:
            print("This is not an interger try again")

def random_number_gen():
    ran_num=random.randint(1,10)
    return ran_num


def check_number(target):
    while True:
        guess = user_guess()
        if guess == target:
            print("You have guessed the correct number")
            break
        else:
            print("Please Try again!!: ")

def main():
    target=random_number_gen()
    check_number(target)

if __name__ == "__main__":
    main()