import pynput, time
from pynput.keyboard import Key, Controller
time.sleep(2)
keyboard = Controller()
for x in range(100):
    keyboard.press(Key.cmd.value)
    keyboard.press('v')
    keyboard.release('v')
    # keyboard.release(Key.ctrl.value) #this would be for your key combination
    keyboard.release(Key.cmd.value)
    keyboard.press(Key.enter.value)
    keyboard.release(Key.enter.value)
    