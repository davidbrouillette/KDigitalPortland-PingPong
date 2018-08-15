import pygame

## Keys are BUTTON
BITDO_KEY_MAPPINGS_JOYBUTTON = {
    "1": "b",
    "0": "a",
    "3": "x",
    "4": "y",
    "7": "rshoulder",
    "6": "lshoulder",
    "11": "start",
    "10": "select"
}

## Keys are (AXIS,VALUE) tuples
BITDO_KEY_MAPPINGS_JOYAXIS = {
    ("0","1"):"right",
    ("0","-1"):"left",
    ("1","1"):"down",
    ("1","-1"):"up"
}

def initMapping():
    return {
        "right": None,
        "left": None,
        "down": None,
        "up": None,
        "start": None,
        "select": None,
        "a": None,
        "b": None,
        "y": None,
        "x": None,
        "rshoulder": None,
        "lshoulder": None
    }

def parseButton(event):
    if event.type == pygame.JOYAXISMOTION and event.value != 0:
        value = "1"
        if event.value < 0:
            value = "-1"
        return BITDO_KEY_MAPPINGS_JOYAXIS[str(event.axis), value]
    elif event.type == pygame.JOYBUTTONDOWN:
        return BITDO_KEY_MAPPINGS_JOYBUTTON[str(event.button)]