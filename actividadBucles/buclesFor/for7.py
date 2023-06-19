#7.	Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.

def program (num):
    
    sum = 0
    counter = 0
    
    for i in range (10):
        
        sum += 1
        counter += 1
        multiply = num * sum
        
        print(f"{num} x {counter} is: {multiply}")

numImput = int(input("Insert a number: "))
program(numImput)