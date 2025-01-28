import time as t
import threading
import random
import importlib
import config
import os
from datetime import datetime


# region Imports

import pyautogui as kp
import customtkinter as ctk
import keyboard as kb




# ---------------------------------------------------------------------------------------------------------
#
# Write `pip install pyautogui customtkinter keyboard` in cmd to install libraries if not installed already
#
# ---------------------------------------------------------------------------------------------------------




path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py") # get path to config.py


def set_config(variable, value):
    try:
        with open(path, 'r') as file:
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
            print(f"Error: Variable '{variable}' not found in {path}.")
            return

        with open(path, 'w') as file:
            file.writelines(updated_lines)

        # print(f"Successfully set '{variable}' to {value}.")
        return

    except FileNotFoundError:
        print(f"Error: Config file '{path}' not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return








postmemes_delay = 36
search_delay = 30
crime_delay = 46
beg_delay = 42
hunt_delay = 22
stream_delay = 1820 # Requires keyboard & mouse

def get_time():
    local_time = datetime.now()

    hours = local_time.hour
    minutes = local_time.minute
    seconds = local_time.second

    total_seconds = (hours * 3600) + (minutes * 60) + seconds

    return total_seconds


timer = get_time()




running = False

def timer_stop():
    global running
    running = False

def timer_loop():
    global timer, running
    while running:
        update()
        timer += 1
        t.sleep(1)


def timer_start():
    global running
    thread = threading.Thread(target=timer_loop, daemon=True)
    thread.start()


timer_start()


# region Functions

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
        if timer % stream_delay == 0:
            stream()

        t.sleep(1)

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
        if not config.safe_mode:
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


command = False


def run(target_function, *args, **kwargs):
    thread = threading.Thread(target=target_function, args=args, kwargs=kwargs, daemon=True)
    thread.start()



def beg():   
    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(460, 1040)
    kp.moveTo(pos)

    kp.typewrite("/beg")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    command = False


def hunt():
    
    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(460, 1040)
    kp.moveTo(pos)

    kp.typewrite("/hunt")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    command = False


def crime():
    if config.safe_mode:
        return

    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(460, 1040)
    kp.moveTo(pos)

    kp.typewrite("/crime")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    kp.leftClick(460, 990)

    kp.moveTo(pos)

    command = False



def search():
    if config.safe_mode:
        return
    
    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(460, 1040)
    kp.moveTo(pos)

    kp.typewrite("/search")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    kp.leftClick(460, 990)

    kp.moveTo(pos)

    command = False



def postmemes():
    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(460, 1040)
    kp.moveTo(pos)

    kp.typewrite("/postmemes")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1.5)

    pos = kp.position()

    # type

    kp.leftClick(460, 950)

    ys = [900, 870, 830, 790, 760]
    y = random.choice(ys)

    kp.leftClick(460, y)

    t.sleep(1)
    # platform
    kp.leftClick(460, 900)

    ys = [850, 800, 730, 700, 650]
    y = random.choice(ys)
    kp.leftClick(460, y)

    t.sleep(1)

    kp.leftClick(460, 990)

    kp.moveTo(pos)

    command = False





def stream():
    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(460, 1040)
    kp.moveTo(pos)

    kp.typewrite("/stream")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(2)

    pos = kp.position()


    ys =  [ 990, # main
            945, # select game
            910, # game 1
            875, # game 2
            830, # game 3
            800, # game 4
            760, # game 5
        ]


    kp.leftClick(460, ys[0])

    t.sleep(1)
    kp.leftClick(460, ys[1])

    t.sleep(config.load_time)
    game = random.randint(2, 6)
    kp.leftClick(460, ys[game])

    t.sleep(1)
    kp.leftClick(460, ys[0])

    t.sleep(1)
    kp.moveTo(pos)

    command = False




def start_thread():
    bot_thread = threading.Thread(target=start, daemon=True)
    bot_thread.start()




# region GUI

app = ctk.CTk()
app.title("Dank Memer Bot")
app.geometry("800x400+460+100")



# Sidebar Frame
sidebar_frame = ctk.CTkFrame(app, width=150, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky="nsw")



# Content Frame
content_frame = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
content_frame.grid(row=0, column=1, padx=10, sticky="nsew")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)



# Tab Frames for Switching
main_tab_frame = ctk.CTkFrame(content_frame, corner_radius=10)
settings_tab_frame = ctk.CTkFrame(content_frame, corner_radius=10)



content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_rowconfigure(0, weight=1)



settings_tab_frame.grid_columnconfigure(0, weight=1)
settings_tab_frame.grid_columnconfigure(1, weight=1)
settings_tab_frame.grid_columnconfigure(2, weight=1)



main_tab_frame.grid_columnconfigure(0, weight=1)  # Center horizontally






# region GUI Functions


def enable_window():
    app.attributes("-topmost", True)
def disable_window():
    app.attributes("-topmost", False)


def set_window():
    if config.window_enabled:
        enable_window()
    else:
        disable_window()


def toggle_window():
    set_config("window_enabled", not config.window_enabled)
    importlib.reload(config)
    set_window()


set_window()




