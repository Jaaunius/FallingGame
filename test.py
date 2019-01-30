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

index = 0
index1 = 1

snakeX = 500
snakeY = 500

enemyX = [randint(0, 800), randint(0, 800), randint(0, 800), randint(0, 800), randint(0, 800)]
enemyY = [50, 50, 50, 50, 50]

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Falling Game')

def player(block_size):
    pygame.draw.rect(win, white, [snakeX, snakeY, block_size, block_size])

def enemy(x,y):
    pygame.draw.ellipse(win, red, [enemyX[0], enemyY[0], 30, 30])
    pygame.draw.ellipse(win, red, [enemyX[1], enemyY[1], 30, 30])
    pygame.draw.ellipse(win, red, [enemyX[2], enemyY[2], 30, 30])
    pygame.draw.ellipse(win, red, [enemyX[3], enemyY[3], 30, 30])
    pygame.draw.ellipse(win, red, [enemyX[4], enemyY[4], 30, 30])

def enemyLower():
    enemyY[0] += 5
    enemyY[1] += 5
    enemyY[2] += 5
    enemyY[3] += 5
    enemyY[4] += 5

def clone():
    enemyY[0] = 0
    enemyX[0] = randint(0, 800)
    enemyY[1] = 0
    enemyX[1] = randint(0, 800)
    enemyY[2] = 0
    enemyX[2] = randint(0, 800)
    enemyY[3] = 0
    enemyX[3] = randint(0, 800)
    enemyY[4] = 0
    enemyX[4] = randint(0, 800)

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

    if snakeX == enemyX[0] and snakeY == enemyY[0]:
        break

    if snakeX == enemyX[1] and snakeY == enemyY[1]:
        break

    if snakeX == enemyX[2] and snakeY == enemyY[2]:
        break

    if snakeX == enemyX[3] and snakeY == enemyY[3]:
        break

    if snakeX == enemyX[4] and snakeY == enemyY[4]:
        break

    win.fill(black)

    player(40)
    enemy(500,300)
    enemyLower()

    pygame.display.update()
pygame.quit()
