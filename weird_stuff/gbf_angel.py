from pynput.mouse import Button, Controller
import time
mouse = Controller()
def go(pos):
    mouse.position = pos
    mouse.press(Button.left)
    mouse.release(Button.left)
time.sleep(3)
while 1:
    print(mouse.position)
    mouse.position = (935,358)
    go((935,358))
    print(mouse.position)
    time.sleep(3)
    mouse.position = (1023,544)
    go((1023,544))
    print(mouse.position)
    time.sleep(15)
    mouse.position = (1083,375)
    go((1083,375))
    time.sleep(2)
    mouse.position =(820,393)
    go((820,393))
    print(mouse.position)
    time.sleep(36)
    mouse.position = (948,474)
    go((948,474))
    print(mouse.position)
    time.sleep(3)
    mouse.position = (877,405)
    go((877,405))
    print(mouse.position)
    time.sleep(3)