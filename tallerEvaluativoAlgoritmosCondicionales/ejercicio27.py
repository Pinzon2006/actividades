#27. Realice un menú donde el usuario deberá seleccionar una opción de las operaciones básicas, y se le solicite al usuario digitar dos números, y dependiendo de la respuesta realice cada operación.

def cal (selectOption,number1,number2):
    
    if selectOption == 1:
        result1 = number1 + number2
        print(f"The sum of {number1} and {number2} is: {result1}")

    elif selectOption == 2:
        result2 = number1 - number2
        print(f"The subtract of {number1} and {number2} is: {result2}")
        
    elif selectOption == 3:
        result3 = number1 * number2
        print(f"The multiplication of {number1} and {number2} is: {result3}")
        
    elif selectOption == 4:
        result4 = number1 / number2
        print(f"The division of {number1} and {number2} is: {result4}")
        
    elif selectOption == 5:
        result5 = number1 // number2
        print(f"The whole division of {number1} and {number2} is: {result5}")
        
    elif selectOption == 6:
        result6 = number1 % number2
        print(f"The quotient of {number1} and {number2} is: {result6}")
        
    else:
        print("This type of operation is not currently available.")

print(f"Basic operations calculator\nSum = 1\nSubtract = 2\nMultiplication = 3\nDivision = 4\nWhole Division = 5\nQuotient = 6\n")
cal(selectOption = int(input("Select a one option: ")), number1 = int(input("Insert a number: ")), number2 = int(input("Insert another number: ")))