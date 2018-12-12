import pygame
from random import randint
pygame.init()

win = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Falling Blocks")

enemyX = randint(0,700)
x = 350
y = 660
width = 30
height = 30
vel = 15
win.fill((0,0,0))
run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 700 - width - vel:
        x += vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.draw.ellipse(win, (255, 0, 110), (enemyX, 0, width, height))

    pygame.display.update()
pygame.quit()
