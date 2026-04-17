import pygame
import datetime
import math

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (300, 300)
        self.radius = 250

        self.sec_length = 200
        self.min_length = 150

    def get_time(self):
        now = datetime.datetime.now()
        return now.minute, now.second

    def draw_ticks(self):
        for i in range(60):
            angle = math.radians(i * 6)

            x1 = self.center[0] + (self.radius - 10) * math.sin(angle)
            y1 = self.center[1] - (self.radius - 10) * math.cos(angle)

            if i % 5 == 0:
                # big tick
                x2 = self.center[0] + (self.radius - 30) * math.sin(angle)
                y2 = self.center[1] - (self.radius - 30) * math.cos(angle)
                width = 4
            else:
                # small tick
                x2 = self.center[0] + (self.radius - 20) * math.sin(angle)
                y2 = self.center[1] - (self.radius - 20) * math.cos(angle)
                width = 2

            pygame.draw.line(self.screen, (200, 200, 200), (x1, y1), (x2, y2), width)

    def draw_hand(self, length, angle, color, width):
        rad = math.radians(angle)

        x = self.center[0] + length * math.sin(rad)
        y = self.center[1] - length * math.cos(rad)

        pygame.draw.line(self.screen, color, self.center, (x, y), width)

    def draw(self):
        minutes, seconds = self.get_time()

        sec_angle = seconds * 6
        min_angle = minutes * 6 + seconds * 0.1

        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius, 3)

        self.draw_ticks()

        self.draw_hand(self.sec_length, sec_angle, (255, 0, 0), 2)
        self.draw_hand(self.min_length, min_angle, (0, 100, 255), 5)