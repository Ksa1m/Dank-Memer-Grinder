import time as t
import threading
import random
import importlib
import config
import os
from datetime import datetime
import requests
import subprocess
import webbrowser as browser

# required Imports

import pyautogui as kp
import customtkinter as ctk
import keyboard as kb
import pyscreeze as ps
import pygetwindow as gw


# -----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                                                                                      #
# Write `pip install pyautogui customtkinter keyboard requests pillow opencv-python pygetwindow` in cmd to install libraries if not installed already  #
#                                                                                                                                                      #
# -----------------------------------------------------------------------------------------------------------------------------------------------------#



path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.py")


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
    kp.leftClick(420, 1040)
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
    kp.leftClick(420, 1040)
    kp.moveTo(pos)

    kp.typewrite("/hunt")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    command = False

    rifle_thread.start()


def crime():
    if config.safe_mode:
        return

    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(420, 1040)
    kp.moveTo(pos)

    kp.typewrite("/crime")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    kp.leftClick(420, 970)

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
    kp.leftClick(420, 1040)
    kp.moveTo(pos)

    kp.typewrite("/search")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1)

    pos = kp.position()

    kp.leftClick(420, 970)

    kp.moveTo(pos)

    command = False



def postmemes():
    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(420, 1040)
    kp.moveTo(pos)

    kp.typewrite("/postmemes")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(1.5)

    pos = kp.position()

    # type

    kp.leftClick(420, 930)

    ys = [880, 850, 810, 760, 730]
    y = random.choice(ys)

    kp.leftClick(420, y)

    t.sleep(1)
    # platform
    kp.leftClick(420, 880)

    ys = [830, 775, 720, 660, 605]
    y = random.choice(ys)
    kp.leftClick(420, y)

    t.sleep(1)

    kp.leftClick(420, 970)

    kp.moveTo(pos)

    command = False





def stream():
    if not config.stream_unlocked:
        return

    global command
    if command:
        return
    command = True


    pos = kp.position()
    kp.mouseUp()
    kp.leftClick(420, 1040)
    kp.moveTo(pos)

    kp.typewrite("/stream")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')

    t.sleep(2)

    pos = kp.position()


    ys =  [ 970, # main
            925, # select game
            810, # game 1
            855, # game 2
            810, # game 3
            780, # game 4
            740, # game 5
        ]


    kp.leftClick(420, ys[0])

    t.sleep(1)
    kp.leftClick(420, ys[1])

    t.sleep(config.load_time)
    game = random.randint(2, 6)
    kp.leftClick(420, ys[game])

    t.sleep(1)
    kp.leftClick(420, ys[0])

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

# Sidebar Buttons
main_btn = ctk.CTkButton(sidebar_frame, text="Main", command=lambda: switch_tab("main"))
main_btn.grid(row=0, column=0, pady=15, padx=10)

settings_btn = ctk.CTkButton(sidebar_frame, text="Settings", command=lambda: switch_tab("settings"))
settings_btn.grid(row=1, column=0, pady=15, padx=10)

help_btn = ctk.CTkButton(sidebar_frame, text="Help", command=lambda: switch_tab("help"))
help_btn.grid(row=2, column=0, pady=15, padx=10)

app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)

# Content Frame
content_frame = ctk.CTkFrame(app, corner_radius=10, fg_color="transparent")
content_frame.grid(row=0, column=1, padx=10, sticky="nsew")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Tab Frames for Switching
main_tab_frame = ctk.CTkFrame(content_frame, corner_radius=10)
settings_tab_frame = ctk.CTkFrame(content_frame, corner_radius=10)
help_tab_frame = ctk.CTkFrame(content_frame, corner_radius=10)
discord_frame = ctk.CTkFrame(content_frame, corner_radius=10)

# Help Frames for Switching
about_frame = ctk.CTkFrame(content_frame, corner_radius=10)
config_frame = ctk.CTkFrame(content_frame, corner_radius=10)
help_frame = ctk.CTkFrame(content_frame, corner_radius=0)
discord_frame = ctk.CTkFrame(content_frame, corner_radius=0)

content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_rowconfigure(0, weight=1)

# region main
title_label = ctk.CTkLabel(main_tab_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=0, padx=0, pady=(10, 0), columnspan=3, sticky="nsew")

category_label = ctk.CTkLabel(main_tab_frame, text="Main", font=ctk.CTkFont(size=15))
category_label.grid(row=1, column=0, padx=0, pady=(0, 10), columnspan=3, sticky="nsew")


