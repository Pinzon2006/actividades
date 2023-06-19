#1.	Suma de los n primeros números, solicite al usuario el numero de elementos a sumar

def sumeNumbers(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

numElements = int(input("Input a number: "))
result = sumeNumbers(numElements)
print(f"The sum of the {numElements} es: {result}")
