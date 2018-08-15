import pygame
from gui import GUI
from textObject import TextObject
from BitdoKeyMappings import parseButton

def GUI_gameOver(keyMapping, winner, score):
    setupGUI = GUI()
    
    winPrompt = winner + " wins!"
    
    winnerText = TextObject("winner", winPrompt, 350, 0, 75)
    promptText = TextObject("prompt", "Play Again?", 350, 125)
    elevenText = TextObject("left", "Yes", 200, 200, 75)
    twentyoneText = TextObject("right", "No", 500, 200, 75)
    rshoulderText = TextObject("rshoulder", "-->", 500, 275, 100)
    lshoulderText = TextObject("lshoulder", "<--", 200, 275, 100)

    setupGUI.addGUIObject(winnerText)
    setupGUI.addGUIObject(promptText)
    setupGUI.addGUIObject(elevenText)
    setupGUI.addGUIObject(twentyoneText)
    setupGUI.addGUIObject(rshoulderText)
    setupGUI.addGUIObject(lshoulderText)
    setupGUI.setupGUI()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                button = parseButton(event)
                if button in keyMapping and keyMapping[button] is not None:
                    keyMapping[button](event)
                    running = False
                    break;
                
        pygame.display.update()
        setupGUI.update()
        setupGUI.draw()
        setupGUI.clock.tick(30)
        
    setupGUI.objects = []


