#Realizar el siguente algoritmo
#Entrada: Un numero que se almacena en una variable llamada numeroDia
#Proceso: Realizar las respectivas comparaciones para cada uno de los valores entre 1 y 7
#Salida: Mostrar el nombre del dia segun el valor contenido en numeroDia

def week (numberDay):
    
    if numberDay == 1:
        print(f"{numberDay} corresponds to Monday")
    
    elif numberDay == 2:
        print(f"{numberDay} corresponds to Tuesday")
    
    elif numberDay == 3:
        print(f"{numberDay} corresponds to Wednesday")
    
    elif numberDay == 4:
        print(f"{numberDay} corresponds to Thursday")
    
    elif numberDay == 5:
        print(f"{numberDay} corresponds to Friday")
    
    elif numberDay == 6:
        print(f"{numberDay} corresponds to Saturday")
    
    elif numberDay == 7:
        print(f"{numberDay} corresponds to Sunday")
        
    else:
        print(f"{numberDay} is not a day of the week")
        
week(numberDay=int(input("Insert a number from 1 to 7: ")))