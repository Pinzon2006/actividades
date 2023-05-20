#3. Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso, nota definitiva, el nro de clases en el semestre y el número de las fallas. En el caso de que las fallas superen el 30% del número de clases se debe mostrar la nota que no aprobó y se calificara cero(0).

name = input("Enter your Name: ")
curse = input("Enter the name of the course: ")
noted = float(input("Enter the final grade: "))
nclass = int(input("Enter the number of classes for the semester: "))
nfails = int(input("Enter number of failures: "))
notef = nclass * 0.3

if nfails <= notef:
    print(f"\n\nInformacion Semestre: \nName: {name}\nCourse: {curse}\nFinal Note: {noted}\nN° Classes: {nclass}\nN° Fails: {nfails}")
    
else:
    noted = 0
    print(f"\n\nInformacion Semestre: \nName: {name}\nCourse: {curse}\nFinal Note: {noted}\nN° Classes: {nclass}\nN° Fails: {nfails}")