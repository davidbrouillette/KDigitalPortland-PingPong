import pygame
from BitdoKeyMappings import BITDO_KEY_MAPPINGS_JOYBUTTON, BITDO_KEY_MAPPINGS_JOYAXIS, parseButton

def MainLoop(running, keyMapP1, keyMapP2, gui, currentMatch):
    actions = None

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
                name = event.joy
                print("Event: " + str(event))
                if name == 1:
                    actions = keyMapP1
                elif name == 0:
                    actions = keyMapP2
                if actions and button in actions and actions[button] is not None:
                    actions[button](name, event)
        
        pygame.display.update()
        gui.update()
        gui.draw()
        gui.clock.tick(30)

##                if event.type == pygame.JOYBUTTONDOWN:
##                    self.button_data[event.button] = True
##                if event.type == pygame.JOYBUTTONUP:
##                    self.button_data[event.button] = False
##                if event.type == pygame.JOYHATMOTION:
##                    self.hat_data[event.hat] = event.value
    
    
    