import pygame
from racer import RacerGame
from ui import Button
from persistence import load_scores, save_score, load_settings, save_settings

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

state = "menu"
settings = load_settings()
name = "Player"

game = None

play_btn = Button("Play", 100, 150)
leader_btn = Button("Leaderboard", 100, 220)
settings_btn = Button("Settings", 100, 290)
quit_btn = Button("Quit", 100, 360)

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "menu":
                if play_btn.clicked(event.pos):
                    name = input("Enter name: ")
                    game = RacerGame(settings)
                    state = "game"
                if leader_btn.clicked(event.pos):
                    state = "leaderboard"
                if settings_btn.clicked(event.pos):
                    state = "settings"
                if quit_btn.clicked(event.pos):
                    running = False

            elif state == "gameover":
                state = "menu"

            elif state == "leaderboard":
                state = "menu"

    if state == "menu":
        play_btn.draw(screen, font)
        leader_btn.draw(screen, font)
        settings_btn.draw(screen, font)
        quit_btn.draw(screen, font)

    elif state == "game":
        game.update()
        game.draw(screen)
        if game.game_over:
            save_score(name, game.score, game.distance)
            state = "gameover"

    elif state == "gameover":
        txt = font.render("Game Over", True, (0,0,0))
        screen.blit(txt, (120,250))

    elif state == "leaderboard":
        scores = load_scores()
        y = 100
        for s in scores:
            txt = font.render(f"{s['name']} {s['score']}", True, (0,0,0))
            screen.blit(txt, (80,y))
            y += 40

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
