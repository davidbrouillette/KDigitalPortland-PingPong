import pygame
import threading
from BitdoKeyMappings import parseButton

def listenForControllerInput(player1, player2):
    thread = threading.Thread(target=listenLoop, kwargs={"player1":player1,"player2":player2})
    thread.setDaemon(True)
    return thread
    

def listenLoop(player1,player2):
    done = True
    while done:
        for event in pygame.event.get():
            joy = event.joy
            button = parseButton(event)
            keyMapping
            if joy == "0":
                keyMapping = player1.keyMapping
            else:
                keyMapping = player2.keyMapping
            
            print(event)
            print(joy)
            if button in keyMapping and keyMapping[button] is not None:
                if event.joy == "0":
                    keyMapping[button](player1.name, event)
                else:
                    keyMapping[button](player2.name, event)