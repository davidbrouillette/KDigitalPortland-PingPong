import pygame

class TextObject:
    def __init__(self, id, text, x, y, fontSize=50):
        self.id = id
        self.pos = (x,y)
        self.text = text
        self.color = (255,117,73)
        self.font = pygame.font.SysFont("lato", fontSize, True)
        self.bounds = self.getSurface(self.text)
        
    def draw(self, surface, centralized=False):
        textSurface, self.bounds = self.getSurface(self.text)
        pos = (self.pos[0] - self.bounds.width // 2, self.pos[1])
        surface.blit(textSurface, pos)
        
    def getSurface(self, text):
        textSurface = self.font.render(text, False, self.color)
        return textSurface, textSurface.get_rect()
    
    def update(self):
        pass


