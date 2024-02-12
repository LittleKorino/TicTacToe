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

#Testing   
t = 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color[0])

    #Rectanglessss!!!
    pygame.draw.rect(screen, color[1], [0, 0, t, t], 5)
    pygame.draw.rect(screen, color[1], [0, t, t, t], 5)
    pygame.draw.rect(screen, color[1], [t, 0, t, t], 5)
    pygame.draw.rect(screen, color[1], [2*t, 0, t, t], 5)
    pygame.draw.rect(screen, color[1], [0, 2*t, t, t], 5)
    pygame.draw.rect(screen, color[1], [t, t, t, t], 5)
    pygame.draw.rect(screen, color[1], [2*t, t, t, t], 5)
    pygame.draw.rect(screen, color[1], [t, 2*t, t, t], 5)
    pygame.draw.rect(screen, color[1], [2*t, 2* t, t, t], 5)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60 
    clock.tick(60)

pygame.quit()
#testing by *NIKHIL*
#Teeeesststinf By ✈️✈️✈️