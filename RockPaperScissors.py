# ROCK PAPER SCISSORS
import os
from time import sleep
import random
def RPS():
    n=int(input('To win: '))
    print()
    Player=0
    Comp=0
    rps=['Rock','Paper','Scissors']
    draw=0
    print('Keep in mind,only valid inputs are ',rps)
    sleep(3)
    while Player<n and Comp<n:
        os.system('cls')
        print('You=',Player,'CPU=',Comp)
        print()
        a=input('You: ')
        b=random.choice(rps)
        if a==b:
            draw+=1
        elif a=='Rock':
            if b=='Paper':
                Comp+=1
            elif b=='Scissors':
                Player+=1
        elif a=='Paper':
            if b=='Scissors':
                Comp+=1
            elif b=='Rock':
                Player+=1
        elif a=='Scissors':
            if b=='Rock':
                Comp+=1
            elif b=='Paper':
                Player+=1
        else:
            print('You must Enter only specified inputs\n')
        print()
        print("Computer: ",b)
        print()
        print('You=',Player,'CPU=',Comp)
        sleep(2)
    if Player>Comp:
        print('\n\nCongratulations,You won\n\n')
    elif Comp>Player:
        print('\n\nOops, you lost \nBetter Luck Next time XD\n')
RPS()
