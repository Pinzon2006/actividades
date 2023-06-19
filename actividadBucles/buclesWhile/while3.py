#3.	Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

def program(n):
    
    sum = 0
    counter = 0
    i = 1

    while i <= n:
        if i % 2 != 0:
            sum += i
            counter += 1
        i += 1

    print(f"The sum of all odd numbers up to {n} is: {sum}\nHay {counter} odd numbers.")

n = int(input("Insert a number: "))
program(n)
