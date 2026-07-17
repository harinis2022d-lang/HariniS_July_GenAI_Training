def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average:.1f}")
    print("Grade:", grade)

    print("Subjects below 40:")
    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i+1}")
            found = True
    if not found:
        print("None")


name = input("Enter Name: ")
roll = int(input("Enter Roll Number: "))

marks = []
for i in range(5):
    marks.append(float(input(f"Enter mark {i+1}: ")))

analyze_result(name, roll, marks)
