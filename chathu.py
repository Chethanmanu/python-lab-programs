'''Take it in turns to roll the dice. Move your counter forward the number of spaces shown
on the dice. If your counter lands at the bottom of a ladder, you can move up to the top of
the ladder. If your counter lands on the head of a snake, you must slide down to the bottom
of the snake.'''
import time
import random

def Roll_dice():
    return random.randint(1,6)

def Move(Player, value, P1N, P2N, P3N, P4N):
    snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
    ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
    Throw = Roll_dice()
    if Player == 1:
        num = value + Throw
        print(P1N, "Rolled a", Throw, "And is now on", num)
    if Player == 2:
        num = value + Throw
        print(P2N, "Rolled a", Throw, "And is now on", num)
    if Player == 3:
        num = value + Throw
    print(P3N, "Rolled a", Throw, "And is now on", num)
    if Player == 4:
        num = value + Throw
        print(P4N, "Rolled a", Throw, "And is now on", num)
    if num in snake_squares:
        print("Player got bitten by a snake and is now on square", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        print("Player climbed a ladder and is now on square", ladder_squares[num])
        num = ladder_squares[num]
    else:
        print("",end = "")
    return num

def Setup_Players():
    players=6
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 2:
                print("Must be less than 5 and greater than 1")
            else:
                return players
        except:
            print("Must be a number")



def Player_Names(NumP):
    Names = []
    for i in range(1,NumP+1):
        Names.append(input("What is the name of Player"+str(i)+"?"))
    Names.append("")
    return Names


Num_Players=Setup_Players()
P_Names = Player_Names(Num_Players)
P1N = 0
P2N = 0
P3N = 0
P4N = 0
for i in P_Names:
    if P1N == 0:
        P1N = i
        if Num_Players == 1:
            P2N, P3N, P4N = "", "", ""
            break
    elif P2N == 0:
        P2N = i
        if Num_Players == 2:
            P3N, P4N = "", ""
            break
    elif P3N == 0:
        P3N = i
        if Num_Players == 3:
            P4N = ""
            break
    elif P4N == 0:
        P4N = i
    else:
        break
print(P1N, P2N, P3N, P4N, ", Welcome To Snakes And Ladders")
input("Press Enter")
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
x = 0
while Num1 < 100 and Num2 < 100 and Num3 < 100 and Num4 < 100:       
    while x < Num_Players:
        x=x+1
        if x == 1:
            Num1 = Move(1, Num1, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num1 > 99:
                print(P1N, "WINS!")
                time.sleep(3)
                exit()
        if x == 2:
            Num2 = Move(2, Num2, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num2 > 99:
                print(P2N, "WINS!")
                time.sleep(3)
                exit()            
        if x == 3:
            Num3 = Move(3, Num3, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num3 > 99:
                print(P3N, "WINS!")
                time.sleep(3)
                exit()
        if x == 4:
            Num4 = Move(4, Num4, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num4 > 99:
                print(P4N, "WINS!")
                time.sleep(3)
                exit()
    x=0
