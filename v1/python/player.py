import pygame

class Player:
    def __init__(self, name, controllerId, x, y):
        self.name = name
        self.controllerId = controllerId
        self.textFunc = None
        self.pos = (x,y)
        self.color = (219,204,161)
        self.font = pygame.font.SysFont("lato", 175, True)
        self.bounds = self.getSurface("0")
        
    def draw(self, surface, centralized=False):
        textSurface, self.bounds = self.getSurface(str(self.textFunc(self.name)))
        pos = (self.pos[0] - self.bounds.width // 2, self.pos[1])
        surface.blit(textSurface, pos)
        
    def getSurface(self, text):
        textSurface = self.font.render(text, False, self.color)
        return textSurface, textSurface.get_rect()
    
    def update(self):
        pass


