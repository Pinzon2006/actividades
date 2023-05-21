# 26. Escriba un programa en Python que acepte la opción de dos jugadoras en
# a. Piedra-Papel-Tijera y decida el resultado (solución).
# b. Entrada: persona1=piedra; persona2=papel
# c. Salida: Gana persona2: El papel envuelve a la piedra

def play (player1, player2):
    
    if player1 == "rock" and player2 == "scissors":
        print("Player 1 wins because rock breaks scissors")
    
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins because rock breaks scissors")
    
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins because paper wrapping rock")
        
    elif player2 == "paper" and player1 == "rock":
        print("Player 2 wins because paper wrapping rock")
        
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins because scissors cut paperr")
        
    elif player2 == "scissors" and player1 == "paper":
        print("Player 2 wins because scissors cut paperr")
        
    elif player1 == "rock" and player2 == "rock":
        print("Tie")
        
    elif player1 == "paper" and player2 == "paper":
        print("Tie")
        
    elif player1 == "scissors" and player2 == "scissors":
        print("Tie")
        
    else:
        print("This action cannot be performed")
        
play (player1 = input("Player 1 insert rock, paper or scissors: "), player2 = input("Player 2 insert rock, paper or scissors: "))