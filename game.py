import random

def game( a , b ):
    if a == "Snake":
       if b == "Snake":
        print("Hey, Game Tied")
       elif b == "Gun":
        print("HAHA, Player2 wins and Player1 Loses")
       elif b == "Water":
        print("HAHA Player2 wins and Player1 loses")
    if a == "Water":
       if b == "Water":
        print("Hey, Game Tied")
       if b == "Gun":
        print("HAHA, PLayer1 wins and Player2 Loses")
       if b == "Snake":
        print("HAHA Player2 wins and Player2 loses")

    if a == "Gun":
       if b == "Gun":
        print("Hey, Game Tied")
       if b == "Snake":
        print("HAHA, Player1 wins and Player2 Loses")
       if b == "Water":
        print("HAHA Player2 wins and Player1 loses")


print("Hey player1! What do you pick? Snake or Water or Gun?:")
player1 = random.randint( 1 , 3 )
if player1 == 1:
    player1 = "Snake"
elif player1 == 2:
    player1 = "Water"
else:
    player1 = "Gun"
print(player1)

player2 = input("Hey Player 2! What do you pick? Snake or Water or Gun?:\n")
game(player1, player2)

