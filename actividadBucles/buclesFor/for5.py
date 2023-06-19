#5.	Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

def sumNumbers(num):
    
    sum = 0
    totalNumOdd = 0
    
    for i in range(1, num, 2):
        sum += i
        totalNumOdd +=1
    return sum + num, totalNumOdd

numInput = int(input("Insert a number: "))
result, counter = sumNumbers(numInput)
print(f"The sum of odd numbers up to {numInput} is: {result}. And total d odd numbers is: {counter}")