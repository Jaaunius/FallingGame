import pygame
from random import randint

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

vel = 15

enemyX = [0] * 5
enemyY = [0] * 5

index = 0
index1 = 1

snakeX = 500
snakeY = 500

enemyX[0] = randint(0, 800)
enemyY[0] = 50
enemyX[1] = randint(0, 800)
enemyY[1] = 50

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Falling Game')

def player(block_size):
    pygame.draw.rect(win, white, [snakeX, snakeY, block_size, block_size])

def enemy(x,y):
    pygame.draw.ellipse(win, red, [enemyX[0], enemyY[0], 30, 30])
    pygame.draw.ellipse(win, red, [enemyX[1], enemyY[1], 30, 30])

def enemyLower():
    enemyY[0] += 5
    enemyY[1] += 5

def clone():
    enemyY[0] = 0
    enemyX[0] = randint(0, 800)
    enemyY[1] = 0
    enemyX[1] = randint(0, 800)

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snakeX -= vel
    if keys[pygame.K_RIGHT]:
        snakeX += vel

    if enemyY[0] >= display_height:
        clone()

    if enemyY[1] >= display_height:
        clone()

    win.fill(black)

    player(40)
    enemy(500,300)
    enemyLower()

    pygame.display.update()
pygame.quit()
