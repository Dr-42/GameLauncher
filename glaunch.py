# Simple gui for launching games using shell commands
import tkinter as tk
import os
from tkinter import ttk, filedialog
import json

# Handle cleanup
def on_closing():
    win.destroy()
    win.quit()

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
    global imgN
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

def open_game_dir(dir_field):
    dir_path_string = filedialog.askdirectory()
    dir_field.delete('1.0', tk.END)
    dir_field.insert('1.0', dir_path_string)

def open_game_exe(exe_field):
    file_path_string = filedialog.askopenfilename()
    exe_field.delete('1.0', tk.END)
    exe_field.insert('1.0', file_path_string)

def save_game():
    pass

def quit_pop():
    pop.destroy()
    pass

def options():
    global pop
    pop = tk.Toplevel(win)
    pop.title("Save Game")

    frpop = tk.Frame(pop)
    p_name = tk.Label(frpop, text="Name: ")
    p_dir = tk.Label(frpop, text="Dir: ")
    p_exe = tk.Label(frpop, text="Exe: ")
    p_namefield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")
    p_dirfield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")
    p_exefield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")
    p_dirButton = tk.Button(frpop, text="🗀 ", command=lambda: open_game_dir(p_dirfield))
    p_exeButton = tk.Button(frpop, text="🗀 ", command=lambda: open_game_exe(p_exefield))
    p_saveButton = tk.Button(frpop, text="Save", command=save_game)
    p_quitButton = tk.Button(frpop, text="Quit", command=quit_pop)

    p_name.grid(row=0, column=0)
    p_namefield.grid(row=0, column=1, columnspan=2)
    p_dir.grid(row=1, column=0)
    p_dirfield.grid(row=1, column=1, columnspan=2)
    p_dirButton.grid(row=1, column=3)
    p_exe.grid(row=2, column=0)
    p_exefield.grid(row=2, column=1, columnspan=2)
    p_exeButton.grid(row=2, column=3)
    p_saveButton.grid(row=3, column=1)
    p_quitButton.grid(row=3, column=2)

    frpop.pack()


def create_ui():
    global win, root, img, lb, imgBox
    #Create the UI
    win = tk.Tk()
    win.title("Game Launcher")
    root = tk.Frame(win)

    head = tk.Label(root, text="Library")
    opt = tk.Button(root, text= "≡", command=options)
    head.grid(row=0, column=0, columnspan=2, sticky='w')
    opt.grid(row=0, column=2, sticky="e")

    lb = tk.Listbox(root, selectmode=tk.SINGLE, height=9)
    for game in data:
        lb.insert(tk.END, game)

    lb.bind('<<ListboxSelect>>', onselect)
    lb.grid(row= 1, column= 0, columnspan=3)

    strt = tk.Button(root, text= "Launch", command=launch_game)
    win.protocol("WM_DELETE_WINDOW", on_closing)
    qut = tk.Button(root, text= "Quit", command=on_closing)
    strt.grid(row=2, column=0, columnspan=2, sticky="ew")
    qut.grid(row=2, column=2, sticky="ew")

    img = tk.PhotoImage(file = "/run/media/spandan/Projects/Python/GameLauncher/images/hollow_knight.png")
    imgBox = tk.Label(root, image=img)
    imgBox.grid(row=0, column=3, rowspan=3, sticky="ewns")

    root.pack(expand=True)

def load_data():
    global data
    dat = open("/run/media/spandan/Projects/Python/GameLauncher/data.json", "r").read()
    data = json.loads(dat)
 
if __name__ == "__main__":
    load_data()
    create_ui()
    keyboard_controls()
    # Start the main loop
    root.mainloop()
