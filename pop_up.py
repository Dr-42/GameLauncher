import tkinter as tk
from tkinter import ttk
import new_game

def open_add_game(win, data, lb):
   new_game.options(win, data, lb) 
   quit_pop()

def open_remove_game():
    pass

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
    p_remove_game = tk.Button(frpop, text="Remove Game", command=open_remove_game)
    p_head.grid(row=0, column=0)
    p_back.grid(row=0, column=1, sticky="e")
    p_add_game.grid(row=1, column=0, columnspan=2, sticky="ew")
    p_remove_game.grid(row=2, column=0, columnspan=2, sticky="ew")

    frpop.pack()
