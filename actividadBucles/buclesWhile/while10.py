#10. Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

def program():
    
    num_students = int(input("Enter the number of students: "))
    
    highest_grade = float('-inf')
    lowest_grade = float('inf')
    total_grades = 0

    for i in range(num_students):
        
        print("\nStudent", i+1)
        grade1 = float(input("Enter grade 1: "))
        grade2 = float(input("Enter grade 2: "))
        grade3 = float(input("Enter grade 3: "))

        total_grades += grade1 + grade2 + grade3

        highest_grade = max(highest_grade, grade1, grade2, grade3)
        lowest_grade = min(lowest_grade, grade1, grade2, grade3)

    if num_students > 0:
        
        average = total_grades / (num_students * 3)
        print(f"\nHighest grade: {highest_grade}\nLowest grade: {lowest_grade}\nAverage grade: {average}")
        
    else:
        print("No students were entered.")

program()