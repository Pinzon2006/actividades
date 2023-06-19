#6.	Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

def program():
    
    total = 0
    count = 0

    while True:
        
        grade = float(input("Enter the grade: "))

        if grade == -1:
            break

        total += grade
        count += 1

    if count > 0:
        
        average = total / count
        print(f"The average grade is: {average}")
        
    else:
        print("No grades were entered.")

program()