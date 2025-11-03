#Part A) Grocery Analyzer
"""
groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}
total = 0
while True:
    grocery=input("Enter the name of the grocery item: ")
    cost = input(f"What is the cost of {grocery}?: ")
    groceries[grocery]=float(cost)
    x=input("Press Y to continue or anything else to break")
    if x == "y" or x == "Y":
        continue
    else:
        break
i = 0
for item, price in groceries.items():
    if price >= 4.000:
        x = price * 0.10
        price = price - x
    i += 1
    print(f"{item:10} ${price:5.2f}")
    total += price
print(f"\nTotal cost: ${total:.2f}")
print(f"you have {i} items")
"""
#Part B) Student Tracker
"""
students = ["Ava", "Noah", "Liam"]
grades = [88, 92, 79]
student = ""
grade = 0
while True:
    student=input("Insert the students name: ")
    students.append(student)
    grade=input("Insert Grade: ")
    grades.append(grade)
    x=input("Press Y to continue or anything else to loop")
    if x == "y" or x == "Y":
        break
total = 0
count=0
highest=0
lowest=100
Honor_Roll=[]
for i in grades:
    i=int(i)
    if highest < i:
        highest = i
    elif lowest > i:
        lowest = i
    count += 1
    total += i
average= total/count

for i in range(len(students)):
    print(f"{students[i]} → {grades[i]}")
    grades[i]=int(grades[i])
    i=int(i)
    if grades[i] >= 90:
        Honor_Roll.append((students[i],grades[i]))
print(f"The average is {average}. The highest was {highest}. The lowest was {lowest}")
print("----Honor Roll----")
for name,grade in Honor_Roll:
    print(f"{name:10} {grade:5.0f}%")
"""
#Part C) Game scoreboard
"""
Top_Player_score=0
Top_Player_name=""
scores = {"Alex": 12, "Priya": 18, "Jordan": 9}
while True:
    x=input("Insert a name:(or type done to stop) ")
    if x.lower() == 'done':
        break
    y=input("Insert Points for player: ")
    scores[x]=y
for name, points in scores.items():
    print(f"{name:10} {points} pts")
    points=int(points)
    if points>=20:
        print("Level Up!")
    if points > Top_Player_score:
        Top_Player_score=points
        Top_Player_name=name
print(f"The Top Player was {Top_Player_name} who scored {Top_Player_score} points!")
"""
#Part D) Playlist Analyzer
"""
songs = ["Song A", "Song B", "Song C"]
unique_songs = set(songs)
plays = [5, 10, 7]
most_played=""
most_played_count=0
for i in range(len(songs)):
    if most_played_count < plays[i]:
        most_played_count=plays[i]
        most_played=songs[i]
    print(f"{songs[i]} --PlayCount--> {songs[i]}")
print(f"The most played song is {most_played} with {most_played_count} plays!")
print(f"Unique songs are: {unique_songs}")
"""

# Reflection:
# 1. Which mini-project felt most realistic, and why?
#The grocery store one felt the most realistic. Its like a really low level inventory software.
# 2. How do loops make data handling easier?
#Loops allow for you to go through multiple items quickly and with slight automation.
# 3. What did you find challenging about combining loops with collections?
#remembering all the different steps to unpacking at first was difficult.
# 4. One idea for how you could expand any of these mini-projects.
#For the grocery store one possibly adding a way for the user to just add the item to the order
#and then having it output the list of items and price.