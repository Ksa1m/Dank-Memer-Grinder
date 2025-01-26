import time as t
import threading
import random
import importlib

import pyautogui as kp
import customtkinter as ctk
import keyboard as kb
import config




def set_config(variable, value, config_file="config.py"):
    try:
        with open(config_file, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        variable_found = False
        for line in lines:
            if line.strip().startswith(variable):
                key, _ = line.split('=', 1)
                updated_lines.append(f"{key.strip()} = {value}\n")
                variable_found = True
            else:
                updated_lines.append(line)

        if not variable_found:
            return f"Error: Variable '{variable}' not found in {config_file}."

        with open(config_file, 'w') as file:
            file.writelines(updated_lines)

        return f"Successfully set '{variable}' to {value}."

    except FileNotFoundError:
        return f"Error: Config file '{config_file}' not found."
    except Exception as e:
        return f"Error: {e}"








postmemes_delay = 36
search_delay = 25
crime_delay = 46
beg_delay = 42
hunt_delay = 22
stream_delay = 1810 # Required keyboard & mouse


timer = 352


running = False

def timer_stop():
    global running
    running = False

def timer_loop():
    global timer, running
    while running:
        # update()
        timer += 1
        t.sleep(1)


def timer_start():
    global running
    thread = threading.Thread(target=timer_loop, daemon=True)
    thread.start()


timer_start()




def Toggle():
    global running
    running = not running
    start_btn.configure(text="Start")

    if running:
        timer_start()
        start_thread()
    else:
        reset_text()

def start():
    start_btn.configure(text="Running")
    while running:
        if timer % postmemes_delay == 0:
            postmemes()

        if timer % beg_delay == 0:
            beg()

        if timer % hunt_delay == 0:
            hunt()

        if timer % crime_delay == 0:
            crime()

        if timer % search_delay == 0:
            search()

        if timer % stream_delay == 0:
            search()
        
        t.sleep(1)




running_text = "Running"


def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}m {remaining_seconds}s"


def update():
    global running, running_text, timer
    
    if running:
        # Running
        if "...." in running_text:
            running_text = "Running"

        start_btn.configure(text=running_text)

        running_text += "."


        # Begging

        remainder = timer % beg_delay
        if remainder == 0:
            begging_left = beg_delay
        else:
            begging_left = beg_delay - remainder
        
        begging_text = f"Beg: {begging_left}"
        
        beg_btn.configure(text=begging_text)

        # Hunting

        remainder = timer % hunt_delay
        if remainder == 0:
            hunting_left = hunt_delay
        else:
            hunting_left = hunt_delay - remainder
        
        hunting_text = f"Hunt: {hunting_left}"
        
        hunt_btn.configure(text=hunting_text)

        # Crime

        remainder = timer % crime_delay
        if remainder == 0:
            crime_left = crime_delay
        else:
            crime_left = crime_delay - remainder
        
        crime_text = f"Crime: {crime_left}"
        
        crime_btn.configure(text=crime_text)

        # Search
        if not config.safe_mode:
            remainder = timer % search_delay
            if remainder == 0:
                search_left = search_delay
            else:
                search_left = search_delay - remainder
            
            search_text = f"Search: {search_left}"
            
            search_btn.configure(text=search_text)

        # Postmemes

        remainder = timer % postmemes_delay
        if remainder == 0:
            postmemes_left = postmemes_delay
        else:
            postmemes_left = postmemes_delay - remainder
        
        postmemes_text = f"Postmemes: {postmemes_left}"
        
        postmemes_btn.configure(text=postmemes_text)

        # Stream
        
        if config.stream_unlocked:
            remainder = timer % stream_delay
            if remainder == 0:
                stream_left = stream_delay
            else:
                stream_left = stream_delay - remainder
            
            stream_left_last = seconds_to_minutes(stream_left)
            stream_text = f"Stream: {stream_left_last}"
            
            stream_btn.configure(text=stream_text)


def reset_text():
    beg_btn.configure(text="Beg")
    hunt_btn.configure(text="Hunt")
    crime_btn.configure(text="Crime")
    search_btn.configure(text="Search")
    postmemes_btn.configure(text="Postmemes")
    stream_btn.configure(text="Stream")


# region Functions

def beg():
    kp.typewrite("/beg")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

def hunt():
    kp.typewrite("/hunt")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')


def crime():
    kp.typewrite("/crime")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    xs = [525, 555, 685]
    y = 990
    x = random.choice(xs)
    kp.leftClick(x, y)

    kp.moveTo(pos)



def search():
    if config.safe_mode:
        return
    
    kp.typewrite("/search")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    xs = [525, 555, 685]
    y = 990
    x = random.choice(xs)
    kp.leftClick(x, y)

    kp.moveTo(pos)



def postmemes():
    kp.typewrite("/postmemes")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1.5)
    pos = kp.position()

    # type
    x = 550

    kp.leftClick(x, 950)

    ys = [905, 870, 832, 794, 756]
    y = random.choice(ys)

    kp.leftClick(x, y)

    t.sleep(1)
    # platform
    kp.leftClick(x, 900)

    x = 550
    ys = [850, 800, 730, 700, 650]
    y = random.choice(ys)
    kp.leftClick(x, y)

    t.sleep(1)

    y = 990
    x = 525
    kp.leftClick(x, y)

    kp.moveTo(pos)



