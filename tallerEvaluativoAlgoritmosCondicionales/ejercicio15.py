#15. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 15% sobre el total de la compra y si son menos de 3 camisas el descuento es del 5%.

price = int(input("Insert shirt price: "))
shirts = int(input("Insert the number of shirts purchased: "))

if shirts >= 3:
    subtotal1 = (price * shirts)
    discount1 = subtotal1 * 0.15
    total1 = subtotal1 - discount1
    print(f"The final price is: {total1}")
    
else:
    subtotal2 = (price * shirts)
    discount2 = subtotal2 * 0.05
    total2 = subtotal2 - discount2
    print(f"The final price is: {total2}")