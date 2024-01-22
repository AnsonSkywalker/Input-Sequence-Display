import time
from pynput.keyboard import Key, Listener

keys_currently_pressed = []
count = 0
flag = True

def on_press(key):
    global count
    if key not in keys_currently_pressed:
        keys_currently_pressed.append(key)
        flag = True
        try:
            if key == Key.space:
                key = "空格"
            elif key == Key.ctrl_l:
                key = "CTRL"
            elif key == Key.shift_l:
                key = "SHIFT" 
            elif key.char.lower() == "w":
                key = "W"
            elif key.char.lower() == "a":
                key = "A"
            elif key.char.lower() == "s":
                key = "S"
            elif key.char.lower() == "d":
                key = "D"
            elif key.char.lower() == "q":
                key = "Q"
            elif key.char.lower() == "e":
                key = "E"
            elif key.char.lower() == "f":
                key = "F"
            elif key.char.lower() == "r":
                key = "R"
            elif key.char.lower() == "g":
                key = "G"
            elif key.char.lower() == "x":
                key = "X"
            else:
                flag = False
        except AttributeError:
            flag = False
        #else:
        #    key = str(key)
        #    key = key.replace("'", "")
        #    key = key.upper()    
        if flag:
            count = 0
            print("帧后击键：{}".format(key))      

def on_release(key):
    global n
    if key in keys_currently_pressed:
        keys_currently_pressed.remove(key)
    #print(key, '键抬起')

listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    print(count,end='')
    count += 1
    time.sleep(0.0167)
    print("\r",end="")
