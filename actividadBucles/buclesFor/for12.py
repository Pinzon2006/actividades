#12. Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

def calculate_grade_stats():
    numStudents = int(input("Enter the number of students: "))

    highestGrade = float("-inf")
    lowestGrade = float("inf")
    totalGrade = 0

    for i in range(numStudents):
        print(f"Student {i+1}")
        grades = []
        for j in range(4):
            grade = float(input(f"Enter grade {j+1}: "))
            grades.append(grade)

            if grade > highestGrade:
                highestGrade = grade

            if grade < lowestGrade:
                lowestGrade = grade

        student_average = sum(grades) / 4
        totalGrade += student_average

    classAverage = totalGrade / numStudents

    print(f"Highest grade: {highestGrade}\nLowest grade: {lowestGrade}\nClass average: {classAverage}")

calculate_grade_stats()
