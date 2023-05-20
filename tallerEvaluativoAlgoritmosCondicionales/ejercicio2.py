#2. Diseñe un algoritmo que, al ingresar la edad del usuario, si es mayor de edad mostrar el un mensaje “es mayor de edad”.

edad = int(input("Enter your age: "))

if edad >= 18:
    print("You are of legal age")
    
else:
    print("You are a minor")