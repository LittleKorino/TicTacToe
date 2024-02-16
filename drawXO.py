import pygame
import Utilities

def drawX (screen:object, xCood:int, yCood:int, width:int, colour:str):

    pygame.draw.line(screen, colour, (xCood - 0.5*width , yCood - 0.5*width), (xCood + 0.5*width,yCood + 0.5*width), 10)
    pygame.draw.line(screen, colour, (xCood - 0.5*width , yCood + 0.5*width), (xCood + 0.5*width,yCood - 0.5*width), 10)

def drawO (screen:object, xCood:int, yCood:int, width:int, colour:str):

    pygame.draw.circle(screen,colour, (xCood , yCood ), width/2, 10)

#Draw Border lines:
def DrawBorder(screen:object,CentreX,CentreY,Charwidth, color:str) -> None:
     #Vertical lines
    #Refer the picture in readme for the position of the lines.
    pygame.draw.line(screen, color[1], (CentreX - 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX - 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    pygame.draw.line(screen, color[1], (CentreX + 0.5*Charwidth , CentreY - 1.5*Charwidth), ((CentreX + 0.5*Charwidth) , (CentreY - 1.5*Charwidth) + 3*Charwidth ), 10)
    
    #Horizontal lines
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY - 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY - 0.5*Charwidth) ), 10)
    pygame.draw.line(screen, color[1], (CentreX - 1.5*Charwidth , CentreY + 0.5*Charwidth), ((CentreX - 1.5*Charwidth) + 3*Charwidth , (CentreY + 0.5*Charwidth) ), 10)

def drawText(text:str, font:object, colour:str, surface:object, x:int, y:int) -> None:
    img = font.render(text, True, colour)
    surface.blit(img, (x, y))

#Draw Board
def DrawBoard(screen,board,color,Charwidth,CentreX,CentreY) -> None:
      for i in range(3):
        for j in range (3):
            if board[i][j] == "X":
                drawX(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.7*Charwidth,color[1])
            elif board[i][j] == "O":
                drawO(screen, CentreX - Charwidth + j*Charwidth, CentreY - Charwidth + i*Charwidth, 0.8*Charwidth,color[1])
            else:
                continue

#Check which Row/column need to be striken
def DrawCrosssedLine(screen,board,CentreX,CentreY,Charwidth) -> None:
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
