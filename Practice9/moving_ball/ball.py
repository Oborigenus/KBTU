class Ball:
    def __init__(self, x, y, radius, speed, width, height):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.width = width
        self.height = height

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= self.width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.height - self.radius:
            self.y = new_y