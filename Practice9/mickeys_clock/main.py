import pygame
from clock import Clock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
app_clock = Clock(screen)

running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    app_clock.draw()

    pygame.display.flip()

    clock.tick(1)

pygame.quit()