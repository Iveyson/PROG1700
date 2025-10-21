#Step1: Counting In Ranges
# Simple range example
"""
for i in range(2, 11, 2):
    print("Count:", i)
print("Done!")
"""
#Step 2: Pattern Printing Party
"""
for i in range(1, 6):
    print("🔺" * i)

for i in range(1, 6):
    print(" " * (6 - i) + "🌲" * (2 * i - 1))
    if i == 5:
        for i in range(4, 0, -1):
            print(" " * (6 - i) + "🌲" * (2 * i - 1))
"""
#Step 3: Real World Example: Student Grade Summary
students = ["Ava", "Noah", "Liam", "Sophia"]
grades = [88, 92, 79, 95]

print("Student Grade Report:")
for i in range(len(students)):
    print(f"{students[i]} → {grades[i]}%")

average = sum(grades) / len(grades)
print(f"\nClass Average: {average:.1f}%")