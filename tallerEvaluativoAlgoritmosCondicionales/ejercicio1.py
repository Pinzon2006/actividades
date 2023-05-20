#1. Diseñe un algoritmo que capture dos números, y que realice la suma de dichos números, y mostrar los datos si es el resultado no es negativo.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
suma = num1 + num2

if suma > 0:
    print(f"The sum is equal to: {suma}")
    
else:
    print(f"The sum is negative")