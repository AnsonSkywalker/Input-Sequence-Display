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
        if key == Key.space:
            key = "空格"
        elif key == Key.ctrl_l:
            key = "CTRL"
        elif key == Key.shift_l:
            key = "SHIFT" 
        elif key.char == "w":
            key = "W"
        elif key.char == "a":
            key = "A"
        elif key.char == "s":
            key = "S"
        elif key.char == "d":
            key = "D"
        elif key.char == "q":
            key = "Q"
        elif key.char == "e":
            key = "E"
        elif key.char == "f":
            key = "F"
        elif key.char == "r":
            key = "R"
        elif key.char == "g":
            key = "G"
        elif key.char == "x":
            key = "X"
        else:
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
