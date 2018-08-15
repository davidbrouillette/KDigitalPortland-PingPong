import pygame

class GUI:
    def __init__(self):
        self.title = "Ping Pong"
        self.surface = None
        self.clock = None
        self.backgroundColor = (11,132,127)
        self.width = 700
        self.height = 400
        self.objects = []
        
    def setupGUI(self):
        self.surface = pygame.display.set_mode((self.width,self.height), pygame.NOFRAME)
        #pygame.FULLSCREEN|
        self.surface.fill(self.backgroundColor)
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        
    def addGUIObject(self, obj):
        self.objects.append(obj)
    
    def update(self):
        for o in self.objects:
            o.update()
            
    def draw(self):
        self.surface.fill(self.backgroundColor)
        for o in self.objects:
            o.draw(self.surface)
            
    

##        screen.fill((135,180,210))
##        text = pygame.font.Font(None, 100)
##        textArea = text.render("HELLO!", True, (255,255,255))
##        rect = textArea.get_rect(center=(160,120))
##        screen.blit(textArea, rect)
##        pygame.display.update()
##
##from guizero import App, Text, Picture
##
##class GUI_MATCH:
##    def __init__(self, app):
##        self.app = app
##        self.app.bg = "lightgrey"
##        app.title = "Ping Pong"
##        self.playerOneScore = Text(self.app, text="0", size=200, font="Times New Roman", color="blue", grid=[0,0])
##        self.playerTwoScore = Text(self.app, text="0", size=200, font="Times New Roman", color="blue", grid=[1,0])
##
##        self.playerOneServe = Text(self.app, text="<--", size=150, font="Times New Roman", color="black", grid=[0,1])
##        self.playerTwoServe = Text(self.app, text="-->", size=150, font="Times New Roman", color="lightgrey", grid=[1,1])
##
##    def start(self):
##        self.app.display()
##
##    def updateGUI(self, server, player1Score, player2Score):
##        self.playerOneScore.value = player1Score
##        self.playerTwoScore.value = player2Score
##
##        if server == 'player1':
##            self.playerOneServe.text_color = 'black'
##            self.playerTwoServe.text_color = 'lightgrey'
##        else:
##            self.playerOneServe.text_color = 'lightgrey'
##            self.playerTwoServe.text_color = 'black'
##            
##        self.app.update()
