from evdev import InputDevice, categorize, ecodes

#A_BTN = 304
A_BTN = 30
X_BTN = 305
#B_BTN = 306
B_BTN = 48
Y_BTN = 307
HOME_BTN = 316
R_SHOULDER_BTN = 318
R_TRIGGER_BTN = 319
R_ANALOG_CLICK = 315



class ControllerR:
    def __init__(self):
        self.buttonMap = {}

    def mapButtonAction(self, button, fn):
        self.buttonMap[button] = fn;




def RunEventLoop(fn):
    gamepad = InputDevice('/dev/input/event1')
    
    print("in RunEventLoop")
    for event in gamepad.read_loop():
        print("in for loop")
        if event.type == ecodes.EV_KEY:
            print("event.type == ecodes.EV_KEY")
            if event.value == 1:
                if event.code == A_BTN:
                    print("A")
                    fn('player1')
                elif event.code == 306:
                    print("B")
                elif event.code == B_BTN:
                    print("B")
                    fn('player2')
                elif event.code == 305:
                    print("X")
                
                print(event)


def GetRawInput():
    gamepad = InputDevice('/dev/input/event1')
    print(gamepad)
    for event in gamepad.read_loop():
        print(categorize(event))
