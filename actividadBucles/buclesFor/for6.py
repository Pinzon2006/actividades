#6.	Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo

def program (num1, num2):
    
    if num1 < num2:
        
        sum = 0
        
        for i in range(1, num2+1):
            
            sum += i
            
        return sum
        
    elif num1 == num2:
        print("Sorry, both numbers are the same.")
    
    else:
        print("Sorry, the number 1 is larger thar number 2.")
        
num1 = int(input("Insert a number: "))
num2 = int(input("Insert another number: "))
result = program(num1, num2)
print(result)