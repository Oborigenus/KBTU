import pygame

class Button:
    def __init__(self, text, x, y):
        self.text=text
        self.rect=pygame.Rect(x,y,200,50)

    def draw(self, screen, font):
        pygame.draw.rect(screen,(0,0,0),self.rect,2)
        txt=font.render(self.text,True,(0,0,0))
        screen.blit(txt,(self.rect.x+20,self.rect.y+10))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)