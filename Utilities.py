import pygame
import drawXO
import random

WaitHumanLatch = False

def isBoardFull(board) -> bool:
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                isBoardFull = False
                return isBoardFull
    isBoardFull = True
    return isBoardFull


def PlayMove(pos,screen,board,Avialable_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver,waitforhuman=False) -> None:
    i,j = pos
    global WaitHumanLatch
    #Check if the player has won
    isGameOver = CheckGameStatus(board)[2]
    if isGameOver == True:
        return 0
    if WaitHumanLatch == True:
        return 0
    
    #Checking if the space is available
    if Avialable_Space[i][j] == 0 and isBoardFull(board) == False:
        print("Space is not available")
    else: 
        if currentPlayer == "X" and Avialable_Space[i][j]!= 0 and isGameOver == False and WaitHumanLatch == False:
            board[i][j] = currentPlayer
            Avialable_Space[i][j] = 0
            drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)
            
        if currentPlayer == "O" and Avialable_Space[i][j]!= 0 and isGameOver == False and WaitHumanLatch == False:
            board[i][j] = currentPlayer
            Avialable_Space[i][j] = 0
            drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)
    if waitforhuman == True:
        currentPlayer = nextTurn(currentPlayer)
        WaitHumanLatch = True
        return currentPlayer

def nextTurn(currentPlayer) -> str:
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return currentPlayer


def CheckGameStatus(board) -> str:
    winner = "Null"
    #Checking Vertical
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != "":
            isGameOver = True
            winner = board[i][0]
            
            return (winner,"Vertical"+str(i),isGameOver)
      
    #Checking Horizontal
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "":
            isGameOver = True
            winner = board[0][i]
            
            return (winner,"Horizontal"+str(i),isGameOver)

    #Checking Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "":
        isGameOver = True
        winner = board[0][0]
        return (winner,"Diagonal1",isGameOver)
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "":
        isGameOver = True
        winner = board[0][2]
        return (winner,"Diagonal2",isGameOver)
    else:
        spotAvailable = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    spotAvailable =+ 1
        if spotAvailable == 0:
            isGameOver = True
            return ("Tie","Null",isGameOver) 
        else: 
            isGameOver = False
            return winner,"Null",isGameOver
        

def PlayRandomly(board,Avialable_Space,currentPlayer) -> list:
    #Check if the player has won
    isGameOver = CheckGameStatus(board)[2]
    if isGameOver == True:
        return (0,0)
    #Randomly choosing the row and column
    i = random.randint(0,2)
    j = random.randint(0,2)
    
    #Checking if the space is available
    if Avialable_Space[i][j] == 0 and isBoardFull != True:
        return PlayRandomly(board,Avialable_Space,currentPlayer)
    else: 
       return (i,j)
    

