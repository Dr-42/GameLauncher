# Simple gui for launching games using shell commands
import tkinter as tk
import os
from tkinter import ttk

# Create a window
root = tk.Tk()
root.title("Game Launcher")

# Dictionary of games with their paths
games = {
        "Hollow Knight": ("/home/spandan/.wine/drive_c/Hollow Knight", "hollow_knight.exe", "hollow_knight.png"),
        "Dead Cells": ("/home/spandan/.wine/drive_c/Dead Cells/" , "deadcells.exe", "dead_cells.png"),
        "Cuphead": ("/home/spandan/.wine/drive_c/Cuphead The Delicious Last Course/", "Cuphead.exe", "cuphead.png"),
        "Outer Wilds": ("/home/spandan/.wine/drive_c/Outer Wilds" , "OuterWilds.exe", "outer_wilds.png"),
        "Road Redemption": ("/home/spandan/.wine/drive_c/Road Redemption" , "RoadRedemption.exe", "road_redemption.png"),
        "Dark Souls": ("/home/spandan/.wine/drive_c/Dark Souls" , "DARKSOULS.exe", "dark_souls.png"),
        "Celeste": ("/home/spandan/.wine/drive_c/Celeste/Celeste.v1.4.0.0/", "Celeste.exe", "celeste.png")
        }


# Handle cleanup
def on_closing():
    root.destroy()
    root.quit()

# Create a button to launch the selected game
def launch_game():
    game = lb.get(lb.curselection())
    game_path = games[game][0]
    game_exe = games[game][1]
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
    imgPath = "/run/media/spandan/Projects/Python/GameLauncher/images/" + games[key][2]
    imgN = tk.PhotoImage(file=imgPath)
    imgBox.configure(image=imgN)
    imgBox.image = imgN

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    get_image(value)

if __name__ == "__main__":
    img = tk.PhotoImage(file = "/run/media/spandan/Projects/Python/GameLauncher/images/hollow_knight.png")
    lb = tk.Listbox(root, selectmode=tk.SINGLE)
    for game in games:
        lb.insert(tk.END, game)

    lb.bind('<<ListboxSelect>>', onselect)
    lb.grid(row= 0, column= 0, columnspan=2)

    strt = tk.Button(root, text= "Launch", command=launch_game)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    qut = tk.Button(root, text= "Quit", command=on_closing)
    strt.grid(row=1, column=0)
    qut.grid(row=1, column=1)

    imgBox = tk.Label(root, image=img)
    imgBox.grid(row=0, column=2, rowspan=2)

    keyboard_controls()
    # Start the main loop
    root.mainloop()
    root.destroy()
    root.quit()


