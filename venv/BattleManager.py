import random as rand
import tkinter as tk
from tkinter import *
import tkinter.font as font





if __name__ == "__main__":

    manager = tk.Tk()

    # all the fonts in descending order
    biggest_font = font.Font(root=manager, family="Arial", size=16, weight="bold")
    big_font = font.Font(root=manager, family="Arial", size=14)
    f = font.Font(root=manager, family="Arial", size=14)

    g = 1
    main_text = tk.Label(text="Swords and Sorcery Battle Simulator", font=biggest_font)
    main_text.grid(row=1, column=1, columnspan=6, ipadx=10, ipady=10)
    g += 1
    side1 = tk.Frame(manager, highlightbackgroun="black", highlightthickness=1)
    side1_title = tk.Label(side1, text="Side One", font=big_font)
    side1_title.grid(row=1, column=1, columnspan=4)
    side1_info = tk.Label(side1, text="    #                 Name                          STR         DEF   ", bg="grey")
    side1_title.grid(row=1, column=1, columnspan=4)
    side1_info.grid(row=2, column=1, columnspan=5)
    side2 = tk.Frame(manager, highlightbackgroun="black", highlightthickness=1)
    side2_title = tk.Label(side2, text="Side Two", font=big_font)
    side2_info = tk.Label(side2, text="    #                 Name                          STR         DEF   ", bg="grey")
    side2_title.grid(row=1, column=1, columnspan=4)
    side2_info.grid(row=2, column=1, columnspan=5)
    side1.grid(row=g, column=1)
    side2.grid(row=g, column=3)
    battle_button = tk.Button(text="Battle!")
    battle_button.grid(row=g, column=2)
    battle_button["font"] = big_font

    str_def = ["0", "1", "2", "3", "4", "5"]
    critter_number = 10



    slot = 1
    i = 3
    while i != critter_number:
        critter1 = tk.Frame(side1)
        c1_number = tk.Entry(critter1, width=6)
        c1_name = tk.Entry(critter1, width=30)
        attackvar1 = StringVar(manager)
        attackvar1.set("0")
        defensevar1 = StringVar(manager)
        defensevar1.set("0")
        c_atk1 = tk.OptionMenu(critter1, attackvar1, *str_def)
        c_def1 = tk.OptionMenu(critter1, defensevar1, *str_def)
        critter1.grid(row=i, column=slot)
        c1_number.grid(row=i, column=slot)
        c1_name.grid(row=i, column=slot + 1)
        c_atk1.grid(row=i, column = slot + 2, sticky= "nsew")
        c_def1.grid(row=i, column=slot + 3, sticky= "nsew")
        i += 1

    slot = 1
    i = 3
    while i != critter_number:
        critter1 = tk.Frame(side2)
        c1_number = tk.Entry(critter1, width=6)
        c1_name = tk.Entry(critter1, width=30)
        attackvar1 = StringVar(manager)
        attackvar1.set("0")
        defensevar1 = StringVar(manager)
        defensevar1.set("0")
        c_atk1 = tk.OptionMenu(critter1, attackvar1, *str_def)
        c_def1 = tk.OptionMenu(critter1, defensevar1, *str_def)
        critter1.grid(row=i, column=slot)
        c1_number.grid(row=i, column=slot)
        c1_name.grid(row=i, column=slot + 1)
        c_atk1.grid(row=i, column = slot + 2, sticky= "nsew")
        c_def1.grid(row=i, column=slot + 3, sticky= "nsew")
        i += 1






    manager.mainloop()