import pygame
def drawX (screen:object, xCood:int, yCood:int, width:int, colour:str):

    pygame.draw.line(screen, colour, (xCood - 0.5*width , yCood - 0.5*width), (xCood + 0.5*width,yCood + 0.5*width), 10)
    pygame.draw.line(screen, colour, (xCood - 0.5*width , yCood + 0.5*width), (xCood + 0.5*width,yCood - 0.5*width), 10)

def drawO (screen:object, xCood:int, yCood:int, width:int, colour:str):

    pygame.draw.circle(screen,colour, (xCood , yCood ), width/2, 10)
