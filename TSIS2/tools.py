from collections import deque
import pygame
import math

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    w, h = surface.get_size()
    queue = deque()
    queue.append((x, y))

    while queue:
        px, py = queue.popleft()

        if px < 0 or px >= w or py < 0 or py >= h:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))



def draw_square(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    side = min(abs(x2 - x1), abs(y2 - y1))

    dx = 1 if x2 >= x1 else -1
    dy = 1 if y2 >= y1 else -1

    front = pygame.Rect(x1, y1, side * dx, side * dy)

    offset = side // 4
    back = pygame.Rect(
        x1 + offset,
        y1 - offset,
        side * dx,
        side * dy
    )

    pygame.draw.rect(surface, color, front, width)
    pygame.draw.rect(surface, color, back, width)

    pygame.draw.line(surface, color, front.topleft, back.topleft, width)
    pygame.draw.line(surface, color, front.topright, back.topright, width)
    pygame.draw.line(surface, color, front.bottomleft, back.bottomleft, width)
    pygame.draw.line(surface, color, front.bottomright, back.bottomright, width)

def draw_equilateral_triangle(surface, color, start, end, width):
    x1, y1 = start
    side = abs(end[0] - x1)
    height = int(side * math.sqrt(3) / 2)

    points = [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - height)]
    pygame.draw.polygon(surface, color, points, width)

def draw_right_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(surface, color, points, width)

def draw_rhombus(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(surface, color, points, width)