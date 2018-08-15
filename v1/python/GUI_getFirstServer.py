import pygame
from gui import GUI
from textObject import TextObject
from BitdoKeyMappings import parseButton

def GUI_getFirstServer(keyMapping):
    setupPromptOne = GUI()
    
    promptText = TextObject("prompt", "First Server", 350, 25)
    elevenText = TextObject("left", "Player 1", 200, 150)
    twentyoneText = TextObject("right", "Player 2", 500, 150)
    rshoulderText = TextObject("rshoulder", "-->", 500, 225, 125)
    lshoulderText = TextObject("lshoulder", "<--", 200, 225, 125)

    setupPromptOne.addGUIObject(promptText)
    setupPromptOne.addGUIObject(elevenText)
    setupPromptOne.addGUIObject(twentyoneText)
    setupPromptOne.addGUIObject(rshoulderText)
    setupPromptOne.addGUIObject(lshoulderText)
    setupPromptOne.setupGUI()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                break;
            if event.type == pygame.JOYBUTTONDOWN:
                button = parseButton(event)
                if button in keyMapping and keyMapping[button] is not None:
                    keyMapping[button](event)
                    running = False
                    break;
                
        pygame.display.update()
        setupPromptOne.update()
        setupPromptOne.draw()
        setupPromptOne.clock.tick(30)
        
    setupPromptOne.objects = []

