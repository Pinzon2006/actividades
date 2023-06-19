#7.	Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def program():
    
    totalSum = 0

    while True:
        
        number = int(input("Enter an integer number: "))

        if number == 0:
            break

        totalSum += number

    print(f"The sum of all the numbers is: {totalSum}")

program()