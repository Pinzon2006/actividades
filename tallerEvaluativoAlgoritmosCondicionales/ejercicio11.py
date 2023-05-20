#11. Determinar si un número es par o impar.

number = int(input("Insert a number: "))

if number % 2 == 0:
    print(f"{number} It is an even number")
    
else:
    print(f"{number} It is an odd number")