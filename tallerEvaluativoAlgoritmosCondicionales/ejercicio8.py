#8. Diseñar un algoritmo que muestre si una persona tiene ingresos o no, debe indicarlos ingresos y egresos, se debe validar el saldo , pero para ser más específicos se responderá a las siguientes preguntas:
#Si no tiene efectivo entonces está en números rojos.
#Si tiene poco efectivo menor a 2000, que muestre que debe esforzarse por trabajar más.
#Si tiene un efectivo menor a 3000 entonces significa que le va regularmente bien.
#Si tiene un efectivo mayor a 3000 entonces significa que tiene buen status financiero.
income = float(input("Enter the amount of income: "))
expenditures = float(input("Enter the number of outflows: "))
total = income-expenditures

if total >= 0:
    print("You should strive to work harder")

elif total >= 2001 and income <= 3000:
    print("Regularly well")

elif total >= 3001:
    print("Has a good financial status")

else:
    print("You are in the red")