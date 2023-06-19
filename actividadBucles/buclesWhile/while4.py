#4.	Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo

def program(start, end):
    
    if start >= end:
        print(f"{start} is smaller than {end}")
        return

    current = start

    while current <= end:
        print(current)
        current += 1

num1 = int(input("Insert a number: "))
num2 = int(input("Insert another number: "))
program(num1, num2)
