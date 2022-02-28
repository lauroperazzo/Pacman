import pygame

yellow = (255,255,0)
pygame.init()

screen = pygame.display.set_mode((640,480),0)
while True:

# Draw player on screen
    pygame.draw.circle(screen, yellow, (320,240),50,0)
    pygame.display.update()
#Events

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            exit()