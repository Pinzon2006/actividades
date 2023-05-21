#Realizar el siguiente algoritmo:
#Calcular el salario de un empleado dado el numero de horas, el valor de la hora y la categoria del empleado
#Categoria - Incremento
#   A           10%
#   B           15%
#   C           23%
#   D           25%

def salary(category,numberNours,valueHour):
    subTotal = numberNours * valueHour
    
    if category == "A":
        increaseA = subTotal * 0.1
        totalA = subTotal + increaseA
        print(f"Your salary final is: {totalA}")
    
    elif category == "B":
        increaseB = subTotal * 0.15
        totalB = subTotal + increaseB
        print(f"Your salary final is: {totalB}")
    
    elif category == "C":
        increaseC = subTotal * 0.23
        totalC = subTotal + increaseC
        print(f"Your salary final is: {totalC}")
    
    elif category == "D":
        increaseD = subTotal * 0.23
        totalD = subTotal + increaseD
        print(f"Your salary final is: {totalD}")
        
    else:
        print(f"Error, category {category} does not exist")
    
salary(category=input("Enter the category you belong to \"A,B,C or D\": "),numberNours=int(input("Insert number of hours worked: ")),valueHour=int(input("Insert hourly rate: ")))