import random
import os
import time

def clear():
    os.system("clear")

# Set of instructions for Rock-Paper-Scissors
def rpsls_instructions():

    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Scissors")
    print()
    
    
#minimax based on my eval function
def minimax(turn, tie, last_move):
    if turn == 0:
        return random.randint(0, 2)
    elif tie==False:
        return last_move
    else:
        return minimax (turn-1, tie, last_move)
    

#game loop for Rock-Paper-Scissors
def rpsls():
    
    global rps_table
    global game_map
    global name
    global game_turn
    
    game_turn = 0
    player_move = 0
    tie_game=True
    player_points = 0
    computer_points = 0
    # Game Loop for each game of Rock-Paper-Scissors
    while (True or player_points <= 2 or computer_points <=2):
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
        
        print()
        

        # Player Input
        player_last_move=player_move
        inp = input("Enter your move : ")

        if inp.lower() == "help":
            clear()
            rpsls_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break	
        elif inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1		
        elif inp.lower() == "scissors":
            player_move = 2	
        else:
            clear()
            print("Wrong Input!!")
            rpsls_instructions()	
            continue

        #Handling users input
        print("Computer making a move....")
        
        comp_move = minimax(game_turn, tie_game, player_last_move)
        print()
        time.sleep(2)
    

        print("Computer chooses ", game_map[comp_move].upper())

        winner = rps_table[player_move][comp_move]
        game_turn+=1
        print()
        if winner == player_move:
            print(name, "WINS!!!")
            player_points+=1
            print("Player Points:", player_points , " Computer Points:" , computer_points)
            tie_game=False
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
            computer_points+=1
            print("Player Points:", player_points , " Computer Points:" , computer_points)
            tie_game=False
        else:
            print("TIE GAME")
            player_points+=.5
            computer_points+=.5
            print("Player Points:", player_points , " Computer Points:" , computer_points)
            tie_game=True		
        print()
        time.sleep(2)
        clear()
        

# The main function
if __name__ == '__main__':

    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors"}
    
    # Win-Lose Matrix for Rock-Paper-Scissors
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

    
    name = input("Enter your name: ")

    # The GAME LOOP
    while True:

        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to quit")
        print()

        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")	
            continue

        # Play the game
        if choice == 1:
            rpsls()

        # Quit the GAME LOOP 	
        elif choice == 2:
            break

        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")

                            