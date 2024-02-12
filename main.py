import pygame
import drawXO

# pygame setup
pygame.init()
windowwidth = 1280
windowheight = 720
screen = pygame.display.set_mode((windowwidth, windowheight))
clock = pygame.time.Clock()
running = True

# Game setup
(h,k) = (windowwidth/2, windowheight/2)
Charwidth = 200

# Set colours
darkmode = ["black","white"]
whitemode = ["white","black"]
boolDark = True

if boolDark:
    #Set colour pallette
    color = darkmode
else:
    color = whitemode

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
    pygame.draw.line(screen, color[1], (h - 0.5*Charwidth , k - 1.5*Charwidth), ((h - 0.5*Charwidth) , (k - 1.5*Charwidth) + 3*Charwidth ), 10)
    pygame.draw.line(screen, color[1], (h + 0.5*Charwidth , k - 1.5*Charwidth), ((h + 0.5*Charwidth) , (k - 1.5*Charwidth) + 3*Charwidth ), 10)
    
    #Horizontal lines
    pygame.draw.line(screen, color[1], (h - 1.5*Charwidth , k - 0.5*Charwidth), ((h - 1.5*Charwidth) + 3*Charwidth , (k - 0.5*Charwidth) ), 10)
    pygame.draw.line(screen, color[1], (h - 1.5*Charwidth , k + 0.5*Charwidth), ((h - 1.5*Charwidth) + 3*Charwidth , (k + 0.5*Charwidth) ), 10)

    #Draw X
    drawXO.drawX(screen, h , k , 0.75 * Charwidth,color[1])
    #draw O
    drawXO.drawO(screen,h , k - Charwidth, 0.75* Charwidth,color[1])
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60 
    clock.tick(60)

pygame.quit()