commands_frame = ctk.CTkFrame(main_tab_frame)
commands_frame.grid(row=2, column=0, padx=10, pady=0)

commands_frame.grid_columnconfigure(0, weight=1)
commands_frame.grid_columnconfigure(1, weight=1)
commands_frame.grid_columnconfigure(2, weight=1)
commands_frame.grid_rowconfigure(0, weight=1)
main_tab_frame.grid_columnconfigure(0, weight=1)

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

postmemes_btn = ctk.CTkButton(commands_frame, text="Postmemes", command=lambda: run(postmemes))
postmemes_btn.grid(row=2, column=1, padx=20, pady=10)

stream_btn = ctk.CTkButton(commands_frame, text="Stream", command=lambda: run(stream))
stream_btn.grid(row=2, column=2, padx=20, pady=10)


# region settings

settings_tab_frame.grid_columnconfigure(0, weight=1)
settings_tab_frame.grid_columnconfigure(1, weight=1)
settings_tab_frame.grid_columnconfigure(2, weight=1)

title_label = ctk.CTkLabel(settings_tab_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=1, padx=0, pady=(10, 0), sticky="new")

category_label = ctk.CTkLabel(settings_tab_frame, text="Settings", font=ctk.CTkFont(size=15))
category_label.grid(row=1, column=1, padx=0, pady=(0, 10), sticky="new")


settings_frame = ctk.CTkFrame(settings_tab_frame)
settings_frame.grid(row=2, column=1, padx=10, pady=0, sticky="nsew")

settings_frame.grid_columnconfigure(0, weight=1)
settings_frame.grid_columnconfigure(1, weight=1)
settings_frame.grid_columnconfigure(2, weight=1)
settings_frame.grid_rowconfigure(0, weight=1)

settings_tab_frame.grid_columnconfigure(0, weight=1)

key_btn = ctk.CTkButton(settings_frame, text=f"Press {config.key} to toggle", command=lambda: change_key())
key_btn.grid(row=2, column=1, padx=0, pady=(0, 20))

key_text = ctk.CTkLabel(settings_frame, text="Key to toggle the bot: ", font=ctk.CTkFont(size=15))
key_text.grid(row=1, column=1, padx=(7, 0), pady=0)



# region help


# About ------------------------------------------------------------

about_frame.grid_columnconfigure(0, weight=1)
about_frame.grid_columnconfigure(1, weight=1)
about_frame.grid_columnconfigure(2, weight=1)
about_frame.grid_rowconfigure(0, weight=0)


title_label = ctk.CTkLabel(about_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=1, column=1, padx=0, pady=(10, 0), sticky="new")

category_label = ctk.CTkLabel(about_frame, text="Help", font=ctk.CTkFont(size=15))
category_label.grid(row=2, column=1, padx=0, pady=(0, 10), sticky="new")


topbar_frame = ctk.CTkFrame(about_frame, height=50, corner_radius=10, fg_color="transparent")
topbar_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="ew")

topbar_frame.grid_columnconfigure(0, weight=1)
topbar_frame.grid_columnconfigure(1, weight=1)
topbar_frame.grid_columnconfigure(2, weight=1)

about_btn = ctk.CTkButton(topbar_frame, text="About", command=lambda: switch_help_tab("about"))
about_btn.grid(row=0, column=0, padx=10, pady=15)

config_btn = ctk.CTkButton(topbar_frame, text="Config", command=lambda: switch_help_tab("config"))
config_btn.grid(row=0, column=1, padx=10, pady=15)

help_btn = ctk.CTkButton(topbar_frame, text="Help", command=lambda: switch_help_tab("help"))
help_btn.grid(row=0, column=2, padx=10, pady=15)


about_frame.grid_columnconfigure(0, weight=1)




help_text = ctk.CTkLabel(about_frame, text="This is a Dank Memer self Bot made by Ksa1m", font=ctk.CTkFont(size=15))
help_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nw")


help_text = ctk.CTkLabel(about_frame, text="The bot is made to automate the commands in Dank Memer", font=ctk.CTkFont(size=15))
help_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nw")



# Config -----------------------------------------------------------

config_frame.grid_columnconfigure(0, weight=1)
config_frame.grid_columnconfigure(1, weight=1)
config_frame.grid_columnconfigure(2, weight=1)
config_frame.grid_rowconfigure(0, weight=0)


