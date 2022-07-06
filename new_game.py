import tkinter as tk
import json
from tkinter import ttk, filedialog

def open_wineprefix(dir_field):
    dir_path_string = filedialog.askdirectory(initialdir= "/home/spandan/")
    dir_field.delete('1.0', tk.END)
    dir_field.insert('1.0', dir_path_string)

def open_game_dir(dir_field):
    dir_path_string = filedialog.askdirectory(initialdir= "/home/spandan/.wine/drive_c")
    dir_field.delete('1.0', tk.END)
    dir_field.insert('1.0', dir_path_string)

def open_game_exe(exe_field):
    file_path_string = filedialog.askopenfilename(initialdir= "/home/spandan/.wine/drive_c", filetypes=[('EXE', '*.exe')])
    exe_field.delete('1.0', tk.END)
    exe_field.insert('1.0', file_path_string)

def open_game_image(img_field):
    file_path_string = filedialog.askopenfilename(initialdir= "/run/media/spandan/Projects/Python/GameLauncher/images", filetypes=[('PNG', '*.png')])
    img_field.delete('1.0', tk.END)
    img_field.insert('1.0', file_path_string)

def quit_pop():
    pop.destroy()

def save_game(data, lb, name_field, dir_field, exe_field, img_field, wineprefix_field):
    name = name_field.get("1.0", tk.END)[:-1] 
    direc = dir_field.get("1.0", tk.END)[:-1] 
    exe = exe_field.get("1.0", tk.END)[:-1] 
    img = img_field.get("1.0", tk.END)[:-1] 
    wineprefix = wineprefix_field.get("1.0", tk.END)[:-1]

    data[name] = (direc, exe, img, wineprefix)
    lb.delete(0, tk.END)
    for game in data:
        lb.insert(tk.END, game)

    with open("/run/media/spandan/Projects/Python/GameLauncher/data.json", 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',',': '))

    quit_pop()


def options(win, data, lb):
    global pop
    pop = tk.Toplevel(win)
    pop.title("Save Game")

    frpop = tk.Frame(pop)
    p_head = tk.Label(frpop, text="Add Game")
    p_back = tk.Button(frpop, text="⏎", command=quit_pop)

    p_name = tk.Label(frpop, text="Name: ")
    p_dir = tk.Label(frpop, text="Dir: ")
    p_exe = tk.Label(frpop, text="Exe: ")
    p_img = tk.Label(frpop, text="Image: ")
    p_wineprefix = tk.Label(frpop, text="Wineprefix: ")

    p_namefield = tk.Text(frpop, height=1, width=31, wrap="none", background="#7d807e", foreground="#000000")
    p_dirfield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")
    p_exefield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")
    p_imgfield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")
    p_wineprefixfield = tk.Text(frpop, height=1, width=25, wrap="none", background="#7d807e", foreground="#000000")

    p_dirButton = tk.Button(frpop, text="🗀 ", command=lambda: open_game_dir(p_dirfield))
    p_exeButton = tk.Button(frpop, text="🗀 ", command=lambda: open_game_exe(p_exefield))
    p_imgButton = tk.Button(frpop, text="🗀 ", command=lambda: open_game_image(p_imgfield))
    p_wineprefixButton = tk.Button(frpop, text="🗀 ", command=lambda: open_wineprefix(p_wineprefixfield))
    p_saveButton = tk.Button(frpop, text="Save", command=lambda: save_game(data, lb, p_namefield, p_dirfield, p_exefield, p_imgfield, p_wineprefixfield))

    p_head.grid(row=0, column=0)
    p_back.grid(row=0, column=3, sticky="e")
    p_name.grid(row=1, column=0)
    p_namefield.grid(row=1, column=1, columnspan=3)
    p_dir.grid(row=2, column=0)
    p_dirfield.grid(row=2, column=1, columnspan=2)
    p_dirButton.grid(row=2, column=3)
    p_exe.grid(row=3, column=0)
    p_exefield.grid(row=3, column=1, columnspan=2)
    p_exeButton.grid(row=3, column=3)
    p_wineprefix.grid(row=4, column=0)
    p_wineprefixfield.grid(row=4, column=1, columnspan=2)
    p_wineprefixButton.grid(row=4, column=3)
    p_saveButton.grid(row=5, column=0, columnspan=4)
    p_img.grid(row=4, column=0)
    p_imgfield.grid(row=4, column=1, columnspan=2)
    p_imgButton.grid(row=4, column=3)
    p_saveButton.grid(row=5, column=0, columnspan=4)

    frpop.pack()


