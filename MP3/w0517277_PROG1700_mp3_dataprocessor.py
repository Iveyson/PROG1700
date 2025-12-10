def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        content = content.strip()
        lines = content.split("\n")
        students = []
        grades = []
        for line in lines:
            parts = line.split(",")
            name = parts[0].strip()
            grade_str = parts[1].strip()
            grade = int(grade_str)
            students.append((name, grade))
            grades.append(grade)
    return students, grades


def process_data(grades):
    highest = max(grades)
    lowest = min(grades)
    average = sum(grades) / len(grades)
    return highest, lowest, average


def write_report(output_file, students, highest, lowest, average):
    with open(output_file, "w") as file:
        file.write("Grades\n")
        file.write("------------------\n")
        for name, grade in students:
            file.write(f"{name}: {grade}\n")
        file.write("\nSummary\n")
        file.write("------------------\n")
        file.write(f"Highest Grade: {highest}\n")
        file.write(f"Lowest Grade: {lowest}\n")
        file.write(f"Average Grade: {average:.2f}\n")


def main():
    students, grades = read_file("grades.csv")
    print(students, grades)
    highest, lowest, average = process_data(grades)
    write_report("grades_summary.txt", students, highest, lowest, average)
    print("grades_summary.txt has been created.")


if __name__ == "__main__":
    main()






"""
Sources:
https://www.w3schools.com/python/ref_file_read.asp <--- .read method
https://www.w3schools.com/python/ref_string_split.asp <--- .split method
https://www.w3schools.com/python/ref_string_strip.asp <--- .strip method
https://www.w3schools.com/python/ref_func_min.asp <--- min function 
https://www.w3schools.com/python/ref_func_max.asp <--- max function
https://www.w3schools.com/python/ref_func_sum.asp <--- sum function
"""