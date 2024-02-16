import pygame
import drawXO
import random

#Used in Handling of Human Inputs
WaitHumanLatch = False

def isBoardFull(board:list) -> bool:
    """

Checks the board is completely filled or not and Returns True if Filled or False if not filled

    """
    for i in range(3):
        for j in range(3):
            #Loops Through All the Board
            if board[i][j] == "":
                isBoardFull = False
                return isBoardFull
    isBoardFull = True
    return isBoardFull


def PlayMove(pos,screen,board,Avialable_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver,waitforhuman=False) -> None:
    """
    
This function takes in a tuple of (x,y) Then draws the CurrentPlayer into the board and changes the board properties accordingly
This function is also capable of handling Human inputs by waiting for Humans to complete

    """
    
    #Error Handling
    if pos == []:
        #print("Position is Empty")
        return
    #Decompose location x,y as i and j
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
        return
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
    """
    
Changes the CurrentPlayer

    """
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return currentPlayer


def CheckGameStatus(board) -> str:
    """

This Function is used To Return Three outputs namely "Winner" if winner is found then finds the which row/column or diagonal
is needed to be striken and also a gamestate Function
[0] -> Winner -> ["Null","X","O","Tie"]
[1] -> Row/Column/Diagonal -> ["Null","Veritical[0-2]","Horizontal[0-2]","Diagonal[1-2]"]
[2] -> GameState -> isGameOver : bool

    """
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
                #Loops thorough all elements of the board
                if board[i][j] == '':
                    #increases the available spot by one
                    spotAvailable =+ 1
        if spotAvailable == 0: #Checks if it is not increased
            isGameOver = True
            return ("Tie","Null",isGameOver) 
        else: 
            isGameOver = False
            return winner,"Null",isGameOver
        

def PlayRandomly(board,Avialable_Space,currentPlayer) -> list:
    """
    
This Function Generates a random coordinates which is a 100% empty Spot
(i,j) -> Indices free on the board (ie empty spot)

    """
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
    """
    
This Function used to handle the Human input By using pygame's MOUSEBUTTONDOWN event and also with get_pos()
Takes input as Board and Clicked (From event handler) and draws the respective place with CurrentPlayer
This also uses pygames's collide.point() method of rect to see mouse collision with rectangle
It also returns True if human's turn is over which is helpfull for further handling of input

    """
    #Check if the player has won
    isGameOver = CheckGameStatus(board)[2]
    if isGameOver == True:
        return
    
    #Get mouse position
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

    #looping thorigh each and every rectangle one by one
    for rect in AllRect:
        
        #Debugging
        # col = "RED"
        # if rect.collidepoint(mouseX,mouseY) and Clicked == True:
        #     col = "GREEN"
        #     print("Clicked on ",rect.center) 
        # pygame.draw.rect(screen,col, rect, 1)
        # print(isGameOver)
        
        if isGameOver != True:
            if rect.collidepoint(mouseX,mouseY) and Clicked == True:
                #Checks Collision and also Mouse Clicked Event
                
                #convert The coordinates of rectangles to Indices of the board
                j = int((rect.center[0] - CentreX - Charwidth )//Charwidth +2)
                i = int((rect.center[1] - CentreY - Charwidth )//Charwidth +2)

                #Debugging
                #print(i,j)
                #print(currentPlayer)
                #print(isGameOver)

                #Draws X
                if currentPlayer == "X" and Avialable_Space[i][j]!= 0 and isGameOver == False:
                    board[i][j] = "X"
                    Avialable_Space[i][j] = 0
                    drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)
                    #print("Drawn X")
                    HumanMoved = True
                #Draws O
                if currentPlayer == "O" and Avialable_Space[i][j]!= 0 and isGameOver == False:
                    board[i][j] = "O"
                    Avialable_Space[i][j] = 0
                    drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)
                    #print("Drawn O")
                    HumanMoved = True
                #Check if the player has won
                isGameOver = CheckGameStatus(board)[2]
    return HumanMoved


