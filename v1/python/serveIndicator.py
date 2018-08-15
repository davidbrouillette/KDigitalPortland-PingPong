import pygame

class ServeIndicator:
    def __init__(self, id, icon, x, y, colorFunc):
        self.id = id
        self.pos = (x,y)
        self.icon = icon
        self.color = (255,117,73)
        self.servingColor = (255,117,73)
        self.notServingColor = (200,199,211)
        self.colorFunc = colorFunc
        self.font = pygame.font.SysFont("lato", 150, True)
        self.bounds = self.getSurface(self.icon)
        
    def draw(self, surface, centralized=False):
        textSurface, self.bounds = self.getSurface(self.icon)
        pos = (self.pos[0] - self.bounds.width // 2, self.pos[1])
        surface.blit(textSurface, pos)
        
    def getSurface(self, text):
        color = self.color
        isNotServing = self.colorFunc(self.id)
        if isNotServing:
            color = self.notServingColor
            
        textSurface = self.font.render(text, False, color)
        return textSurface, textSurface.get_rect()
    
    def update(self):
        pass

