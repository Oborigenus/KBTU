import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

snake = [(100, 100)]
direction = (20, 0)

def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, 20)
        y = random.randrange(0, HEIGHT, 20)

        if (x, y) not in snake:
            r = random.random()

            if r < 0.6: 
                return [x, y, 1, (255, 0, 0), time.time(), 6]
            elif r < 0.9:
                return [x, y, 2, (255, 165, 0), time.time(), 5]
            else:
                return [x, y, 3, (255, 255, 0), time.time(), 4]

food = spawn_food()

score = 0
level = 1
speed = 10

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and direction != (0, 20):
        direction = (0, -20)
    elif keys[pygame.K_DOWN] and direction != (0, -20):
        direction = (0, 20)
    elif keys[pygame.K_LEFT] and direction != (20, 0):
        direction = (-20, 0)
    elif keys[pygame.K_RIGHT] and direction != (-20, 0):
        direction = (20, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    if head in snake:
        running = False

    snake.insert(0, head)

    current_time = time.time()
    if current_time - food[4] > food[5]:
        food = spawn_food()  # replace expired food

    if head == (food[0], food[1]):
        score += food[2]
        food = spawn_food()

        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, 20, 20))

    pygame.draw.rect(screen, food[3], (food[0], food[1], 20, 20))

    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()