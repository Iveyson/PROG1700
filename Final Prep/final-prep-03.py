import random, time
"""
gifts = ["🍫", "🧸", "🎮", "📚", "🎧"]
random.shuffle(gifts)
score=0
my_dict={}
print("Shuffled gifts:", gifts)
for item in gifts:
    print("You see:", item)
    if item=="🎮" or item== "🎧":
        score+=10
    elif item =="📚" or item=="🍫":
        score+=5
    elif item=="🧸":
        score+=8
    print(f"current score is {score}")
    time.sleep(0.5)
print(f"Final Score is {score}")
"""

gifts = ["🍫", "🧸", "🎮", "📚", "🎧"]
random.shuffle(gifts)
while True:
    user_input=input(f"How many gifts would you like to unpack? {len(gifts)}")
    print("Shuffled gifts:", gifts)
    for item in gifts:
        print("You see:", item)

