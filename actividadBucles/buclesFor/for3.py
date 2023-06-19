#3. Escribir un programa que pida el nombre al usuario y lo muestre 10 veces por pantalla.

nameUser = input("Insert your name: ")

for num in range (1, 11):
    print(f"{num}. Hello {nameUser}")