import random as rand
import tkinter as tk
from tkinter import *
import tkinter.font as font


def muster():
    i = 1
    for critter in side1_list:
        print(critter1.getvar(attackvar.get()))
        print(str(i))
        i += 1



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
    side2 = tk.Frame(manager, highlightbackgroun="black", highlightthickness=1)
    side2_title = tk.Label(side2, text="Side Two", font=big_font)
    side2_title.grid(row=1, column=1, columnspan=4)
    side1.grid(row=g, column=1)
    side2.grid(row=g, column=3)
    battle_button = tk.Button(text="Battle!", command=muster)
    battle_button.grid(row=g, column=2)
    battle_button["font"] = big_font

    str_def = ["0", "1", "2", "3", "4", "5"]
    critter_number = 10


    side1_list =[]
    slot = 1
    i = 3
    while i != critter_number:
        critter1 = tk.Frame(side1)

        if i == 3:
            side_back = tk.Frame(critter1, bg="grey")
            side_info1 = tk.Label(critter1, text="#", bg="grey")
            side_info2 = tk.Label(critter1, text="Name", bg="grey")
            side_info3 = tk.Label(critter1, text="STR", bg="grey")
            side_info4 = tk.Label(critter1, text="DEF", bg="grey")
            side_back.grid(row=2, column=1, columnspan=4, sticky="nsew")
            side_info1.grid(row=2, column=1)
            side_info2.grid(row=2, column=2)
            side_info3.grid(row=2, column=3)
            side_info4.grid(row=2, column=4)

        c1_number = tk.Entry(critter1, width=6)
        c1_name = tk.Entry(critter1, width=30)
        attackvar = StringVar(critter1)
        attackvar.set("0")
        defensevar = StringVar(critter1)
        defensevar.set("0")
        c_atk1 = tk.OptionMenu(critter1, attackvar, *str_def)
        c_def1 = tk.OptionMenu(critter1, defensevar, *str_def)

        critters = IntVar(critter1)
        critters.set(0)
        name = StringVar(critter1)
        name.set("")

        side1_list.append(critter1)

        critter1.grid(row=i, column=slot, padx=10)
        c1_number.grid(row=i, column=slot)
        c1_name.grid(row=i, column=slot + 1)
        c_atk1.grid(row=i, column = slot + 2, sticky= "nsew")
        c_def1.grid(row=i, column=slot + 3, sticky= "nsew")
        i += 1

    slot = 1
    i = 3
    while i != critter_number:
        critter2 = tk.Frame(side2)

        if i == 3:
            side_back = tk.Frame(critter2, bg="grey")
            side_info1 = tk.Label(critter2, text="#", bg="grey")
            side_info2 = tk.Label(critter2, text="Name", bg="grey")
            side_info3 = tk.Label(critter2, text="STR", bg="grey")
            side_info4 = tk.Label(critter2, text="DEF", bg="grey")
            side_back.grid(row=2, column=1, columnspan=4, sticky="nsew")
            side_info1.grid(row=2, column=1)
            side_info2.grid(row=2, column=2)
            side_info3.grid(row=2, column=3)
            side_info4.grid(row=2, column=4)

        c1_number = tk.Entry(critter2, width=6)
        c1_name = tk.Entry(critter2, width=30)
        attackvar1 = StringVar(manager)
        attackvar1.set("0")
        defensevar1 = StringVar(manager)
        defensevar1.set("0")
        c_atk1 = tk.OptionMenu(critter2, attackvar1, *str_def)
        c_def1 = tk.OptionMenu(critter2, defensevar1, *str_def)
        critter2.grid(row=i, column=slot, padx=10)
        c1_number.grid(row=i, column=slot)
        c1_name.grid(row=i, column=slot + 1)
        c_atk1.grid(row=i, column = slot + 2, sticky= "nsew")
        c_def1.grid(row=i, column=slot + 3, sticky= "nsew")
        i += 1






    manager.mainloop()