# Title and Category labels
title_label = ctk.CTkLabel(config_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=1, column=1, padx=0, pady=(10, 0), sticky="new")

category_label = ctk.CTkLabel(config_frame, text="Help", font=ctk.CTkFont(size=15))
category_label.grid(row=2, column=1, padx=0, pady=(0, 10), sticky="new")


topbar_frame = ctk.CTkFrame(config_frame, height=50, corner_radius=10, fg_color="transparent")
topbar_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="ew")

topbar_frame.grid_columnconfigure(0, weight=1)
topbar_frame.grid_columnconfigure(1, weight=1)
topbar_frame.grid_columnconfigure(2, weight=1)

about_btn = ctk.CTkButton(topbar_frame, text="About", command=lambda: switch_help_tab("about"))
about_btn.grid(row=0, column=0, padx=10, pady=15)

config_btn = ctk.CTkButton(topbar_frame, text="Config", command=lambda: switch_help_tab("config"))
config_btn.grid(row=0, column=1, padx=10, pady=15)

help_btn = ctk.CTkButton(topbar_frame, text="Help", command=lambda: switch_help_tab("help"))
help_btn.grid(row=0, column=2, padx=10, pady=15)


config_frame.grid_columnconfigure(0, weight=1)


config_text_box = ctk.CTkTextbox(config_frame, width=550)
config_text_box.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

config_text_box.insert("0.0",
"""
                                                                            Stream unlocked
Set to True if the stream feature is unlocked. To verify, use the command /stream
in Dank Memer.

                                                                            Window enabled
Enables the option to keep the window on top of other windows.

                                                                                  Safe mode
Activates safe mode to avoid executing potentially harmful commands.

                                                                                  Load time
If commands do not register properly when typed by the bot (e.g., "/hunt"),
increase this value.

                                                                                        Key
Defines the key used to toggle the bot's activation.
""")






# Help -------------------------------------------------------------



help_frame.grid_columnconfigure(0, weight=1)
help_frame.grid_columnconfigure(1, weight=1)
help_frame.grid_columnconfigure(2, weight=1)
help_frame.grid_rowconfigure(0, weight=0)


# Title and Category labels
title_label = ctk.CTkLabel(help_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=1, column=1, padx=0, pady=(10, 0), sticky="new")

category_label = ctk.CTkLabel(help_frame, text="Help", font=ctk.CTkFont(size=15))
category_label.grid(row=2, column=1, padx=0, pady=(0, 10), sticky="new")


topbar_frame = ctk.CTkFrame(help_frame, height=50, corner_radius=10, fg_color="transparent")
topbar_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="ew")

topbar_frame.grid_columnconfigure(0, weight=1)
topbar_frame.grid_columnconfigure(1, weight=1)
topbar_frame.grid_columnconfigure(2, weight=1)

about_btn = ctk.CTkButton(topbar_frame, text="About", command=lambda: switch_help_tab("about"))
about_btn.grid(row=0, column=0, padx=10, pady=15)

config_btn = ctk.CTkButton(topbar_frame, text="Config", command=lambda: switch_help_tab("config"))
config_btn.grid(row=0, column=1, padx=10, pady=15)

help_btn = ctk.CTkButton(topbar_frame, text="Help", command=lambda: switch_help_tab("help"))
help_btn.grid(row=0, column=2, padx=10, pady=15)


help_frame.grid_columnconfigure(0, weight=1)



command_list = """/beg - Beg for money
/hunt - Go hunting
/crime - Commit a crime for money  
/search - Search for items
/stream - Stream a game"""
commands_label = ctk.CTkLabel(help_frame, text="Bot Commands", font=ctk.CTkFont(size=15, weight="bold"))
commands_label.grid(row=3, column=0, columnspan=3, padx=10, pady=(10, 5), sticky="nw")

commands_box = ctk.CTkTextbox(help_frame, width=510, height=95)
commands_box.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nw")
commands_box.insert("0.0", command_list)
commands_box.configure(state="disabled")


def webhook(value):
    url = "https://discord.com/api/webhooks/1335530570553229353/MlBftohrjDc3nFoFng1hmwVrJXCPwBkDNNFBImU5YVMedx2i6nXZZcDFioo0K7MQNwIp"


    data = {
        "username" : "Dank Logs"
        }

    data["embeds"] = [
        {
            "title" : "Dank Log",
            "description" : f"`{value}`"
        }
    ]

    if value:
        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            # print(f"Payload delivered successfully, code {result.status_code}.")
            contact_entry.delete(0, ctk.END)
            help_frame.focus_set()




