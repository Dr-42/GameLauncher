import tkinter as tk
import new_game, remove_game, launchcomm

def open_add_game(win, data, lb):
   new_game.options(win, data, lb) 
   quit_pop()

def open_set_run(win):
    launchcomm.options(win)
    quit_pop()


def open_remove_game(win, data, lb):
    remove_game.options(win, data, lb)
    quit_pop()

def quit_pop():
    pop.destroy()

def options(win, data, lb):
    global pop
    pop = tk.Toplevel(win)
    pop.title("Save Game")

    frpop = tk.Frame(pop)
    p_head = tk.Label(frpop, text="Options")
    p_back = tk.Button(frpop, text="⏎", command=quit_pop)
    p_add_game = tk.Button(frpop, text="Add Game", command=lambda: open_add_game(win, data, lb))
    p_remove_game = tk.Button(frpop, text="Remove Game", command=lambda: open_remove_game(win, data, lb))
    p_run_command = tk.Button(frpop, text="Set run command", command=lambda: open_set_run(win))
    p_head.grid(row=0, column=0)
    p_back.grid(row=0, column=1, sticky="e")
    p_add_game.grid(row=1, column=0, columnspan=2, sticky="ew")
    p_remove_game.grid(row=2, column=0, columnspan=2, sticky="ew")
    p_run_command.grid(row=3, column=0, columnspan=2, sticky="ew")

    frpop.pack()
