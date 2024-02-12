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
def drawText(text, font, colour, surface, x, y):
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
            if board[i][j] == 0:
                drawXO.drawX(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.75*Charwidth,color[1])
            elif board[i][j] == 1:
                drawXO.drawO(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.75*Charwidth,color[1])
            else:
                continue


#Board Setup
board = [["","",""],
        ["","",""],
        ["","",""]]

Avialable_Space =   [[1,1,1],
                    [1,1,1],
                    [1,1,1]]

player = [0,1]
currentPlayer = player[0]
gameOver = False

# Check gameStatus
def CheckGameStatus(board):
    #Checking Horizontal
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]  
    #Checking Vertical
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1] 
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    #Checking Diagonal
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return ""
    
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

   
    #Draw the board

    i = random.randint(0,2)
    j = random.randint(0,2)
    if currentPlayer == 0 and Avialable_Space[i][j]!= 0 and gameOver == False:
        board[i][j] = currentPlayer
        Avialable_Space[i][j] = 0
        currentPlayer = player[1]
        DrawBoard(board)
        if CheckGameStatus(board) != "":
            print("Player X wins!")
            drawText("Player X wins", text_font, color[1], screen, 10, 10)
            break
    elif currentPlayer == 1 and Avialable_Space[i][j]!= 0 and gameOver == False:
        board[i][j] = currentPlayer
        Avialable_Space[i][j] = 0
        currentPlayer = player[0]
        DrawBoard(board)
        if CheckGameStatus(board) != "":
            print("Player O wins!")
            drawText("Player O wins", text_font, color[1], screen, 10, 10)
            break

    else:
        continue

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60 
    clock.tick(1)

pygame.quit()

