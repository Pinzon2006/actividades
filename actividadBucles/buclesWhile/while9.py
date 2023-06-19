#9.	Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio.

def program():
    
    count = 0
    total = 0
    highest = float('-inf')
    lowest = float('inf')

    while True:
        
        temperature = float(input("Enter a temperature: "))

        if temperature == 0:
            break

        count += 1
        total += temperature

        if temperature > highest:
            
            highest = temperature

        if temperature < lowest:
            
            lowest = temperature

    if count > 0:
        
        average = total / count
        print(f"Highest temperature: {highest}\nLowest temperature: {lowest}\nAverage temperature: {average}")
        
    else:
        print("No temperatures were entered.")

program()