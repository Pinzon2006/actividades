#8.	Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero

def program():
    
    while True:
        
        number = int(input("Enter an integer greater than zero: "))

        if number <= 0:
            
            print("Invalid input. Please enter a number greater than zero.")
            
        else:
            break

    divisors = []
    
    for i in range(1, number + 1):
        
        if number % i == 0:
            
            divisors.append(i)

    print(f"The divisors of {number}, are: {divisors}")
    
program()