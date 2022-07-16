#!/usr/bin/python3
# Simple gui for launching games using shell commands
import tkinter as tk
import os
from tkinter import ttk, filedialog
import json
from PIL import Image, ImageTk
import pop_up

# Handle cleanup
def on_closing():
    win.destroy()
    win.quit()

def load_data():
    global data
    root_dir = os.path.expanduser('~') + "/.glaunch/"
    if not os.path.isdir(root_dir):
        os.system("mkdir " + root_dir)
    if not os.path.isfile(root_dir + "data.json"):
        data = {}
    else:
        dat = open(root_dir + "data.json", "r").read()
        data = json.loads(dat)

    if not os.path.isfile(root_dir + ".runcmd"):
        print("No runcmd file")
        file = open(root_dir + ".runcmd", "w")
        file.write("wine")

        

# Create a button to launch the selected game
def launch_game():
    game = lb.get(lb.curselection())
    if(data[game][3] == "[Linux Native]"):
        game_path = data[game][0]
        print(game_path)
        os.chdir(game_path)
        command = "exec " + '\"' + data[game][1] + '\"'
    else:
        game_path = data[game][0]
        game_exe =  " \"" + data[game][1] + "\""
        wineprefix = "WINEPREFIX=" + data[game][3]

        os.chdir(game_path)

        run_cmd = " " + open(os.path.expanduser('~') + "/.glaunch/.runcmd", "r").read()
        command = wineprefix + run_cmd + game_exe

    print(command)
    # Launch the game
    os.system(command)

def get_image(key):
    global imgN
    imgPath = data[key][2] 
    imgN = Image.open(imgPath)
    aspect = imgN.width/imgN.height
    imgN.thumbnail((int(316 * aspect), 316), Image.Resampling.LANCZOS)
    imgNtk = ImageTk.PhotoImage(imgN)
    imgBox.configure(image=imgNtk)
    imgBox.image = imgNtk

def onselect(evt):
    w = evt.widget
    if w.curselection() != ():
        index = int(w.curselection()[0])
        value = w.get(index)
        get_image(value)

def create_ui():
    global win, root, lb, imgBox
    #Create the UI
    win = tk.Tk()
    win.title("Game Launcher")
    root = tk.Frame(win)

    head = tk.Label(root, text="Library")
    opt = tk.Button(root, text= "≡", command=lambda: pop_up.options(win, data, lb))
    head.grid(row=0, column=0, columnspan=2, sticky='w')
    opt.grid(row=0, column=2, sticky="e")

    imgBox = tk.Label(root)
    imgBox.grid(row=0, column=3, rowspan=3, sticky="ewns")

    lb = tk.Listbox(root, selectmode=tk.SINGLE, height=9)
    for game in data:
        lb.insert(tk.END, game)

    lb.bind('<<ListboxSelect>>', onselect)
    lb.select_set(0)
    lb.event_generate("<<ListboxSelect>>")
    lb.grid(row= 1, column= 0, columnspan=3)

    strt = tk.Button(root, text= "Launch", command=launch_game)
    win.protocol("WM_DELETE_WINDOW", on_closing)
    qut = tk.Button(root, text= "Quit", command=on_closing)
    strt.grid(row=2, column=0, columnspan=2, sticky="ew")
    qut.grid(row=2, column=2, sticky="ew")

    root.pack(expand=True)
 
if __name__ == "__main__":
    load_data()
    create_ui()
    # Start the main loop
    root.mainloop()
