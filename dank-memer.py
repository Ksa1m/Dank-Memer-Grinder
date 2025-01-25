import time as t
import threading
import random
import importlib

import pyautogui as kp
import customtkinter as ctk
import keyboard as kb
import config




def toggle_config(variable_name, config_file="config.py"):
    try:
        with open(config_file, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            if line.strip().startswith(variable_name):
                key, value = line.split('=')
                new_value = "False" if value.strip() == "True" else "True" if value.strip() == "False" else None
                if new_value is None:
                    return f"Error: Variable '{variable_name}' is not a boolean."
                updated_lines.append(f"{key.strip()} = {new_value}\n")
            else:
                updated_lines.append(line)

        if not any(line.startswith(variable_name) for line in lines):
            return f"Error: Variable '{variable_name}' not found in {config_file}."

        with open(config_file, 'w') as file:
            file.writelines(updated_lines)

        return f"Successfully toggled '{variable_name}'."

    except FileNotFoundError:
        return f"Error: Config file '{config_file}' not found."
    except Exception as e:
        return f"Error: {e}"







postmemes_delay = 30  # click
search_delay = 25  # click
crime_delay = 44 # 40 # click 
beg_delay = 42  # 40
hunt_delay = 22 # 20
stream_delay = 1800 # Required keyboard & mouse




timer = 296
running = False

# region timer
def timer_stop():
    global running
    running = False

def timer_loop():
    global timer, running
    while running:
        update()
        timer += 1
        # print(timer)
        t.sleep(1)


def timer_start():
    global running
    thread = threading.Thread(target=timer_loop, daemon=True)
    thread.start()

# endregion

timer_start()






def Toggle():
    global running
    running = not running
    # print(f"Running: {running}")
    start_btn.configure(text="Start")

    if running:
        timer_start()
        start_thread()
    else:
        reset_text()

def start():
    start_btn.configure(text="Running")
    while running:
        if kb.is_pressed('f7'):
            print("Toggling...")
            Toggle()

        
        if timer % beg_delay == 0:
            beg()

        if timer % hunt_delay == 0:
            hunt()

        if timer % crime_delay == 0:
            crime()

        if timer % search_delay == 0:
            search()

        if timer % postmemes_delay == 0:
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

        # Crime

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
    # print("begging")
    kp.typewrite("/beg")
    t.sleep(0.2)
    kp.press('enter')
    kp.press('enter')

def hunt():
    # print("hunting")
    kp.typewrite("/hunt")
    t.sleep(0.2)
    kp.press('enter')


def crime():
    # print("crime")
    kp.typewrite("/crime")
    t.sleep(0.2)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    xs = [455, 555, 685]
    y = 990
    x = random.choice(xs)
    kp.leftClick(x, y)

    kp.moveTo(pos)

    kp.press('enter')


def search():
    # print("searching")
    kp.typewrite("/search")
    t.sleep(0.2)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    xs = [455, 555, 685]
    y = 990
    x = random.choice(xs)
    kp.leftClick(x, y)

    kp.moveTo(pos)



def postmemes():
    # print("postmemes")
    kp.typewrite("/postmemes")
    t.sleep(0.2)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    y = 990
    x = 440
    kp.leftClick(x, y)

    kp.moveTo(pos)



def stream():
    # print("postmemes")
    kp.typewrite("/stream")
    t.sleep(0.2)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    y = 990
    x = 440
    kp.leftClick(x, y)
    t.sleep(1)
    y = 990
    x = 440
    kp.leftClick(x, y)
    t.sleep(1)
    y = 990
    x = 440
    kp.leftClick(x, y)
    t.sleep(1)
    kp.moveTo(pos)


# endregion 

def start_thread():
    bot_thread = threading.Thread(target=start, daemon=True)
    bot_thread.start()


def bind_key():
    kb.add_hotkey('f8', Toggle)

bind_key()



# GUI

app = ctk.CTk()
app.title("Dank Memer Bot")
app.geometry("540x300+700+100")


def enable_window():
    app.attributes("-topmost", True)
def disable_window():
    app.attributes("-topmost", False)





def toggle_window():
    toggle_config("window_enabled")
    importlib.reload(config)
    set_window()

def set_window():
    if config.window_enabled:
        enable_window()
    else:
        disable_window()



set_window()



def set_stream():
    if not config.stream_unlocked:
        stream_btn.configure(state="disabled")
    else:
        stream_btn.configure(state="normal")




def toggle_stream():
    global stream_btn
    toggle_config("stream_unlocked")
    importlib.reload(config)
    set_stream()



        




title_label = ctk.CTkLabel(app, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=1, padx=0, pady=10)



start_btn = ctk.CTkButton(app, text="Start", command=Toggle)
start_btn.grid(row=1, column=1, padx=20, pady=20)

beg_btn = ctk.CTkButton(app, text="Beg", command=beg)
beg_btn.grid(row=2, column=0, padx=20, pady=20)

hunt_btn = ctk.CTkButton(app, text="Hunt", command=hunt)
hunt_btn.grid(row=2, column=1, padx=20, pady=20)

crime_btn = ctk.CTkButton(app, text="Crime", command=crime)
crime_btn.grid(row=2, column=2, padx=20, pady=20)

search_btn = ctk.CTkButton(app, text="Search", command=search)
search_btn.grid(row=3, column=0, padx=20, pady=20)

postmemes_btn = ctk.CTkButton(app, text="Postmemes", command=postmemes)
postmemes_btn.grid(row=3, column=1, padx=20, pady=20)

stream_btn = ctk.CTkButton(app, text="Stream", command=stream)
stream_btn.grid(row=3, column=2, padx=20, pady=20)

set_stream()


topwin_check = ctk.CTkCheckBox(app, text="Always see this window", command=toggle_window)
topwin_check.grid(row=4, column=0)

stream_check = ctk.CTkCheckBox(app, text="Stream Unlocked", command=toggle_stream)
stream_check.grid(row=4, column=1)

def set_checks():
    if config.stream_unlocked:
        stream_check.select()
    else:
        stream_check.deselect()


    if config.window_enabled:
        topwin_check.select()
    else:
        topwin_check.deselect()

set_checks()


app.mainloop()
