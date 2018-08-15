import pygame
import threading
from BitdoKeyMappings import BITDO_KEY_MAPPINGS_JOYBUTTON, BITDO_KEY_MAPPINGS_JOYAXIS, parseButton

class Controller:
    def __init__(self, name, id, keyMapping, instance):
        self.button_data = None
        self.hat_data = None
        self.done = True
        self.controllerInstance = instance
        self.name = name
        self.keyMapping = keyMapping
        
        
        if not self.button_data:
            self.button_data = {}
            for i in range(self.controllerInstance.get_numbuttons()):
                self.button_data[i] = False
                
        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controllerInstance.get_numhats()):
                self.hat_data[i] = (0,0)
