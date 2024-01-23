import time
from pynput.keyboard import Key, Listener

keys_currently_pressed = []
count = 0
flag = True
time_last = time.time_ns()
time_now = 0

tickrate = 60 # 每一秒钟记为多少帧，单位Hz
wait = 5 # 超过多长时间没有输入就忽略本次计数，单位秒

def on_press(key):
    global count,time_last,time_now
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
            elif key.char == "\x17": # Ctrl+W
                key = "W"
            elif key.char == "\x01": # Ctrl+A
                key = "A"
            elif key.char == "\x13": # Ctrl+S
                key = "S"
            elif key.char == "\x04": # Ctrl+D
                key = "D"
            else:
                flag = False
        except AttributeError:
            flag = False
        #else:
        #    key = str(key)
        #    key = key.replace("'", "")
        #    key = key.upper()    
        if flag:
            time_now=time.time_ns()
            count = int((time_now - time_last)/1000000000*tickrate)
            if count>(wait*tickrate):
                count = 9999 # 意为超时，间隔无效请忽略
            print(count,"帧 ",format(key),flush = True)
            time_last = time_now    

def on_release(key):
    global n
    if key in keys_currently_pressed:
        keys_currently_pressed.remove(key)
    #print(key, '键抬起')

listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("监听键位输入序列已启动。当前监听帧率：",tickrate,"Hz")
while True:
    pass
