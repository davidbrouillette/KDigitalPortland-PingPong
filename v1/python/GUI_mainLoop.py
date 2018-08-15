import pygame
from gui import GUI
from player import Player
from match import Match
from textObject import TextObject
from BitdoKeyMappings import initMapping, parseButton

def GUI_mainLoop(firstServer, numOfServes):
    mainLoop = GUI()

    player1 = Player("player1", 0, 200, 25)
    player2 = Player("player2", 1, 500, 25)
    currentMatch = Match(player1, player2, firstServer, numOfServes, 5)
    player1.textFunc = currentMatch.getScore
    player2.textFunc = currentMatch.getScore
    
    player1ScoreStr = str(currentMatch.score['player1'])
    player2ScoreStr = str(currentMatch.score['player2'])
    
    player1Score = TextObject("scorePlayer1", player1ScoreStr, 200, 25, 100)
    player2Score = TextObject("scorePlayer2", player2ScoreStr, 500, 25, 100)
    serveIndicatorPlayer1 = TextObject("servePlayer1", "-->", 525, 200, 125)
    serveIndicatorPlayer2 = TextObject("servePlayer2", "<--", 175, 200, 125)
    servingColor = (255,117,73)
    notServingColor = (200,199,211)
        
    keyMapping = initMapping()
    keyMapping["rshoulder"] = lambda x: currentMatch.scorePoint(x)
       
    
    mainLoop.addGUIObject(player1Score)
    mainLoop.addGUIObject(player2Score)
    mainLoop.addGUIObject(serveIndicatorPlayer1)
    mainLoop.addGUIObject(serveIndicatorPlayer2)
    mainLoop.setupGUI()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break;
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                pygame.display.set_mode((700,400))
                break;
            if event.type == pygame.JOYBUTTONDOWN:
                button = parseButton(event)
                if button in keyMapping and keyMapping[button] is not None:
                    print(event)
                    if event.joy is not None:
                        score = None
                        if event.joy == 0:
                            score = keyMapping[button]("player1")
                        elif event.joy == 1:
                            score = keyMapping[button]("player2")
                    player1Score.text = str(score['player1'])
                    player2Score.text = str(score['player2'])
                    if(currentMatch.currentServer == "player1"):
                        serveIndicatorPlayer1.color = servingColor
                        serveIndicatorPlayer2.color = notServingColor
                    elif(currentMatch.currentServer == "player2"):
                        serveIndicatorPlayer1.color = notServingColor
                        serveIndicatorPlayer2.color = servingColor
                
                    print(score)
                
        
        
        pygame.display.update()
        mainLoop.update()
        mainLoop.draw()
        mainLoop.clock.tick(30)
        
    mainLoop.objects = []

