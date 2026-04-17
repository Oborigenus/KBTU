import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

player = MusicPlayer("Practice9/music_player/music")


running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    name, index, total = player.get_track_info()

    track_text = font.render(f"Track: {name}", True, (255, 255, 255))
    screen.blit(track_text, (40, 50))

    playlist_text = font.render(f"Track {index} / {total}", True, (200, 200, 200))
    screen.blit(playlist_text, (40, 90))

    position = player.get_position()
    time_text = font.render(f"Time: {position} sec", True, (180, 180, 180))
    screen.blit(time_text, (40, 130))


    controls = [
        "P = Play",
        "S = Stop",
        "N = Next",
        "B = Previous",
        "Q = Quit"
    ]

    for i, text in enumerate(controls):
        ctrl_surface = font.render(text, True, (150, 150, 150))
        screen.blit(ctrl_surface, (350, 50 + i * 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()