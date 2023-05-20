#10. Mostrar la suma de dos números enteros, si el resultado supera a 10.

number1 = int(input("Insert a number: "))
number2 = int(input("Insert another number: "))
sum = number1 + number2

if sum >= 10:
    print(f"The sum of the numbers is: {sum}")
    
else:
    print("\nThe sum of the numbers does not meet the minimum threshold to perform the operation.")