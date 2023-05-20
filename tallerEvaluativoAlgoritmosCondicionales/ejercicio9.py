#9. Determinar si un aprendiz aprueba o reprueba una formación, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 10; reprueba en caso contrario.

name = input("Insert your name: ")
formation = input("Insert the name of the formation: ")
note1 = int(input("Insert note 1: "))
note2 = int(input("Insert note 2: "))
note3 = int(input("Insert note 3: "))
average = (note1 + note2 + note3)/3

if average >= 10:
    print("You have passed the training")
    
else:
    print("You have not passed the training")