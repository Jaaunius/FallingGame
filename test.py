import pygame
pygame.init()

win = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Falling Blocks")

x = 350
y = 660
width = 30
height = 30
vel = 15

run = True
while run:
    pygame.time.delay(100)

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
    pygame.display.update()

pygame.quit()