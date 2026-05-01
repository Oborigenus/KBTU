import pygame
import math

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

def draw_square(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end

    side = min(abs(x2 - x1), abs(y2 - y1))

    x = x1
    y = y1

    offset = side // 3

    front = pygame.Rect(x, y, side, side)

    back = pygame.Rect(x + offset, y - offset, side, side)

    pygame.draw.rect(surface, color, front, 2)
    pygame.draw.rect(surface, color, back, 2)

    pygame.draw.line(surface, color, (x, y), (x + offset, y - offset), 2)
    pygame.draw.line(surface, color, (x + side, y), (x + side + offset, y - offset), 2)
    pygame.draw.line(surface, color, (x, y + side), (x + offset, y + side - offset), 2)
    pygame.draw.line(surface, color, (x + side, y + side), (x + side + offset, y + side - offset), 2)

def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2)

    points = [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side // 2, y1 - height)
    ]

    pygame.draw.polygon(surface, color, points, 2)


def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end

    points = [
        (x1, y1),
        (x2, y1),
        (x1, y2)
    ]

    pygame.draw.polygon(surface, color, points, 2)


def draw_rhombus(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(surface, color, points, 2)


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

            elif tool == "Square":
                draw_square(screen, color, start_pos, end_pos)
                
            elif tool == "Right_Triangle":
                draw_right_triangle(screen, color, start_pos, end_pos)

            elif tool == "Equilateral":
                draw_equilateral_triangle(screen, color, start_pos, end_pos)

            elif tool == "Rhombus":
                draw_rhombus(screen, color, start_pos, end_pos)

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "Brush":
                pygame.draw.circle(screen, color, event.pos, 5)
            elif tool == "Eraser":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]: tool = "Brush"
    if keys[pygame.K_e]: tool = "Eraser"
    if keys[pygame.K_r]: tool = "Rect"
    if keys[pygame.K_c]: tool = "Circle"
    if keys[pygame.K_s]: tool = "Square"
    if keys[pygame.K_t]: tool = "Right_Triangle"
    if keys[pygame.K_q]: tool = "Equilateral"
    if keys[pygame.K_h]: tool = "Rhombus"

    if keys[pygame.K_1]: color = (0, 0, 0)
    if keys[pygame.K_2]: color = (255, 0, 0)
    if keys[pygame.K_3]: color = (0, 255, 0)
    if keys[pygame.K_4]: color = (0, 0, 255)

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 80))

    instructions = [
        "Tools: B=Brush E=Eraser R=Rect C=Circle S=Square",
        "T=Right Triangle Q=Equilateral H=Rhombus",
        "Colors: 1=Black 2=Red 3=Green 4=Blue",
        f"Current Tool: {tool} | Color: {color}"
    ]

    for i, text in enumerate(instructions):
        img = font.render(text, True, (0, 0, 0))
        screen.blit(img, (10, 5 + i*18))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()