def HumanVsHuman(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) -> str:
        """
        
Simple Function that uses other functions to make a game between two humans

        """
        if HumanMove(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
        #Change player
            currentPlayer = nextTurn(currentPlayer)
        return currentPlayer
        
def HumanVsComputer(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer,isGameOver:bool,HumanFirst:bool = True) -> None:
    """
        
Simple Function that uses other functions to make a game between a human and a random playing bot
The turn can be decided by the HumanFirst bool

    """
    global WaitHumanLatch
    if HumanFirst == True:
        if HumanMove(screen,board,Avialable_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
            currentPlayer = nextTurn(currentPlayer)
            PlayMove(PlayRandomly(board,Avialable_Space,currentPlayer),screen,board,Avialable_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver)
            currentPlayer = nextTurn(currentPlayer)
            return currentPlayer

def HumanVsComputerMiniMax(screen,board,Available_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer,isGameOver:bool,HumanFirst:bool = True) -> None:
    """
    
This is a simple function that creates a game between Humans vs MiniMax
Where the turn is decided by the HumanFirst bool

    """
    global WaitHumanLatch
    if HumanFirst == True:
        if HumanMove(screen,board,Available_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
            currentPlayer = nextTurn(currentPlayer)
            PlayMove(bestMoveO(board),screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver)
            currentPlayer = nextTurn(currentPlayer)
            return currentPlayer

    else:
        TmpVariable = currentPlayer
        currentPlayer = PlayMove(bestMoveX(board),screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver,True)
        if currentPlayer == 0:  #This is used to handle error due to wrong retuning of some functions
            currentPlayer = TmpVariable
        currentPlayer = nextTurn(currentPlayer)
        if HumanMove(screen,board,Available_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer) == True:
            currentPlayer = nextTurn(currentPlayer)
            WaitHumanLatch = False
            PlayMove(bestMoveX(board),screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver,True)
            return currentPlayer
        return currentPlayer


def minimax(board,depth,isMaximizing) -> int:
    """
    
This is a algorithm that recussively checks whole possible branches of the game and decides the best one with help of score
Takes in Board and isMaximizing as input and returns a score which is based on first few lines in the function

    """
    #Check Result and assign the score 
    result = CheckGameStatus(board)[0]
    if result != "Null":
        if result == "X":
            score = 1
        if result == "O":
            score = -1
        if result == "Tie":
            score = 0  
        return score
      
    if isMaximizing: #
        bestScore = -10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    #Checks the free available locaiton
                    board[i][j] = "X"
                    #Plays at the free location
                    score = minimax(board,depth + 1,False) #Recursively calls the Funtion on the modified board again and again in child board till a end of tree is evaluated
                    board[i][j] = ""
                    #Reset the Board back to the original
                    board[i][j] = ""
                    bestScore = max(bestScore,score)
        return bestScore
    else:
        bestScore = 10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    #Checks for free available location
                    board[i][j] = "O"
                    #Plays at the free location
                    score = minimax(board,depth + 1,True)  #Recursively calls the Funtion on the modified board again and again in child board till a end of tree is evaluated
                    board[i][j] = ""
                    bestScore = min(bestScore,score)
        return bestScore
    
def bestMoveX(board):
    """
    
This is a simple function that uses minimax to find the best move for X at the current postion of board

    """
    bestScore = -10000
    bestMoveX = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score = minimax(board,0,False)
                board[i][j] = ""
                if score > bestScore:
                    bestScore = score
                    bestMoveX = [i,j]
    return bestMoveX

def bestMoveO(board):
    """
    
This is a simple function that uses MiniMax to find the best move for O at the current postion of board

    """
    bestScore = 10000
    bestMoveO = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board,0,True)
                board[i][j] = ""
                if score < bestScore:
                    bestScore = score
                    bestMoveO = [i,j]

    return bestMoveO

def MinimaxVsMinimax(screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver):
    PlayMove(bestMoveX(board),screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver)
    currentPlayer = nextTurn(currentPlayer)
    PlayMove(bestMoveO(board),screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver)
    currentPlayer=nextTurn(currentPlayer)