def set_stream():
    if not config.stream_unlocked:
        stream_btn.configure(state="disabled")
    else:
        stream_btn.configure(state="normal")


def toggle_stream():
    set_config("stream_unlocked", not config.stream_unlocked)
    importlib.reload(config)
    set_stream()




def toggle_safe():
    set_config("safe_mode", not config.safe_mode)
    importlib.reload(config)
    set_safe()


def set_safe():
    if config.safe_mode:
        search_btn.configure(state="disabled")
        crime_btn.configure(state="disabled")
    else:
        search_btn.configure(state="normal")
        crime_btn.configure(state="normal")




def switch_tab(tab_name):
    # Hide all tabs
    for widget in content_frame.winfo_children():
        widget.grid_forget()

    if tab_name == "main":
        main_tab_frame.grid(row=0, column=0, sticky="nsew")
    elif tab_name == "settings":
        settings_tab_frame.grid(row=0, column=0, sticky="nsew")




# Sidebar Buttons
main_btn = ctk.CTkButton(sidebar_frame, text="Main", command=lambda: switch_tab("main"))
main_btn.grid(row=0, column=0, pady=15, padx=10)

settings_btn = ctk.CTkButton(sidebar_frame, text="Settings", command=lambda: switch_tab("settings"))
settings_btn.grid(row=1, column=0, pady=15, padx=10)

app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)



switch_tab("main")




title_label = ctk.CTkLabel(main_tab_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=0, padx=0, pady=10, sticky="new")



def bind_key(key):
    kb.add_hotkey(key, Toggle)

bind_key(config.key)



def change_key():
    key_btn.configure(text="Press a key...")  

    def capture_key():
        ehh_key = kb.read_key()
        frfr_key = str(ehh_key).capitalize()
        set_config("key", f'"{frfr_key}"')
        bind_key(frfr_key)
        key_btn.configure(text=f"Press {frfr_key} to toggle")

    if config.key in kb._hotkeys:
        kb.remove_hotkey(config.key)
    key_thread = threading.Thread(target=capture_key, daemon=True)
    key_thread.start()



key_btn = ctk.CTkButton(settings_tab_frame, text=f"Press {config.key} to toggle", command=change_key)
key_btn.grid(row=2, column=1, padx=0, pady=0)

key_text = ctk.CTkLabel(settings_tab_frame, text="Key to toggle the bot: ", font=ctk.CTkFont(size=15))
key_text.grid(row=1, column=1, padx=(7, 0), pady=0)




commands_frame = ctk.CTkFrame(main_tab_frame)
commands_frame.grid(row=1, column=0, padx=10, pady=0)

commands_frame.grid_columnconfigure(0, weight=1)
commands_frame.grid_columnconfigure(1, weight=1)
commands_frame.grid_columnconfigure(2, weight=1)
commands_frame.grid_rowconfigure(0, weight=1)



start_btn = ctk.CTkButton(commands_frame, text="Start", command=Toggle)
start_btn.grid(row=0, column=1, padx=20, pady=10)

beg_btn = ctk.CTkButton(commands_frame, text="Beg", command=lambda: run(beg))
beg_btn.grid(row=1, column=0, padx=20, pady=10)

hunt_btn = ctk.CTkButton(commands_frame, text="Hunt", command=lambda: run(hunt))
hunt_btn.grid(row=1, column=1, padx=20, pady=10)

crime_btn = ctk.CTkButton(commands_frame, text="Crime", command=lambda: run(crime))
crime_btn.grid(row=1, column=2, padx=20, pady=10)

search_btn = ctk.CTkButton(commands_frame, text="Search", command=lambda: run(search))
search_btn.grid(row=2, column=0, padx=20, pady=10)

set_safe()

postmemes_btn = ctk.CTkButton(commands_frame, text="Postmemes", command=lambda: run(postmemes))
postmemes_btn.grid(row=2, column=1, padx=20, pady=10)

stream_btn = ctk.CTkButton(commands_frame, text="Stream", command=lambda: run(stream))
stream_btn.grid(row=2, column=2, padx=20, pady=10)

set_stream()



topwin_check = ctk.CTkCheckBox(settings_tab_frame, text="Window on top", command=toggle_window)
topwin_check.grid(row=0, column=0, padx=10, pady=20)

stream_check = ctk.CTkCheckBox(settings_tab_frame, text="Stream Unlocked", command=toggle_stream)
stream_check.grid(row=0, column=1, padx=10, pady=20)

safe_check = ctk.CTkCheckBox(settings_tab_frame, text="Safe Mode", command=toggle_safe)
safe_check.grid(row=0, column=2, padx=10, pady=20)




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


time_label = ctk.CTkLabel(settings_tab_frame, text=f"Load time: {config.load_time}", font=ctk.CTkFont(size=15))
time_label.grid(row=1, column=0, padx=10, pady=0)

def set_time(value):
    value = round(value, 1)
    set_config("load_time", value)
    time_label.configure(text=f"Load time: {value}")


time_sl = ctk.CTkSlider(settings_tab_frame, width=150, from_=0.1, to=3,command=set_time)
time_sl.grid(row=2, column=0, padx=10, pady=0)
time_sl.set(config.load_time)


app.mainloop()
