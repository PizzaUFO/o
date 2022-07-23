#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def display_board(cellDict):
    print(f"       |       |\n   {cellDict['7']}   |   {cellDict['8']}   |   {cellDict['9']}   \n_______|_______|_______\n       |       |\n   {cellDict['4']}   |   {cellDict['5']}   |   {cellDict['6']}   \n_______|_______|_______\n       |       |\n   {cellDict['1']}   |   {cellDict['2']}   |   {cellDict['3']}   \n       |       |       ")


# In[ ]:


def check_if_won(cellDict):
    for num in[1,4,7]:
        if cellDict[str(num)] == cellDict[str(num+1)] == cellDict[str(num+2)]:
            if cellDict[str(num)] == 'X':
                return 1
            elif cellDict[str(num)] == 'O':
                return 2
    for num in range(1,4):
        if cellDict[str(num)] == cellDict[str(num+3)] == cellDict[str(num+6)]:
            if cellDict[str(num)] == 'X':
                return 1
            elif cellDict[str(num)] == 'O':
                return 2
    for numList in[[3,5,7],[1,5,9]]:
        if numList[0] == numList[1] == numList[2]:
            if cellDict[str(num)] == 'X':
                return 1
            elif cellDict[str(num)] == 'O':
                return 2
    return 0


# In[ ]:


def play_game():
    cellDict = {}
    playerTurn = [1,'X']
    gameIsOver = False
    for num in range(1,10):
        cellDict[str(num)] = ' '
    while gameIsOver == False:
        display_board(cellDict)
        print(f"Player {playerTurn[0]}, it's your turn\n")
        choice = input("What spot do you want?")
        if choice not in [str(x) for x in range(1,10)]:
            choiceIsValid = False
            while choiceIsValid == False:
                choice = input("What you entered is invalid. Try again.\n")
                if choice in [str(x) for x in range(1,10)]:
                    if cellDict[choice] == ' ':
                        choiceIsValid = True
        elif cellDict[choice] != ' ':
            choiceIsValid = False
            while choiceIsValid == False:
                choice = input("What you entered is invalid. Try again.\n")
                if choice in [str(x) for x in range(1,10)]:
                    if cellDict[choice] == ' ':
                        choiceIsValid = True
        cellDict[choice] = playerTurn[1]
        wonStatus = check_if_won(cellDict)
        if wonStatus == 1 or wonStatus == 2:
            display_board(cellDict)
            print(f"Player {wonStatus} wins!")
            gameIsOver = True
        if playerTurn[0]==1:
            playerTurn = [2,'O']
        else:
            playerTurn = [1,'X']
        


# In[ ]:


play_game()


# In[ ]:





# In[ ]:




