#21. La empresa Auteco de motocicletas tiene una promoción de mitad de año, que consiste en lo siguiente. Las motos marca Honda tienen un descuento del 4%, las marcas Yamaha del 7% y las Suzuki del 15%, las otras marcas 3%.

valueMotorcycle = int(input("Insert the value of the motorcycle: "))
disccountHonda = valueMotorcycle * 0.04
totalHonda = valueMotorcycle - disccountHonda
disccountYamaha = valueMotorcycle * 0.07
totalYamaha = valueMotorcycle - disccountYamaha
disccountSuzuki = valueMotorcycle * 0.15
totalSuzuki = valueMotorcycle - disccountSuzuki
disccountother = valueMotorcycle * 0.03
totalOther = valueMotorcycle - disccountother

def mot (typeMotorcycle):
    
    if typeMotorcycle == "honda" or typeMotorcycle == "HONDA":
        print(f"Motorcycle Honda: {totalHonda}")
    elif typeMotorcycle == "yamaha" or typeMotorcycle == "YAMAHA":
        print(f"Motorcycle Yamaha: {totalYamaha}")
    elif typeMotorcycle == "suzuki" or typeMotorcycle == "SUZUKI":
        print(f"Motorcycle Suzuki: {totalSuzuki}")
    elif typeMotorcycle == "other" or typeMotorcycle == "OTHER":
        print(f"Other Motorcycle: {totalOther}")
    else:
        print("Este tipo de moto no exisite.")
    
mot (typeMotorcycle=input("Insert motorcycle type: "))