#5.	Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def program():
    
    totalSales = 0
    discount = 0

    while True:
        amount = float(input("Enter the invoice amount: "))

        if amount == 0:
            break

        totalSales += amount

    if totalSales > 1000:
        discount = totalSales * 0.1

    totalToPay = totalSales - discount

    print(f"Total sales: $ {totalSales}\nDiscount applied: $ {discount}\nTotal to pay: $ {totalToPay}")

program()