import pyautogui as kp
import time as t
import customtkinter as ctk
import threading
import keyboard as kb



postmemes_delay = 30  # click
search_delay = 25  # click
crime_delay = 40
beg_delay = 3  # 40
hunt_delay = 9 # 20



timer = 300
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






app = ctk.CTk()
app.title("Dank Memer Bot")
app.geometry("525x300+700+100")
app.attributes("-topmost", True)

title_label = ctk.CTkLabel(app, text="Dank Memer Bot", font=ctk.CTkFont(size=20, weight="bold"))
title_label.grid(row=0, column=1, padx=0, pady=10)



def Toggle():
    global running
    running = not running
    # print(f"Running: {running}")
    start_btn.configure(text="Start")

    if running:
        timer_start()
        start_thread()

def start():
    start_btn.configure(text="Running")
    while running:
        if kb.is_pressed('f7'):
            print("Toggling...")
            Toggle()

        
        if timer % beg_delay == 0:
            beg()
        
        t.sleep(1)




running_text = "Running"

def update():
    global running, running_text, timer
    

    if running:
        # Running
        if "..." in running_text:
            running_text = "Running"

        start_btn.configure(text=running_text)

        running_text += "."


        # Begging

        begging_text = ""
        begging_left = 10
        remainder = timer % beg_delay
        if remainder == 0:
            begging_left = 3
        else:
            begging_left = 3 - remainder
        
        begging_text = f"Beg: {begging_left}"
        
        beg_btn.configure(text=begging_text)

        # Hunting

        hunting_text = ""
        hunting_left = 10
        remainder = timer % beg_delay
        if remainder == 0:
            hunting_left = 3
        else:
            hunting_left = 3 - remainder
        
        hunting_text = f"Beg: {hunting_left}"
        
        hunt_btn.configure(text=hunting_text)





def beg():
    print("begging")
    # kp.typewrite("pls beg")
    # kp.press('enter')

def hunt():
    print("hunting")
    # kp.typewrite("pls hunt")
    # kp.press('enter')




def start_thread():
    bot_thread = threading.Thread(target=start, daemon=True)
    bot_thread.start()



start_btn = ctk.CTkButton(app, text="Start", command=Toggle)
start_btn.grid(row=1, column=1, padx=20, pady=20)

beg_btn = ctk.CTkButton(app, text="Beg", command=beg)
beg_btn.grid(row=2, column=0, padx=20, pady=20)

hunt_btn = ctk.CTkButton(app, text="Hunt", command=hunt)
hunt_btn.grid(row=2, column=1, padx=20, pady=20)


app.mainloop()
