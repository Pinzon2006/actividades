#8. Diseñar un algoritmo que muestre si una persona tiene ingresos o no, debe indicarlos ingresos y egresos, se debe validar el saldo , pero para ser más específicos se responderá a las siguientes preguntas:
#Si no tiene efectivo entonces está en números rojos.
#Si tiene poco efectivo menor a 2000, que muestre que debe esforzarse por trabajar más.
#Si tiene un efectivo menor a 3000 entonces significa que le va regularmente bien.
#Si tiene un efectivo mayor a 3000 entonces significa que tiene buen status financiero.
def status (quest1):
    
    if quest1 == "yes":
        
        income = float(input("Enter the amount of income: "))
        expenditures = float(input("Enter the number of outflows: "))
        total = income-expenditures
        
        if total < 2000:
            print("You should strive to work harder")

        elif total in range (2001,2999):
            print("Regularly well")

        elif total >= 3000:
            print("Has a good financial status")
            
    elif quest1 == "no":
        print("You are in the red")
        
    else:
        print("Error")
        
status(quest1=input("Do you have income? yes or no: "))