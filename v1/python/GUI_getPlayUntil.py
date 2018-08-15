import pygame
from gui import GUI
from textObject import TextObject
from BitdoKeyMappings import parseButton

def GUI_getPlayUntil(keyMapping):
    setupPromptOne = GUI()

    promptText = TextObject("prompt", "Play Until", 350, 25)
    elevenText = TextObject("eleven", "11", 200, 125, 100)
    twentyoneText = TextObject("twentyone", "21", 500, 125, 100)
    lshoulderText = TextObject("lshoulder", "-->", 500, 225, 125)
    rshoulderText = TextObject("rshoulder", "<--", 200, 225, 125)

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
