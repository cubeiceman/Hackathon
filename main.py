import pygame
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode([WIDTH, HEIGHT])
c = pygame.time.Clock()
WHITE = (255, 255, 255)

before_time = time.time()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    after_time = time.time()
    delta_time = after_time - before_time
    before_time = after_time

    window.fill(WHITE)
    pygame.display.flip()
    c.tick(60)
