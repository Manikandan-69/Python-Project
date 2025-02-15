import random

def game_starts():
    Player1_Score=0
    Player2_Score=0
    n=1
    while n<=3:
        Player1=input("Select Rock, Paper, or Scissor :").title()
        Player2=random.choice(['Rock','Paper','Scissor']).title()
        print("Player 2 selected: ",Player2)

        if Player1==Player2 :
            print("Try Again")
        elif (Player1=='Rock' and Player2=='Scissor') or (Player1=='Paper' and Player2=='Rock') or (Player1=='Scissor' and Player2=='Paper'):
            print("Player 1 Win!!")
            Player1_Score=Player1_Score+1
            n=n+1
        elif (Player1=='Rock' and Player2=='Paper') or (Player1=='Paper' and Player2=='Scissor') or (Player1=='Scissor' and Player2=='Rock'):
            print("Player 2 Win!!")
            Player2_Score=Player2_Score+1
            n=n+1
    return (f"Player1 Score: {Player1_Score} , Player2 Score: {Player2_Score}")

RPS=game_starts()
print(RPS)
    