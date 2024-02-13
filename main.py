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

if boolDark:
    #Set colour pallette
    color = darkmode
else:
    color = whitemode


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
gameOver = False

# Check gameStatus
def CheckGameStatus(board):
    #Checking Horizontal
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            gameOver = True
            return board[i][0]
      
    #Checking Vertical
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            gameOver = True
            return board[0][i]

    #Checking Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        gameOver = True
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        gameOver = True
        return board[0][2]
    else:
        gameOver = False
        return "Continue"

#Check board
def isBoardFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    gameOver = True
    return True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color[0])

    #Vertical lines
    #Refer the picture in readme for the position of the lines.
    pygame.draw.line(screen, color[1], (CentreX - 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX - 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    pygame.draw.line(screen, color[1], (CentreX + 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX + 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    
    #Horizontal lines
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY - 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY - 0.5*Charwidth) ), 10)
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY + 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY + 0.5*Charwidth) ), 10)

    DrawBoard(board)
    i = random.randint(0,2)
    j = random.randint(0,2)
    if currentPlayer == "X" and Avialable_Space[i][j]!= 0 and gameOver == False:
        board[i][j] = currentPlayer
        Avialable_Space[i][j] = 0
        currentPlayer = player[1]
        DrawBoard(board)
        
    if currentPlayer == "O" and Avialable_Space[i][j]!= 0 and gameOver == False:
        board[i][j] = currentPlayer
        Avialable_Space[i][j] = 0
        currentPlayer = player[0]
        DrawBoard(board)


    if CheckGameStatus(board) == "X" :
        #print("X Won")
        drawText("X Won", text_font, color[1], screen, CentreX - 450, CentreY)
        gameOver = True
    if CheckGameStatus(board) == "O" :
        #print("O Won")
        drawText("O Won", text_font, color[1], screen, CentreX - 450, CentreY)
        gameOver = True
    if isBoardFull(board) and gameOver == False:
        #print("Draw")
        drawText("Draw", text_font, color[1], screen, CentreX - 450, CentreY)


    # flip() the display to put your work on screen
    pygame.display.flip() 

    # limits FPS to 60 
    clock.tick(60)

pygame.quit()

