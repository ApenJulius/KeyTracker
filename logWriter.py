from pynput import keyboard
import time
current_time = time.time()
formatted_time = time.strftime("%H_%M_%d_%m", time.localtime(current_time))

file = open(f"logs/output_{formatted_time}.txt", "a")

def type_correct(key): # Handles changing character standard
    try: 
        return listener.canonical(key).value # If special char use the code IE <27> for Key.esc
    except AttributeError: 
        return listener.canonical(key) # If not make unmodified char

def on_press(key):
    file.write(f"Down {type_correct(key)} at {time.time()}\n")

def on_release(key): # Recieves as standard uncorrected key type
    if key == keyboard.Key.esc:
        file.close() # Wont save unless closed
        return False # Stop listener
    file.write(f"Up {type_correct(key)} at {time.time()}\n")


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
   listener.join()