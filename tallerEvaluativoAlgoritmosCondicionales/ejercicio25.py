#25. Escriba un programa que permita adivinar un personaje de Marvel en base a las tres preguntas siguientes:
# a. ¿Puede volar?
# b. ¿Es humano?
# c. ¿Tiene máscara?

listOfCharacters = ["Spider Man","Doctor Strange","Thor","Hulk","Antman"]

def guess (quest1, quest2, quest3):

    if quest1 == "yes":
        
        if quest2 == "yes":
                
            if quest3 == "no":
                print(f"Your characters can be: {listOfCharacters[1]}")
            
        elif quest2 == "no":
                
            if quest3 == "no":
                print(f"Your characters can be: {listOfCharacters[2]}")
            
    elif quest1 == "no":
        
        if quest2 == "yes":
            
            if quest3 == "yes":
                print(f"Your characters can be: {listOfCharacters[0,4]}")
                
            elif quest3 == "no":
                print(f"Your characters can be: {listOfCharacters[3]}")
        
    else:
        print("This character is not in the current list")
    
print("Please answer yes or no to the following questions")
guess(quest1=input("Can it fly ?: "), quest2=input("It is human?: "), quest3=input("Does it have a mask?: "))


#spiderMan = no yes yes
#doctorStrange = yes yes no
#thor = yes no no
#hunk = no yes no
#antman = no yes yes