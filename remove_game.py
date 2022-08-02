import tkinter as tk
import os
import json

def delete_game(data, lb):
    del data[game_name]
    lb.delete(0, tk.END)
    for game in data:
        lb.insert(tk.END, game)

    with open(os.path.expanduser('~') + "/.glaunch/data.json", "w") as json_file:
        json.dump(data, json_file, indent=4, separators=(',',': '))

    quit_pop()

def quit_pop():
    pop.destroy()

def get_game_name(choice):
    global game_name
    game_name = choice 

def options(win, data, lb):
    global pop
    pop = tk.Toplevel(win)
    pop.title("Remove Game")

    frpop = tk.Frame(pop)
    p_head = tk.Label(frpop, text="Remove Game")
    p_back = tk.Button(frpop, text="⏎", command=quit_pop)

    menu = tk.StringVar()
    menu.set("Select Game")
    drop = tk.OptionMenu(frpop, menu, *data.keys(), command=get_game_name)
    del_button = tk.Button(frpop, text="Delete Game", command=lambda: delete_game(data, lb))

    p_head.grid(row=0, column=0, sticky="w")
    p_back.grid(row=0, column=1, sticky="e")
    drop.grid(row=1, column=0, columnspan=2)
    del_button.grid(row=2, column=0, columnspan=2)

    frpop.pack()
