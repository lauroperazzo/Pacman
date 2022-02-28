import pygame

yellow = (255,255,0)
black = (0,0,0)
pygame.init()

#parameters
accelaration= 0.1
position_x=10
position_y=240
radius=30
velocity_x=1;
velocity_y=1;
screen = pygame.display.set_mode((640,480),0)


while True:
    #Condition to movement
    position_x = position_x + velocity_x
    position_y = position_y + velocity_y
    if position_x+radius>640:
        velocity_x = -accelaration
    if position_x-radius<0:
        velocity_x = accelaration
    if position_y+radius>480:
        velocity_y=-accelaration
    if position_y - radius <0:
        velocity_y = accelaration

# Draw player on screen
    screen.fill((black))
    pygame.draw.circle(screen, yellow, (int(position_x),int(position_y)),radius,0)
    pygame.display.update()
#Events

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            exit()