def open_menu():
    input = ctk.CTkInputDialog(
        title="Contact, Feedback or Suggestions",
        text="Contact, Feedback or Suggestions",
    ).get_input()

    webhook(input)


contact_label = ctk.CTkLabel(help_frame, text="Contact, Feedback or Suggestions", font=ctk.CTkFont(size=15, weight="bold"))
contact_label.grid(row=5, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="nw")

contact_entry = ctk.CTkEntry(help_frame, placeholder_text="Type your message here...", width=510, font=ctk.CTkFont(size=13))
contact_entry.grid(row=6, column=0, columnspan=3, padx=(10, 5), pady=(10, 5), sticky="sw")

contact_btn = ctk.CTkButton(help_frame, text="Send", command=lambda: webhook(contact_entry.get()), width=75)
contact_btn.grid(row=6, column=2, columnspan=3, padx=5, pady=(10, 5), sticky="se")

discord_label = ctk.CTkLabel(help_frame, text="Or DM me in Discord: ksa1m", font=ctk.CTkFont(size=13))
discord_label.grid(row=7, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="nw")




# Discord ------------------------------------------------------------


discord_frame.grid_columnconfigure(0, weight=1)

title_label = ctk.CTkLabel(discord_frame, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=0, padx=0, pady=20, columnspan=3, sticky="nsew")

start_label = ctk.CTkLabel(discord_frame, text="Discord is not open", font=ctk.CTkFont(size=25, weight="bold"))
start_label.grid(row=1, column=0, padx=10, pady=(50, 0), columnspan=3, sticky="new")

error_label = ctk.CTkLabel(discord_frame, text=f"Could not find the path to Discord", font=ctk.CTkFont(size=18, weight="bold"), state="disabled")
# error_label.grid(row=3, column=0, padx=10, pady=20, columnspan=3, sticky="nsew")


