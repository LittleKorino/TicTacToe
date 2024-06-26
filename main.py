import pygame
import drawXO
import Utilities

# pygame setup
pygame.init()
windowwidth = 1280
windowheight = 720
screen = pygame.display.set_mode((windowwidth, windowheight))
clock = pygame.time.Clock()
running = True

#Global Variable
WaitHumanLatch = False
(CentreX,CentreY) = (windowwidth/2, windowheight/2)
Charwidth = 200


#Choosing a Font for the canvas
text_font = pygame.font.Font("Res/Fonts/KnightWarrior-w16n8.ttf", 50)

# Set colours
darkmode = ["black","white"]
whitemode = ["white","black"]
boolDark = True

#Board Setup
#This represents the state of the board (ie) It tracks the location of Xs and Os
board = [["","",""],
        ["","",""],
        ["","",""]]

Available_Space =   [[1,1,1],
                    [1,1,1],
                    [1,1,1]]

player = ["X","O"]
currentPlayer = player[0]
isGameOver = False

 

#Main Game Loop
while running:
    Clicked = False
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not Clicked:
            Clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            Clicked = False
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_e:
                boolDark = not boolDark
        
        
    if boolDark:
    #Set colour pallette
        color = darkmode
    else:
        color = whitemode

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color[0])
    #Draw Border
    drawXO.DrawBorder(screen, CentreX, CentreY, Charwidth, color)
    #Draw Board
    drawXO.DrawBoard(screen,board,color,Charwidth,CentreX,CentreY)

    isGameOver = Utilities.CheckGameStatus(board)[2]


    #currentPlayer = Utilities.HumanVsHuman(screen,board,Available_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer)
    Utilities.HumanVsComputerMiniMax(screen,board,Available_Space,CentreX,CentreY,Charwidth,color,Clicked,currentPlayer,isGameOver,False)
    #Utilities.MinimaxVsMinimax(screen,board,Available_Space,color,Charwidth,CentreX,CentreY,currentPlayer,isGameOver)
    
    drawXO.DrawWinnerCheckWin(screen,CentreX,CentreY,Charwidth,color,text_font,board,isGameOver)

    isGameOver,board,Available_Space = Utilities.RestBoard(windowwidth,windowheight,screen,board,Available_Space,color,isGameOver,Clicked)
    # flip() the display to put your work on screen
    pygame.display.flip() 

    # limits FPS to 60 
    clock.tick(60)

pygame.quit()

