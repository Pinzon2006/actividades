#13. Dado tres números calcular el menor

def lowerNumber (number1, number2, number3):
    
    if number1 <= number2 and number1 <= number3:
        print(f"{number1} is larger than {number2} and {number3}")
        
    elif number2 <= number1 and number2 <= number3:
        print(f"{number2} is larger than {number1} and {number3}")
        
    else:
        print(f"{number3} is larger than {number1} and {number2}")
        
lowerNumber(number1 = int(input("Insert a number: ")), number2 = int(input("Insert another number: ")), number3 = int(input("Insert another number: ")))