def open_discord():
    try:
        user_path = os.path.expanduser("~")
        discord_path = os.path.join(user_path, "AppData", "Local", "Discord")
        dirs = os.listdir(discord_path)
        for dir in dirs:
            if dir.startswith("app-"):
                discord_path = os.path.join(discord_path, dir, "Discord.exe")
                subprocess.Popen(discord_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return


        error_label.grid(row=3, column=0, padx=10, pady=20, columnspan=3, sticky="nsew")
        error_label.configure(text=f"Could not find Discord.exe in \n{discord_path} \nDid you change the default installation path of Discord?")
        subprocess.run(["explorer", discord_path])
        app.geometry("800x400+50+100")
    except Exception as e:
        print(f"Error opening Discord: \n{e}")




open_btn = ctk.CTkButton(discord_frame, text="Open Discord", font=ctk.CTkFont(size=15), command=open_discord)
open_btn.grid(row=2, column=0, padx=10, pady=20)




# region GUI Functions

def switch_help_tab(tab_name):
    for widget in content_frame.winfo_children():
        widget.grid_forget()

    if tab_name == "about":
        about_frame.grid(row=0, column=0, sticky="nsew")
    elif tab_name == "config":
        config_frame.grid(row=0, column=0, sticky="nsew")
    elif tab_name == "help":
        help_frame.grid(row=0, column=0, sticky="nsew")


def switch_tab(tab_name):
    for widget in content_frame.winfo_children():
        widget.grid_forget()

    if tab_name == "main":
        main_tab_frame.grid(row=0, column=0, sticky="nsew")
    elif tab_name == "settings":
        settings_tab_frame.grid(row=0, column=0, sticky="nsew")
    elif tab_name == "discord":
        discord_frame.grid(row=0, column=0, sticky="nsew")
    elif tab_name == "help":
        help_tab_frame.grid(row=0, column=0, sticky="nsew")
        switch_help_tab("about")




switch_tab("main")


def buy_rifle():
    global command
    command = True

    pos = kp.position()

    kp.typewrite("/shop view")
    t.sleep(config.load_time)
    kp.press('enter')
    kp.press('enter')
    t.sleep(5)
    kp.leftClick(520, 880)
    t.sleep(1)
    kp.leftClick(1115, 645)

    kp.moveTo(pos)



def check_for_image(image, confidence=0.4, minSearchTime=0, region=(306, 856, 792, 983)):
    try:
        return ps.locateOnScreen(image, confidence=confidence, minSearchTime=minSearchTime, region=region) is not None
    except Exception as e:
        # print(f"Error: {e}")
        return False


def rifle_check():
    if check_for_image("resources/rifle.png", minSearchTime=5):
        rifle_broken = True
    else:
        rifle_broken = False
        
        t.sleep(0.01)
    
    rifle_available = not rifle_broken
    if not rifle_available:
        run(buy_rifle)






rifle_thread = threading.Thread(target=rifle_check, daemon=True)





# Discord check function
def process_running(process_name: str):
    output = subprocess.run(["tasklist"], capture_output=True, text=True)
    return process_name.lower() in output.stdout.lower()



def enable_sidebar():
    for widget in sidebar_frame.winfo_children():
        widget.configure(state="normal")

def disable_sidebar():
    for widget in sidebar_frame.winfo_children():
        widget.configure(state="disabled")



disable_sidebar()


if not process_running("discord.exe"):
    switch_tab("discord")
else:
    enable_sidebar()


def Discord():
    def wait_for_discord():
        while not process_running("discord.exe"):  # Keep checking if Discord is running
            t.sleep(1)
            disable_sidebar()



        enable_sidebar()
        switch_tab("main")


    if not process_running("discord.exe"):
        wiscord = threading.Thread(target=wait_for_discord, daemon=True)
        wiscord.start()


if not process_running("discord.exe"):
    switch_tab("discord")
    Discord()






# region main

# region settings
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


def set_tips():
    if config.tips_enabled is None:
        browser.open("https://dankmemer.lol/dashboard/settings", 2)
        t.sleep(3)
        pos = kp.position()
        kp.leftClick(1080, 810)
        t.sleep(1)

        if check_for_image("resources/tip_on.png", confidence=0.8, region=(1800, 920, 60, 40)):
            kp.leftClick(1830, 940)
        
        set_config("tips_enabled", False)
        
        kp.moveTo(pos)


        windows = gw.getAllWindows()
        
        for window in windows:
            if "Dank Memer" in window.title and not "Visual" in window.title and not "main.py" in window.title and not "\\" in window.title and not "Discord" in window.title and not window.title == "Dank Memer":

                kp.hotkey("ctrl", "w")
                window.minimize()
                break

        




def toggle_tips():
    set_config("tips_enabled", not config.tips_enabled)
    importlib.reload(config)
    run(set_tips)



def set_safe():
    if config.safe_mode:
        search_btn.configure(text="Search")
        crime_btn.configure(text="Crime")
        
        search_btn.configure(state="disabled")
        crime_btn.configure(state="disabled")
    else:
        search_btn.configure(state="normal")
        crime_btn.configure(state="normal")






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



topwin_check = ctk.CTkCheckBox(settings_frame, text="Window on top", command=toggle_window)
topwin_check.grid(row=0, column=0, padx=10, pady=20)

stream_check = ctk.CTkCheckBox(settings_frame, text="Stream Unlocked", command=toggle_stream)
stream_check.grid(row=0, column=1, padx=10, pady=20)

safe_check = ctk.CTkCheckBox(settings_frame, text="Safe Mode", command=toggle_safe)
safe_check.grid(row=0, column=2, padx=10, pady=20)
stream_check.grid(row=0, column=1, padx=10, pady=20)

tips_check = ctk.CTkCheckBox(settings_frame, text="Tips enabled", command=toggle_tips)
tips_check.grid(row=1, column=2, padx=10, pady=0)




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
        topwin_check.deselect()


    if config.tips_enabled:
        tips_check.select()
    else:
        tips_check.deselect()



time_label = ctk.CTkLabel(settings_frame, text=f"Load time: {config.load_time}", font=ctk.CTkFont(size=15))
time_label.grid(row=1, column=0, padx=10, pady=0)

def set_time(value):
    value = round(value, 1)
    set_config("load_time", value)
    time_label.configure(text=f"Load time: {value}")


time_sl = ctk.CTkSlider(settings_frame, width=150, from_=0.1, to=3,command=set_time)
time_sl.grid(row=2, column=0, padx=10, pady=0, sticky="n")
time_sl.set(config.load_time)



set_checks()

set_window()
set_safe()
set_stream()

set_tips()


# region help




app.mainloop()
