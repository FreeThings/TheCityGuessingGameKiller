from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()

class Keys:
    def __init__(self, c_key):
        self.c_key = c_key
    
    def input_key(self):
        keyboard.press(self.c_key)
        keyboard.release(self.c_key)
        
    def enter(self):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)