def HumanMove(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) -> bool:
    #Check if the player has won
    isGameOver = CheckGameStatus(board)[2]
    if isGameOver == True:
        return
    mouseX,mouseY = pygame.mouse.get_pos()
    HumanMoved = False

    #Creating all the collition rectangles
    rect1_1 = pygame.Rect(CentreX - 1.5*Charwidth, CentreY - 1.5*Charwidth, Charwidth, Charwidth)
    rect1_2 = pygame.Rect(CentreX - 0.5*Charwidth, CentreY - 1.5*Charwidth, Charwidth, Charwidth)
    rect1_3 = pygame.Rect(CentreX + 0.5*Charwidth, CentreY - 1.5*Charwidth, Charwidth, Charwidth)
    rect2_1 = pygame.Rect(CentreX - 1.5*Charwidth, CentreY - 0.5*Charwidth, Charwidth, Charwidth)
    rect2_2 = pygame.Rect(CentreX - 0.5*Charwidth, CentreY - 0.5*Charwidth, Charwidth, Charwidth)
    rect2_3 = pygame.Rect(CentreX + 0.5*Charwidth, CentreY - 0.5*Charwidth, Charwidth, Charwidth)
    rect3_1 = pygame.Rect(CentreX - 1.5*Charwidth, CentreY + 0.5*Charwidth, Charwidth, Charwidth)
    rect3_2 = pygame.Rect(CentreX - 0.5*Charwidth, CentreY + 0.5*Charwidth, Charwidth, Charwidth)
    rect3_3 = pygame.Rect(CentreX + 0.5*Charwidth, CentreY + 0.5*Charwidth, Charwidth, Charwidth)
    
    AllRect = [rect1_1,rect1_2,rect1_3,rect2_1,rect2_2,rect2_3,rect3_1,rect3_2,rect3_3]

    #Testing:
    for rect in AllRect:
        col = "RED"
        if rect.collidepoint(mouseX,mouseY) and Clicked == True:
            col = "GREEN"
            print("Clicked on ",rect.center) 
        pygame.draw.rect(screen,col, rect, 1)
        #print(isGameOver)
        if isGameOver != True:
            if rect.collidepoint(mouseX,mouseY) and Clicked == True:
                
                j = int((rect.center[0] - CentreX - Charwidth )//Charwidth +2)
                i = int((rect.center[1] - CentreY - Charwidth )//Charwidth +2)

                print(i,j)
                print(currentPlayer)
                print(isGameOver)
                if currentPlayer == "X" and Avialable_Space[i][j]!= 0 and isGameOver == False:
                    board[i][j] = "X"
                    Avialable_Space[i][j] = 0
                    print("Drawn X")
                    drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)
                    HumanMoved = True
                if currentPlayer == "O" and Avialable_Space[i][j]!= 0 and isGameOver == False:
                    board[i][j] = "O"
                    Avialable_Space[i][j] = 0
                    print("Drawn O")
                    drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)
                    HumanMoved = True
                #Check if the player has won
                isGameOver = CheckGameStatus(board)[2]
    return HumanMoved


def HumanVsHuman(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) -> None:
        if HumanMove(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
        #Change player
            currentPlayer = nextTurn(currentPlayer)
        return currentPlayer
        
def HumanVsComputer(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer,isGameOver:bool,HumanFirst:bool = True) -> None:
    global WaitHumanLatch
    if HumanFirst == True:
        if HumanMove(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
            currentPlayer = nextTurn(currentPlayer)
            PlayMove(PlayRandomly(board,Avialable_Space,currentPlayer),screen,board,Avialable_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver)
            currentPlayer = nextTurn(currentPlayer)
            return currentPlayer

    else:
        TmpVariable = currentPlayer
        currentPlayer = PlayMove(PlayRandomly(board,Avialable_Space,currentPlayer),screen,board,Avialable_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver,True)
        if currentPlayer == 0:
            currentPlayer = TmpVariable
        currentPlayer = nextTurn(currentPlayer)
        if HumanMove(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
            currentPlayer = nextTurn(currentPlayer)
            WaitHumanLatch = False
            PlayMove(PlayRandomly(board,Avialable_Space,currentPlayer),screen,board,Avialable_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver,True)
            return currentPlayer
        return currentPlayer


# def minimax(board,depth,isMaximizing) -> int:
#     score = 0
#     if evaluation(board)!= None:
#         score = evaluation(board)
#         print(score)
#         return score
#     if isMaximizing:
#         bestScore = -10000

#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == "":
#                     board[i][j] = currentPlayer
#                     nextTurn()

#                     if evaluation(board) != None:
#                         score = minimax(board,depth + 1,False)
#                     board[i][j] = ""
#                     bestScore = max(bestScore,score)
#         return bestScore
#     else:
#         bestScore = 10000

#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == "":
#                     board[i][j] = currentPlayer
#                     score = minimax(board,depth + 1,True)
#                     board[i][j] = ""
#                     bestScore = min(bestScore,score)
#         return bestScore
    
# def bestMove(board,currentPlayer,isGameOver):
#     bestScore = -10000
#     bestMove = []
#     score = 0
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == "":
#                 board[i][j] = currentPlayer
#                 score = minimax(board,0,False)
#                 board[i][j] = ""
#                 if score > bestScore:
#                     bestScore = score
#                     bestMove = [i,j]
#     print(bestMove)
#     return bestMove

# def evaluation(board):
#     if CheckGameStatus(board)[0] == "X":
#         return 1
#     if CheckGameStatus(board)[0] == "O":
#         return -1
#     if CheckGameStatus(board)[0] == "Draw":
#         return 0
#     else:
#         return None

