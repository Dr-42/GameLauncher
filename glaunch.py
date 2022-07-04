# Simple gui for launching games using shell commands
import tkinter as tk
import os
from tkinter import ttk
import json

# Handle cleanup
def on_closing():
    win.destroy()
    win.quit()

def on_pop_close():
    pop.destroy()

# Create a button to launch the selected game
def launch_game():
    game = lb.get(lb.curselection())
    game_path = data[game][0]
    game_exe = data[game][1]
    os.chdir(game_path)

    if(game_exe == "hollow_knight.exe"):
        wineprefix = "WINEPREFIX=/home/spandan/HK"
    else:
        wineprefix = "WINEPREFIX=/home/spandan/GZN"

    command = wineprefix + " prime-run wine " + game_exe
    print(command)
    # Launch the game
    os.system(command)

def keyboard_controls():
    root.bind('<Up>', lambda event: lb.yview_scroll(-1, 'units'))
    root.bind('<Down>', lambda event: lb.yview_scroll(1, 'units'))
    # Space key selects the game under cursor
    root.bind('<space>', lambda event: lb.selection_set(lb.curselection()))
    root.bind('<Return>', lambda event: launch_game())
    root.bind('<Escape>', lambda event: on_closing())

def get_image(key):
    imgPath = "/run/media/spandan/Projects/Python/GameLauncher/images/" + data[key][2]
    imgN = tk.PhotoImage(file=imgPath)
    imgBox.configure(image=imgN)
    imgBox.image = imgN

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    get_image(value)

def options():
    global pop
    pop = tk.Toplevel(win)
    pop.title("glaunch.pyConfirmation")
    pop.geometry("300x150")

    frpop = tk.Frame(pop)
    butn = tk.Button(frpop, text="Close", command=on_pop_close)
    butn.grid(row=0, column=0)
    frpop.pack()


if __name__ == "__main__":

    dat = open("/run/media/spandan/Projects/Python/GameLauncher/data.json", "r").read()
    data = json.loads(dat)


    #Create the UI
    win = tk.Tk()
    win.title("Game Launcher")
    root = tk.Frame(win)

    img = tk.PhotoImage(file = "/run/media/spandan/Projects/Python/GameLauncher/images/hollow_knight.png")
    head = tk.Label(root, text="Library")
    opt = tk.Button(root, text= "≡", command=options)
    head.grid(row=0, column=0, columnspan=2, sticky='w')
    opt.grid(row=0, column=2, sticky="e")

    lb = tk.Listbox(root, selectmode=tk.SINGLE)
    for game in data:
        lb.insert(tk.END, game)

    lb.bind('<<ListboxSelect>>', onselect)
    lb.grid(row= 1, column= 0, columnspan=3)

    strt = tk.Button(root, text= "Launch", command=launch_game)
    win.protocol("WM_DELETE_WINDOW", on_closing)
    qut = tk.Button(root, text= "Quit", command=on_closing)
    strt.grid(row=2, column=0, columnspan=2, sticky="ew")
    qut.grid(row=2, column=2, sticky="ew")

    imgBox = tk.Label(root, image=img)
    imgBox.grid(row=0, column=4, rowspan=2)

    root.pack(expand=True)

    keyboard_controls()
    # Start the main loop
    root.mainloop()
    root.destroy()
    root.quit()


