#2.	Sumar pares desde 0 hasta el número que indique el usuario.

def program(num):
    
    result = 0
    counter = 0

    while counter <= num:
        
        if counter % 2 == 0:
            
            result += counter
            
        counter += 1

    return result

num = int(input("Insert a number: "))
result = program(num)
print(f"The sum of even numbers from 0 to {num} is: {result}")
