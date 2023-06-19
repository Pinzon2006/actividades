#1.	Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos

def multiply ():
        
    result = 1
    sum = 1
    
    while sum <= 10:
        
        result *= sum
        sum += 1
        
    return result
    
def sume ():
        
    result = 0
    sum = 1
    
    while sum <= 10:
        
        result += sum
        sum += 1
        
    return result
    
num=int(input("Insert a number: "))

if num > 10:
    result = multiply()
    print(f"The result of the multiplication of the first 10 numbers is: {result}")
    
else:
    result = sume()
    print(f"The result of the sume of the first 10 numbers is: {result}")