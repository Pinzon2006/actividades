#5. Un hombre desea saber cuánto dinero se genera por concepto de intereses en relación la cantidad que tiene en inversión en el banco.
# El decidirá reinvertir los intereses siempre y cuando estos no excedan a $7000, y en ese caso diseña un algoritmo para saber cuánto dinero tendrá finalmente en su cuenta

value = float(input("Enter the amount to invest: "))

if value <= 7000:
    print("You can reinvest the interest")
    
else:
    print("You cannot reinvest interest")