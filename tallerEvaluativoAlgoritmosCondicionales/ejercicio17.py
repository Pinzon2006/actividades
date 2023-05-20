#17. Hacer un programa que pida dos números y los imprima en forma ascendente y descendente.

list = []
value1 = int(input("Insert a number: "))
value2 = int(input("Insert another number: "))

list.append(value1)
list.append(value2)

print(f"\nthe values to add are: {value1} and {value2}")

list.sort()

print(f"\nAscending List: {list}")

list.reverse()

print(f"\nDescending List: {list}")