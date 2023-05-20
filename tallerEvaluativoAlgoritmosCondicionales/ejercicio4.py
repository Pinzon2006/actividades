#4. Diseña un algoritmo que lea 2 números y visualice si son positivos.

num1 = int(input("Insert a number: "))
num2 = int(input("IInsert another number: "))

if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
    
else:
    print("One or both numbers are negative")