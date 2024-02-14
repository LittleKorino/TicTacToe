import pygame
import drawXO
import random

# pygame setup
pygame.init()
windowwidth = 1280
windowheight = 720
screen = pygame.display.set_mode((windowwidth, windowheight))
clock = pygame.time.Clock()
running = True

# Game setup
(CentreX,CentreY) = (windowwidth/2, windowheight/2)
Charwidth = 200


#To render Text in the canvas
text_font = pygame.font.SysFont('Arial', 50) 
def drawText(text:str, font:object, colour:str, surface:object, x:int, y:int) -> None:
    img = font.render(text, True, colour)
    surface.blit(img, (x, y))

# Set colours
darkmode = ["black","white"]
whitemode = ["white","black"]
boolDark = True


#Draw Border lines:
def DrawBorder(screen:object, colour:str) -> None:
     #Vertical lines
    #Refer the picture in readme for the position of the lines.
    pygame.draw.line(screen, color[1], (CentreX - 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX - 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    pygame.draw.line(screen, color[1], (CentreX + 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX + 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    
    #Horizontal lines
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY - 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY - 0.5*Charwidth) ), 10)
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY + 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY + 0.5*Charwidth) ), 10)

#Draw Board
def DrawBoard(board):
      for i in range(3):
        for j in range (3):
            if board[i][j] == "X":
                drawXO.drawX(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.7*Charwidth,color[1])
            elif board[i][j] == "O":
                drawXO.drawO(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.8*Charwidth,color[1])
            else:
                continue


#Board Setup
board = [["","",""],
        ["","",""],
        ["","",""]]

Avialable_Space =   [[1,1,1],
                    [1,1,1],
                    [1,1,1]]

player = ["X","O"]
currentPlayer = player[0]
isGameOver = False


# Check gameStatus
def CheckGameStatus(board,isGameOver) -> str:
    #Checking Vertical
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            isGameOver = True
            return (board[i][0],"Vertical"+str(i),isGameOver)
      
    #Checking Horizontal
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            isGameOver = True
            return (board[0][i],"Horizontal"+str(i),isGameOver)

    #Checking Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        isGameOver = True
        return (board[0][0],"Diagonal1",isGameOver)
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        isGameOver = True
        return (board[0][2],"Diagonal2",isGameOver)
    else:
        isGameOver = False
        return "Continue",isGameOver

#Check board
def isBoardFull(board,isGameOver) -> bool:
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                isGameOver = False
                return isGameOver
    isGameOver = True
    return isGameOver

#Check which Row/column need to be striken
def DrawCrosssedLine(board) -> None:
    #Check Horizontal
    for i in range(3):
        if CheckGameStatus(board,isGameOver)[1] == "Horizontal"+str(i):
            pygame.draw.line(screen, "RED", (CentreX - Charwidth + i*Charwidth, CentreY - 1.5*Charwidth), (CentreX - Charwidth + i*Charwidth, CentreY + 1.5*Charwidth), 10)
    #Check verical
    for i in range(3):
        if CheckGameStatus(board,isGameOver)[1] == "Vertical"+str(i):
            pygame.draw.line(screen, "RED", (CentreX - 1.5*Charwidth, CentreY - Charwidth + i*Charwidth), (CentreX + 1.5*Charwidth, CentreY - Charwidth + i*Charwidth), 10)
    #Check the diagonals
    if CheckGameStatus(board,isGameOver)[1] == "Diagonal1":
            pygame.draw.line(screen, "RED", (CentreX - 1.5*Charwidth, CentreY - 1.5*Charwidth), (CentreX + 1.5*Charwidth, CentreY + 1.5*Charwidth), 10)
    if CheckGameStatus(board,isGameOver)[1] == "Diagonal2": 
            pygame.draw.line(screen, "RED", (CentreX - 1.5*Charwidth, CentreY + 1.5*Charwidth), (CentreX + 1.5*Charwidth, CentreY - 1.5*Charwidth), 10)

