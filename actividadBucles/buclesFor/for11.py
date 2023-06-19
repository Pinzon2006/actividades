#11. Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.

def temperatures():
    numTemperatures = int(input("Insert the number of temperatures: "))

    totalTemperature = 0
    highestTemperature = float("-inf")
    lowestTemperature = float("inf")

    for i in range(numTemperatures):
        
        temperature = float(input(f"Ingrest the temperature {i + 1}: "))

        totalTemperature += temperature

        if temperature > highestTemperature:
            highestTemperature = temperature

        if temperature < lowestTemperature:
            lowestTemperature = temperature

    averageTemperature = totalTemperature / numTemperatures

    print(f"Highest Temperature: {highestTemperature}\nLowest Temperature: {lowestTemperature}\nAverage Temperature: {averageTemperature}")

temperatures()
