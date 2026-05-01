import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 50)

player = pygame.Rect(180, 500, 40, 60)
speed_x = 5
speed_y_forward = 7
speed_y_backward = 4

enemy = pygame.Rect(random.randint(0, 360), -100, 40, 60)
enemy_speed = 5

coins = []
coin_speed = 4
coin_score = 0

coins_for_speedup = 5
speed_increment = 1

game_over = False

def spawn_coin():
    r = random.random()

    if r < 0.6:
        return [random.randint(10, WIDTH-10), -10, 1, (205, 127, 50), 6]
    elif r < 0.9:
        return [random.randint(10, WIDTH-10), -10, 2, (192, 192, 192), 8]
    else:
        return [random.randint(10, WIDTH-10), -10, 3, (255, 215, 0), 10]


running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= speed_x
        if keys[pygame.K_RIGHT]:
            player.x += speed_x
        if keys[pygame.K_UP]:
            player.y -= speed_y_forward
        if keys[pygame.K_DOWN]:
            player.y += speed_y_backward

        player.x = max(0, min(WIDTH - player.width, player.x))
        player.y = max(0, min(HEIGHT - player.height, player.y))

        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(0, 360)

        if random.randint(1, 40) == 1:
            coins.append(spawn_coin())

        for coin in coins:
            coin[1] += coin_speed

        for coin in coins[:]:
            coin_rect = pygame.Rect(coin[0]-coin[4], coin[1]-coin[4], coin[4]*2, coin[4]*2)

            if player.colliderect(coin_rect):
                coin_score += coin[2]  # add value
                coins.remove(coin)

                if coin_score % coins_for_speedup == 0:
                    enemy_speed += speed_increment

        coins = [c for c in coins if c[1] < HEIGHT + 10]

        if player.colliderect(enemy):
            game_over = True

        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(screen, (0, 0, 255), enemy)

        for coin in coins:
            pygame.draw.circle(screen, coin[3], (coin[0], coin[1]), coin[4])

        text = font.render(f"Coins: {coin_score}", True, (0, 0, 0))
        speed_text = font.render(f"Enemy Speed: {enemy_speed}", True, (0, 0, 0))

        screen.blit(text, (WIDTH - 130, 10))
        screen.blit(speed_text, (10, 10))

    else:
        over_text = big_font.render("GAME OVER", True, (0, 0, 0))
        score_text = font.render(f"Final Score: {coin_score}", True, (0, 0, 0))

        screen.blit(over_text, (90, 250))
        screen.blit(score_text, (120, 320))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()