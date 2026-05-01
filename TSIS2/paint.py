import pygame
import math
from tools import *
from datetime import datetime
from collections import deque

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

preview_end = None

color = (0, 0, 0)
tool = "Pencil"
drawing = False
start_pos = None
last_pos = None

brush_size = 5

typing = False
text_input = ""
text_pos = (0, 0)


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(canvas, (0, 0)) 

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if tool == "Fill":
                flood_fill(canvas, *event.pos, color)

            elif tool == "Text":
                typing = True
                text_input = ""
                text_pos = event.pos

            elif tool == "Line":
                drawing = True
                start_pos = event.pos

            else:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if tool == "Line":
                pygame.draw.line(canvas, color, start_pos, event.pos, brush_size)
                preview_end = None

            elif tool == "Rect":
                pygame.draw.rect(canvas, color,
                                 (*start_pos,
                                  end_pos[0]-start_pos[0],
                                  end_pos[1]-start_pos[1]),
                                 brush_size)

            elif tool == "Circle":
                radius = int(math.hypot(end_pos[0]-start_pos[0],
                                        end_pos[1]-start_pos[1]))
                pygame.draw.circle(canvas, color, start_pos, radius, brush_size)

            elif tool == "Square":
                draw_square(canvas, color, start_pos, end_pos, brush_size)

            elif tool == "Right_Triangle":
                draw_right_triangle(canvas, color, start_pos, end_pos, brush_size)

            elif tool == "Equilateral":
                draw_equilateral_triangle(canvas, color, start_pos, end_pos, brush_size)

            elif tool == "Rhombus":
                draw_rhombus(canvas, color, start_pos, end_pos, brush_size)

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "Pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

            elif tool == "Eraser":
                pygame.draw.line(canvas, (255, 255, 255), last_pos, event.pos, brush_size*2)
                last_pos = event.pos

            elif tool == "Line":
                preview_end = event.pos

        if event.type == pygame.KEYDOWN and typing:
            if event.key == pygame.K_RETURN:
                img = font.render(text_input, True, color)
                canvas.blit(img, text_pos)
                typing = False

            elif event.key == pygame.K_ESCAPE:
                typing = False

            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]

            else:
                text_input += event.unicode

    if typing:
        img = font.render(text_input, True, color)
        screen.blit(img, text_pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]: tool = "Pencil"
    if keys[pygame.K_l]: tool = "Line"
    if keys[pygame.K_e]: tool = "Eraser"
    if keys[pygame.K_r]: tool = "Rect"
    if keys[pygame.K_c]: tool = "Circle"
    if keys[pygame.K_s]: tool = "Square"
    if keys[pygame.K_t]: tool = "Right_Triangle"
    if keys[pygame.K_q]: tool = "Equilateral"
    if keys[pygame.K_h]: tool = "Rhombus"
    if keys[pygame.K_f]: tool = "Fill"
    if keys[pygame.K_x]: tool = "Text"

    if keys[pygame.K_1]: brush_size = 2
    if keys[pygame.K_2]: brush_size = 5
    if keys[pygame.K_3]: brush_size = 10

    if keys[pygame.K_4]: color = (0, 0, 0)
    if keys[pygame.K_5]: color = (255, 0, 0)
    if keys[pygame.K_6]: color = (0, 255, 0)
    if keys[pygame.K_7]: color = (0, 0, 255)

    if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
        filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
        pygame.image.save(canvas, filename)
    
    if drawing and tool == "Line" and preview_end:
        pygame.draw.line(screen, color, start_pos, preview_end, brush_size)

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 90))

    info = [
        "P=Pencil L=Line F=Fill X=Text Ctrl+S=Save",
        "R=Rect C=Circle S=Square T=RightTri Q=Equilateral H=Rhombus",
        "1/2/3=Brush Size | 4-7 Colors",
        f"Tool: {tool} | Size: {brush_size} | Color: {color}"
    ]

    for i, text in enumerate(info):
        img = font.render(text, True, (0, 0, 0))
        screen.blit(img, (10, 5 + i*20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()