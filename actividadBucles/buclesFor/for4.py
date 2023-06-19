#4.	Sumar pares desde 0 hasta el número que indique el usuario

def sumNumbers(num):
    suma = 0
    for i in range(2, num, 2):
        suma += i
    return suma + num

numInput = int(input("Insert a number: "))
result = sumNumbers(numInput)
print(f"The sum of even numbers up to {numInput} is: {result}")