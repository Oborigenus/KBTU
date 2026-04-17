import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball = Ball(300, 200, 25, 20, WIDTH, HEIGHT)

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -ball.speed)
            elif event.key == pygame.K_DOWN:
                ball.move(0, ball.speed)
            elif event.key == pygame.K_LEFT:
                ball.move(-ball.speed, 0)
            elif event.key == pygame.K_RIGHT:
                ball.move(ball.speed, 0)

    pygame.draw.circle(screen, (255, 0, 0), (ball.x, ball.y), ball.radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()