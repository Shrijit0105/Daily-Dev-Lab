
def grade_analyzer(marks):

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n--- Student Report ---")
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Grade:", grade)


# Taking input
marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        break

    marks.append(mark)

if len(marks) == 5:
    grade_analyzer(marks)
