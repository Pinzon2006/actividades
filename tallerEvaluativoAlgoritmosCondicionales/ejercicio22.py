#22. A un trabajador le descuentan de su sueldo el 4%, si su sueldo es menor o igual a $1000000, si el sueldo está entre $1000000 y $2000000 el 7%, y por encima de 2000000 el 8% calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo.

salary = int(input("Insert your salary: "))
disccount1 = salary * 0.04
total1 = salary - disccount1
disccount2 = salary * 0.07
total2 = salary - disccount2
disccount3 = salary * 0.08
total3 = salary - disccount3

if salary <= 1000000:
    print(f"Your finaly salary is: {total1}")
    
elif salary in range (1000001,1999999):
    print(f"Your finaly salary is: {total2}")
    
elif salary >= 2000000:
    print(f"Your finaly salary is: {total3}")
    
else:
    print("Error")