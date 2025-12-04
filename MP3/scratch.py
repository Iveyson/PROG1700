
def read_grades(file_path):
    grades = {}
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            if not line.strip():
                continue
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue
            name, grade_str = parts
            try:
                grade = int(grade_str)
            except ValueError:
                continue
            grades[name] = grade
    return grades


def compute_grade_stats(grades, pass_mark=50):
    if not grades:
        return {
            "passing": [],
            "failing": [],
            "total": 0,
            "highest": None,
            "lowest": None,
            "average": None,
            "count": 0,
            "pass_mark": pass_mark,
        }

    passing = []
    failing = []
    total = 0
    iterator = iter(grades.values())
    first_grade = next(iterator)
    highest = first_grade
    lowest = first_grade
    total += first_grade
    passing = []
    failing = []
    total = 0
    highest = None
    lowest = None

    for name, grade in grades.items():
        total += grade
        if (highest is None) or (grade > highest):
            highest = grade
        if (lowest is None) or (grade < lowest):
            lowest = grade
        if grade < pass_mark:
            failing.append(name)
        else:
            passing.append(name)

    count = len(grades)
    average = total / count

    return {
        "passing": passing,
        "failing": failing,
        "total": total,
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "count": count,
        "pass_mark": pass_mark,
    }


def write_grades_to_txt(grades, stats, output_path):
    """
    Writes individual grades and the computed statistics to a text file.
    Expects `stats` to come from `compute_grade_stats`.
    """
    with open(output_path, "w") as f:
        # Write individual grades first
        for name, grade in grades.items():
            f.write(f"{name}: {grade}\n")

        # Write aggregate metrics
        avg_str = "N/A" if stats["average"] is None else f"{stats['average']:.2f}"
        highest_str = "N/A" if stats["highest"] is None else str(stats["highest"])
        lowest_str = "N/A" if stats["lowest"] is None else str(stats["lowest"])

        f.write(f"Average: {avg_str}\n")
        f.write(f"Highest grade: {highest_str}\n")
        f.write(f"Lowest grade: {lowest_str}\n")
        f.write(f"Passing grade: {stats['passing']}\n")
        f.write(f"Failing grade: {stats['failing']}\n")


def main():
    grades_dict = read_grades("grades.csv")
    stats = compute_grade_stats(grades_dict, pass_mark=50)
    write_grades_to_txt(grades_dict, stats, "report.txt")
    print("The report can be found in report.txt")


if __name__ == "__main__":
    main()
