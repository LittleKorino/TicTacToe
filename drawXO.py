import pygame
import Utilities

def drawX (screen:object, xCood:int, yCood:int, width:int, colour:str):
    """
    
Draws The X into given coordinates

    """
    pygame.draw.line(screen, colour, (xCood - 0.5*width , yCood - 0.5*width), (xCood + 0.5*width,yCood + 0.5*width), 10)
    pygame.draw.line(screen, colour, (xCood - 0.5*width , yCood + 0.5*width), (xCood + 0.5*width,yCood - 0.5*width), 10)

def drawO (screen:object, xCood:int, yCood:int, width:int, colour:str):
    """
    
Draws The O into given coordinates

    """
    pygame.draw.circle(screen,colour, (xCood , yCood ), width/2, 10)

#Draw Border lines:
def DrawBorder(screen:object,CentreX,CentreY,Charwidth, color:str) -> None:
    """
    
Draws The two vertical and two horizontal lines over the canvas

    """
     #Vertical lines
    #Refer the picture in readme for the position of the lines.
    pygame.draw.line(screen, color[1], (CentreX - 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX - 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    pygame.draw.line(screen, color[1], (CentreX + 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX + 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    
    #Horizontal lines
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY - 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY - 0.5*Charwidth) ), 10)
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY + 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY + 0.5*Charwidth) ), 10)

def drawText(text:str, font:object, colour:str, surface:object, x:int, y:int) -> None:
    """
    
This function takes input of text and text_font to create a text on the screen

    """
    #Uses pygame's funtion to render text into a image
    img = font.render(text, True, colour)
    #shows the image in the display
    surface.blit(img, (x, y))

#Draw Board
def DrawBoard(screen,board,color,Charwidth,CentreX,CentreY) -> None:
    """
    
This function is used to draw a board at any state by using a board variable which is a two dimensional array that contains and 
Keep tracks of location details of Xs and Os on the board

    """
    for i in range(3):
        for j in range (3):
            #Loops thorugh the entire board
            if board[i][j] == "X":
                drawX(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.7*Charwidth,color[1])
            elif board[i][j] == "O":
                drawO(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.8*Charwidth,color[1])
            else:
                continue

#Check which Row/column need to be striken
def DrawCrosssedLine(screen,board,CentreX,CentreY,Charwidth) -> None:
    """
    
This funtion checks the game status and draws the crossed lines if necessary

    """
    #Check Horizontal
    for i in range(3):
        if Utilities.CheckGameStatus(board)[1] == "Horizontal"+str(i):
            pygame.draw.line(screen, "RED", (CentreX - Charwidth + i*Charwidth, CentreY - 1.5*Charwidth), (CentreX - Charwidth + i*Charwidth, CentreY + 1.5*Charwidth), 10)
    #Check verical
    for i in range(3):
        if Utilities.CheckGameStatus(board)[1] == "Vertical"+str(i):
            pygame.draw.line(screen, "RED", (CentreX - 1.5*Charwidth, CentreY - Charwidth + i*Charwidth), (CentreX + 1.5*Charwidth, CentreY - Charwidth + i*Charwidth), 10)
    #Check the diagonals
    if Utilities.CheckGameStatus(board)[1] == "Diagonal1":
            pygame.draw.line(screen, "RED", (CentreX - 1.5*Charwidth, CentreY - 1.5*Charwidth), (CentreX + 1.5*Charwidth, CentreY + 1.5*Charwidth), 10)
    if Utilities.CheckGameStatus(board)[1] == "Diagonal2": 
            pygame.draw.line(screen, "RED", (CentreX - 1.5*Charwidth, CentreY + 1.5*Charwidth), (CentreX + 1.5*Charwidth, CentreY - 1.5*Charwidth), 10)


def DrawWinnerCheckWin(screen,CentreX,CentreY,Charwidth,color,text_font,board,isGameOver) -> bool:
    """
    
This funtion checks the game status and draws the Text if necessary

    """
    #Checking the Winner:
    if Utilities.CheckGameStatus(board)[0] == "X" :
        #print("X Won")
        drawText("X Won", text_font, color[1], screen, CentreX - 450, CentreY)
        isGameOver = True
    if Utilities.CheckGameStatus(board)[0] == "O" :
        #print("O Won")
        drawText("O Won", text_font, color[1], screen, CentreX - 450, CentreY)
        isGameOver = True
    if Utilities.CheckGameStatus(board)[0] == "Tie":
        #print("Draw")
        drawText("Draw", text_font, color[1], screen, CentreX - 450, CentreY)
    if isGameOver == True:
        DrawCrosssedLine(screen,board,CentreX,CentreY,Charwidth)
    return ()