def stream():
    kp.typewrite("/stream")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    y = 990
    x = 525
    kp.leftClick(x, y)
    t.sleep(1)
    kp.leftClick(x, y)
    t.sleep(1)
    kp.leftClick(x, y)
    t.sleep(1)
    kp.moveTo(pos)




def start_thread():
    bot_thread = threading.Thread(target=start, daemon=True)
    bot_thread.start()



# region GUI


app = ctk.CTk()
app.title("Dank Memer Bot")
app.geometry("540x340+700+100")





def enable_window():
    app.attributes("-topmost", True)
def disable_window():
    app.attributes("-topmost", False)





def toggle_window():
    set_config("window_enabled", not config.window_enabled)
    importlib.reload(config)
    set_window()

def set_window():
    if config.window_enabled:
        enable_window()
    else:
        disable_window()



set_window()


def toggle_stream():
    set_config("stream_unlocked", not config.stream_unlocked)
    importlib.reload(config)
    set_stream()

def set_stream():
    if not config.stream_unlocked:
        stream_btn.configure(state="disabled")
    else:
        stream_btn.configure(state="normal")



def toggle_safe():
    set_config("safe_mode", not config.safe_mode)
    importlib.reload(config)
    set_search()

def set_search():
    if config.safe_mode:
        search_btn.configure(state="disabled")
    else:
        search_btn.configure(state="normal")




        


app.grid_columnconfigure(0, weight=1)

main_frame = ctk.CTkFrame(app)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="new")

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)






# Example for adding widgets to the main frame
title_label = ctk.CTkLabel(main_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=0, padx=0, pady=0, columnspan=3, sticky="ew")



def bind_key(key):
    kb.add_hotkey(key, Toggle)

bind_key(config.key)



def change_key():
    key_btn.configure(text="Press a key...")  

    def capture_key():
        ehh_key = kb.read_key()
        frfr_key = str(ehh_key).capitalize()
        set_config("key", f'"{frfr_key}"')
        # bind_key(frfr_key)
        key_btn.configure(text=f"Press {frfr_key} to toggle")

    if config.key in kb._hotkeys:
        kb.remove_hotkey(config.key)
    key_thread = threading.Thread(target=capture_key, daemon=True)
    key_thread.start()



key_btn = ctk.CTkButton(main_frame, text=f"Press {config.key} to toggle", command=change_key, width=100)
key_btn.grid(row=0, column=2, padx=10, pady=10, sticky="e")












commands_frame = ctk.CTkFrame(app)
commands_frame.grid(row=1, column=0, padx=10, pady=0, sticky="new")

commands_frame.grid_columnconfigure(0, weight=1)
commands_frame.grid_columnconfigure(1, weight=1)
commands_frame.grid_columnconfigure(2, weight=1)



start_btn = ctk.CTkButton(commands_frame, text="Start", command=Toggle)
start_btn.grid(row=0, column=1, padx=20, pady=10)

beg_btn = ctk.CTkButton(commands_frame, text="Beg", command=beg)
beg_btn.grid(row=1, column=0, padx=20, pady=10)

hunt_btn = ctk.CTkButton(commands_frame, text="Hunt", command=hunt)
hunt_btn.grid(row=1, column=1, padx=20, pady=10)

crime_btn = ctk.CTkButton(commands_frame, text="Crime", command=crime)
crime_btn.grid(row=1, column=2, padx=20, pady=10)

search_btn = ctk.CTkButton(commands_frame, text="Search", command=search)
search_btn.grid(row=2, column=0, padx=20, pady=10)

set_search()

postmemes_btn = ctk.CTkButton(commands_frame, text="Postmemes", command=postmemes)
postmemes_btn.grid(row=2, column=1, padx=20, pady=10)

stream_btn = ctk.CTkButton(commands_frame, text="Stream", command=stream)
stream_btn.grid(row=2, column=2, padx=20, pady=10)

set_stream()







settings_frame = ctk.CTkFrame(app)
settings_frame.grid(row=2, column=0, padx=10, pady=10, sticky="new")

settings_frame.grid_columnconfigure(0, weight=1)
settings_frame.grid_columnconfigure(1, weight=1)
settings_frame.grid_columnconfigure(2, weight=1)



topwin_check = ctk.CTkCheckBox(settings_frame, text="Window on top", command=toggle_window)
topwin_check.grid(row=0, column=0, padx=10, pady=10)

stream_check = ctk.CTkCheckBox(settings_frame, text="Stream Unlocked", command=toggle_stream)
stream_check.grid(row=0, column=1, padx=10, pady=10)

safe_check = ctk.CTkCheckBox(settings_frame, text="Safe Mode", command=toggle_safe)
safe_check.grid(row=0, column=2, padx=10, pady=10)




def set_checks():
    if config.stream_unlocked:
        stream_check.select()
    else:
        stream_check.deselect()


    if config.window_enabled:
        topwin_check.select()
    else:
        topwin_check.deselect()


    if config.safe_mode:
        safe_check.select()
    else:
        safe_check.deselect()

set_checks()


time_label = ctk.CTkLabel(settings_frame, text=f"Load time: {config.load_time}", font=ctk.CTkFont(size=15))
time_label.grid(row=1, column=0, padx=10, pady=10)

def set_time(value):
    value = round(value, 1)
    set_config("load_time", value)
    time_label.configure(text=f"Load time: {value}")

time_sl = ctk.CTkSlider(settings_frame, width=150, from_=0.1, to=2,command=set_time)
time_sl.grid(row=2, column=0, padx=10, pady=0)

time_sl.set(config.load_time)


app.mainloop()
