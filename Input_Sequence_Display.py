import time
from pynput.keyboard import Key, Listener
import obspython as obs
import sys
from io import StringIO

buffer = StringIO()
keys_currently_pressed = []
count = 0
flag = True
time_last = time.time_ns()
time_now = 0
source_name = ""

tickrate = 60 # 每一秒钟记为多少帧，单位Hz
wait = 5 # 超过多长时间没有输入就忽略本次计数，单位秒

sys.stdout = buffer

def update_text():
    global source_name

    source = obs.obs_get_source_by_name(source_name)
    text = buffer.getvalue()
    if source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", text)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)

        obs.obs_source_release(source)

def script_properties():
	props = obs.obs_properties_create()
      
	p = obs.obs_properties_add_list(props, "source", "Text Source", obs.OBS_COMBO_TYPE_EDITABLE,obs.OBS_COMBO_FORMAT_STRING)
	sources = obs.obs_enum_sources()
	if sources is not None:
		for source in sources:
			source_id = obs.obs_source_get_unversioned_id(source)
			if source_id == "text_gdiplus" or source_id == "text_ft2_source":
				name = obs.obs_source_get_name(source)
				obs.obs_property_list_add_string(p, name, name)

		obs.source_list_release(sources)
          
	return props

def script_update(settings):
    global source_name
    source_name = obs.obs_data_get_string(settings, "source")
    obs.timer_remove(update_text)
    if source_name != "":
        obs.timer_add(update_text, 1)

def script_description():
	return "在OBS内以滚动序列形式显示用户键盘输入\nDisplay the user's keyboard input in a scrolling sequence\n\nBy Anson_Skywalker"

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
            '''
            else:
                key = str(key)
                key = key.replace("'", "")
                key = key.upper()
            '''
        except:
            flag = False  
        if flag:
            time_now=time.time_ns()
            count = int((time_now - time_last)/1000000000*tickrate)
            if count>(wait*tickrate):
                count = 9999 # 意为超时，间隔无效请忽略
            print(count,"帧 ",format(key),flush = True)
            time_last = time_now    

def on_release(key):
    if key in keys_currently_pressed:
        keys_currently_pressed.remove(key)
    #print(key, '键抬起')

listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("监听键位输入序列已启动。当前监听帧率：",tickrate,"Hz")
