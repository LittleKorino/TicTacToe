#Got this example from pygame
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

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

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60 
    clock.tick(60)

pygame.quit()