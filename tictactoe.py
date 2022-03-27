# TIC TAC TOE 
from time import sleep
import os
def tictactoe(name1='Player 1',name2='Player 2'):
    
    print(f'Hello P1 {name1} and P2 {name2} ')
    
    import numpy as np
    a=np.array([(0,0,0),(0,0,0),(0,0,0)])        # Creating base Matrix
    Player1=[]                               # Moves of Player1
    Player2=[]                               # Moves of Player 2
    b=np.array([(1,2,3),(4,5,6),(7,8,9)])    # Block names
    print('Block numbers are: \n',b)
    
    # Mention all win Conditions
    winnings=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7]]
    
    count1=0     # bucket to check if Player1 has satisfied a win condition
    count2=0     # bucket to check if Player1 has satisfied a win condition
    print(a)
    print('\n\n')
    terms=0             # Check the number of terms and boxes filled  
    satisfied=0         # bucket to check if count1 or count2 has become 3
    
    
    while (count1!=3 and count2!=3) and terms!=9: # Looping until a player wins or all boxes are filled
        print('\n\n')
        
        p1=int(input('Player 1 Enter Block: '))   #P1 input and altering matrix accordingly
        Player1.append(p1)
        if p1==1 or p1==2 or p1==3:
            a[0][p1-1]=1
        elif p1==4:
            a[1][0]=1
        elif p1==5:
            a[1][1]=1
        elif p1==6:
            a[1][2]=1
        elif p1==7:
            a[2][0]=1
        elif p1==8:
            a[2][1]=1
        elif p1==9:
            a[2][2]=1
        os.system('cls')
        print(a)
        terms=0                       # Checking number of boxes filled by Iterating over matrix
        for i in range(3):
            for j in range(3):
                if a[i][j]!=0:
                    terms+=1
        if terms==9:
            break
            
        for i in winnings:        # Checking if a player has satisfied a win condition 
            count1=0              
            count2=0
            for j in i:           # Iterating over each win condition 
                if j in Player1:
                    count1+=1
                if j in Player2:
                    count2+=1
            if count1==3 or count2==3:  # Breaking as soon as a condition is satified
                satisfied=1
                break
        if satisfied==1:
            break            # Breaking the Big while loop
            
        p2=int(input('Player 2 Enter Block: ')) # P2 input and altering matrix accordingly
        Player2.append(p2)
        if p2==1 or p2==2 or p2==3:
            a[0][p2-1]=2
        elif p2==4:
            a[1][0]=2
        elif p2==5:
            a[1][1]=2
        elif p2==6:
            a[1][2]=2
        elif p2==7:
            a[2][0]=2
        elif p2==8:
            a[2][1]=2
        elif p2==9:
            a[2][2]=2
        os.system('cls')
        print(a)

        for i in winnings:                  # Checking if a player has satisfied a win condition 
            count1=0
            count2=0
            for j in i:                     # Iterating over each win condition 
                if j in Player1:
                    count1+=1
                if j in Player2:
                    count2+=1
            if count1==3 or count2==3:       # Breaking as soon as a condition is satified
                break
        
    if count1==3:
        print(f'\n\n{name1} wins')
    elif count2==3:
        print(f'\n\n{name2} wins')
    else:
        print('\n\nIts a draw')
tictactoe()