# Stone Paper Scissor

import random

random_number=random.randint(1,3)
computer_turn=random_number
player_turn=input("Stone(st), Paper(p), Scissor(sc)\nEnter your choice:-")

if random_number==1:
    computer_turn="stone"
elif random_number==2:
    computer_turn="paper"
elif random_number==3:
    computer_turn="scissor"

def game_win():
    print(f'Computer select {computer_turn}.')
    if player_turn=="st":
        if computer_turn=="stone":
            print("Its a tie")
        elif computer_turn=="paper":
            print("You loose.")
        elif computer_turn=="scissor":
            print("Yupp. You win.")

    elif player_turn=="p":
        if computer_turn=="stone":
            print("Yupp. You win.")
        elif computer_turn=="paper":
            print("Its a tie")
        elif computer_turn=="scissor":
            print("You loose.")

    elif player_turn=="sc":
        if computer_turn=="stone":
            print("You loose.")
        elif computer_turn=="paper":
            print("Yupp. You win")
        elif computer_turn=="scissor":
            print("Its a tie.")
game_win()