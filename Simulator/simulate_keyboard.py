from pynput.keyboard import Key, Controller
from time import sleep
import random

def Type(path: str = None, delay: int = None, code: str = None, key_delay: float = 0.1, line_delay: float = 0.1):
    # If the Argument is negative
    if not delay:
        delay = 3

    if delay < 0:
        print("Hmmmmmmmmm 😱 Interesting Time is negative 🥲")
        delay = abs(delay)

    # wait for few seconds before typing
    sleep(delay)
    
    # manually enter your code here or provide a path
    if path:
        with open(path, "r") as file:
            code = file.read()
    elif code:
        pass
    else:
        code = """
    class Complex:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        """

    keyboard = Controller()
    for line in code.split("\n"):
        for char in line:
            # keyboard.type(char)
            if char.isupper():
                keyboard.press(Key.shift)
                keyboard.press(char.lower())
                keyboard.release(char.lower())
                keyboard.release(Key.shift)
            elif char == '!':
                keyboard.press(Key.shift)
                keyboard.press(key='1')
                keyboard.release(key='1')
                keyboard.release(Key.shift)
            elif char == '@':
                keyboard.press(Key.shift)
                keyboard.press(key='2')
                keyboard.release(key='2')
                keyboard.release(Key.shift)
            elif char == '#':
                keyboard.press(Key.shift)
                keyboard.press(key='3')
                keyboard.release(key='3')
                keyboard.release(Key.shift)
            elif char == '$':
                keyboard.press(Key.shift)
                keyboard.press(key='4')
                keyboard.release(key='4')
                keyboard.release(Key.shift)
            elif char == '%':
                keyboard.press(Key.shift)
                keyboard.press(key='5')
                keyboard.release(key='5')
                keyboard.release(Key.shift)
            elif char == '^':
                keyboard.press(Key.shift)
                keyboard.press(key='6')
                keyboard.release(key='6')
                keyboard.release(Key.shift)
            elif char == '&':
                keyboard.press(Key.shift)
                keyboard.press(key='7')
                keyboard.release(key='7')
                keyboard.release(Key.shift)
            elif char == '*':
                keyboard.press(Key.shift)
                keyboard.press(key='8')
                keyboard.release(key='8')
                keyboard.release(Key.shift)
            elif char == '(':
                keyboard.press(Key.shift)
                keyboard.press(key='9')
                keyboard.release(key='9')
                keyboard.release(Key.shift)
            elif char == ')':
                keyboard.press(Key.shift)
                keyboard.press(key='0')
                keyboard.release(key='0')
                keyboard.release(Key.shift)
            elif char == '+':
                keyboard.press(Key.shift)
                keyboard.press(key='=')
                keyboard.release(key='=')
                keyboard.release(Key.shift)
            elif char == ':':
                keyboard.press(Key.shift)
                keyboard.press(key=';')
                keyboard.release(key=';')
                keyboard.release(Key.shift)
            elif char == '?':
                keyboard.press(Key.shift)
                keyboard.press(key='/')
                keyboard.release(key='/')
                keyboard.release(Key.shift)
            elif char == '<':
                keyboard.press(Key.shift)
                keyboard.press(key=',')
                keyboard.release(key=',')
                keyboard.release(Key.shift)
            elif char == '>':
                keyboard.press(Key.shift)
                keyboard.press(key='.')
                keyboard.release(key='.')
                keyboard.release(Key.shift)
            else:
                keyboard.press(char)  # 直接输入字符
                keyboard.release(char)
            # add a random time delay
            # min = raw_delay * 0.1
            # max = raw_delay * 1.9
            rdm_amplifier = 0.9
            key_delay_simui_max = int((key_delay*(1+rdm_amplifier))*1000)
            key_delay_simui_min = int((key_delay*(1-rdm_amplifier))*1000)
            key_delay_simui = random.randint(key_delay_simui_min,key_delay_simui_max)
            key_delay_simuf = key_delay_simui/1000.0
            sleep(key_delay_simuf)  # Add a key_delay seconds between each keystroke
        keyboard.tap(Key.enter)
        keyboard.tap(Key.home)
        sleep(line_delay)  # Add a line_delay seconds between each line
