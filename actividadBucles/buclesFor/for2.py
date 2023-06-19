#2.	Digite un número, si el numero supera a 10, multiplique los 10 primeros números, si no, súmelos

def multiply (num):
    
    if num > 10:
        multi = 1
        
        for i in range(1, num+1):
            multi *= i
        return multi
    
    else:
        sum = 0
        
        for i in range(1, num+1):
            sum += i
        return sum
        

numInsert = int(input("Insert a number: "))
result = multiply(numInsert)
print(f"The multiply {numInsert} is: {result}")