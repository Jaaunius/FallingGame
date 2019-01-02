import pygame
from random import randint

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

block_size = 50

vel = 15

snakeX = 500
snakeY = 500

enemyX = randint(0, 800)
enemyY = []

win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Falling Game')


def snake(block_size):
    pygame.draw.rect(win, green, [snakeX, snakeY, block_size, block_size])


def enemy():
    pygame.draw.ellipse(win, red, [enemyX, enemyY, 15, 15])


run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # for e in enemyX:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snakeX -= vel
    if keys[pygame.K_RIGHT]:
        snakeX += vel

    win.fill(black)
    snake(10)
    enemy()

    pygame.display.update()
pygame.quit()
