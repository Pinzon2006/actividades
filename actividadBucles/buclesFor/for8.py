#8.	Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

def functionAverage (n):
    
    sum = 0
    
    for i in range (n):
        
        note = float(input(f"Insert the note {i + 1}: "))
        sum += note
        
    average = sum / n
    
    return average
        
numNotes = int(input("Insert the number of notes: "))
average = functionAverage(numNotes)
print(f"The average score is: {average}")