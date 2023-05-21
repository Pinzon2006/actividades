#33. Indicar si entre dos números si ambos son pares o uno de ellos cual es par.

def compare (number1,number2):
    
    if number1 % 2 == 0 and number2 % 2 == 0:
        print(f"The numbers {number1} and {number2} are pairs")
        
    elif number1 % 2 == 0:
        print(f"Number {number1} is even and number {number2} is odd")
    
    elif number2 % 2 == 0:
        print(f"Number {number2} is odd and number {number1} is ever")
    
    else:
        print(f"The numbers {number1} adn {number2} are odd")

compare(number1=int(input("Insert a number: ")),number2=int(input("Insert another number: ")))