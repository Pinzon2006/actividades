#10. Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero

def progAl (num):
    
    if num > 0:
        
        divisors = []
        
        for i in range(1, num + 1):
            
            if num % i == 0:
                
                divisors.append(i)
                
        return divisors
    
    else:
        print(f"Error! {num} is equal to or less than 0")
        
numInput = int(input("Input a number: "))
result = progAl(numInput)
print(f"The divisors of {numInput} is: {result}")