#Playing Randomly 
def PlayRandomly(board,currentPlayer,isGameOver) -> None:
    #Randomly choosing the row and column
    i = random.randint(0,2)
    j = random.randint(0,2)
    #Checking if the space is available
    if Avialable_Space[i][j] == 0 and isBoardFull == False:
        PlayRandomly(board,currentPlayer,isGameOver)
    else: 
        if currentPlayer == "X" and Avialable_Space[i][j]!= 0 and isGameOver == False:
            board[i][j] = currentPlayer
            Avialable_Space[i][j] = 0
            DrawBoard(board)
            
        if currentPlayer == "O" and Avialable_Space[i][j]!= 0 and isGameOver == False:
            board[i][j] = currentPlayer
            Avialable_Space[i][j] = 0
            DrawBoard(board)

#Returns the next player
def nextTurn(currentPlayer) -> str:
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return currentPlayer

#Check if the player has won
def CheckWin(board,isGameOver) -> None:
    #Checking the Winner:
    if CheckGameStatus(board,isGameOver)[0] == "X" :
        #print("X Won")
        drawText("X Won", text_font, color[1], screen, CentreX - 450, CentreY)
        isGameOver = True
    if CheckGameStatus(board,isGameOver)[0] == "O" :
        #print("O Won")
        drawText("O Won", text_font, color[1], screen, CentreX - 450, CentreY)
        isGameOver = True
    if isBoardFull(board,isGameOver) and isGameOver == False:
        #print("Draw")
        drawText("Draw", text_font, color[1], screen, CentreX - 450, CentreY)
    if isGameOver == True:
        DrawCrosssedLine(board)
    return isGameOver

#Human move:
def HumanMove(board,currentPlayer,isGameOver) -> None:
    #Check if the player has won
    CheckWin(board,isGameOver)
    mouseX,mouseY = pygame.mouse.get_pos()
    Humanmoved = False

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
        if isGameOver != True:
            if rect.collidepoint(mouseX,mouseY) and Clicked == True:
                if currentPlayer == "X":
                    j = int((rect.center[0] - CentreX - Charwidth )//Charwidth -1)
                    i = int((rect.center[1] - CentreY - Charwidth )//Charwidth -1)
                    board[i][j] = "X"
                    Avialable_Space[i][j] = 0
                    Humanmoved = True
                    DrawBoard(board)
                if currentPlayer == "O":
                    j = int((rect.center[0] - CentreX - Charwidth )//Charwidth -1)
                    i = int((rect.center[1] - CentreY - Charwidth )//Charwidth -1)
                    board[i][j] = "O"
                    Avialable_Space[i][j] = 0
                    Humanmoved = True
                    DrawBoard(board)
                #Check if the player has won
                CheckWin(board,isGameOver)
                print(currentPlayer)
    if Humanmoved:
       currentPlayer = nextTurn(currentPlayer)
       print("Current Player: ",currentPlayer)
       return currentPlayer

#Main Game Loop
while running:
    Clicked = False
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not Clicked:
            print("Mouse Clicked")
            Clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            Clicked = False
        if event.type == pygame.KEYDOWN:       
            # checking if key "A" was pressed
            if event.key == pygame.K_e:
                print("E pressed")
                boolDark = not boolDark
        
        
    if boolDark:
    #Set colour pallette
        color = darkmode
    else:
        color = whitemode

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color[0])
    #Draw Border
    DrawBorder(screen, color[1])
    #Draw Board
    DrawBoard(board)
    #Play a Random move
    #PlayRandomly(board,currentPlayer,isGameOver)
    #Change player
    #currentPlayer = nextTurn(currentPlayer)
    #Check if the player has won
    isGameOver = CheckWin(board,isGameOver)
    HumanMove(board,currentPlayer,isGameOver)


    # flip() the display to put your work on screen
    pygame.display.flip() 

    # limits FPS to 60 
    clock.tick(60)

pygame.quit()

