import tkinter as tk
import os

def set_run_command(name_field):
    file = open(os.path.expanduser('~') + "/.glaunch/.runcmd", "w")
    file.write(name_field.get("1.0", tk.END)[:-1])
    quit_pop

def quit_pop():
    pop.destroy()

def options(win):
    global pop
    pop = tk.Toplevel(win)
    pop.title("Save Game")

    frpop = tk.Frame(pop)
    p_head = tk.Label(frpop, text="Set Run Command")
    p_back = tk.Button(frpop, text="⏎", command=quit_pop)

    p_name = tk.Label(frpop, text="Run command")
    p_namefield = tk.Text(frpop, height=1, width=31, wrap="none", background="#7d807e", foreground="#000000")

    p_saveButton = tk.Button(frpop, text="Save", command=lambda: set_run_command(p_namefield))

    p_head.grid(row=0, column=0)
    p_back.grid(row=0, column=3, sticky="e")
    p_name.grid(row=1, column=0)
    p_namefield.grid(row=1, column=1, columnspan=2)
    p_saveButton.grid(row=6, column=0, columnspan=4)
    frpop.pack()
