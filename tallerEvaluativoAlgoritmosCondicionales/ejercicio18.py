#18. Hacer un programa que pida 3 números e indicar si el tercero es igual a la suma del primero y el segundo.

number1 = int(input("Insert a number: "))
number2 = int(input("Insert another number: "))
number3 = int(input("Insert another number: "))
sum = number1 + number2

if number3 == sum:
    print(f"The sum {number1} and {number2} is equal {number3}")
    
else:
    print(f"the sum of numbers {number1} and {number2} do not equal {number3}")