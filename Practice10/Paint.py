import pygame

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

color = (0, 0, 0)
tool = "Brush"
drawing = False
start_pos = None

screen.fill((255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "Rect":
                pygame.draw.rect(screen, color, (*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]), 2)
            elif tool == "Circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "Brush":
                pygame.draw.circle(screen, color, event.pos, 5)
            elif tool == "Eraser":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]:
        tool = "Brush"
    if keys[pygame.K_r]:
        tool = "Rect"
    if keys[pygame.K_c]:
        tool = "Circle"
    if keys[pygame.K_e]:
        tool = "Eraser"

    if keys[pygame.K_1]:
        color = (0, 0, 0)
    if keys[pygame.K_2]:
        color = (255, 0, 0)
    if keys[pygame.K_3]:
        color = (0, 255, 0)
    if keys[pygame.K_4]:
        color = (0, 0, 255)

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 60))

    instructions = [
        "Tools: B=Brush R=Rect C=Circle E=Eraser",
        "Colors: 1=Black 2=Red 3=Green 4=Blue",
        f"Current Tool: {tool} | Color: {color}"
    ]

    for i, text in enumerate(instructions):
        img = font.render(text, True, (0, 0, 0))
        screen.blit(img, (10, 5 + i*18))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()