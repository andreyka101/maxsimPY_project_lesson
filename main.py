from tkinter import *
from player_vs_player import player_vs_player_fun_start
root = Tk()
root.geometry("600x500")
def remove_buttons_player_vs_player():
    player_vs_player_fun_start()
    player_vs_player_button.place(x=-100,y=-100)
    player_vs_PC_button.place(x=-100,y=-100)

player_vs_player_button = Button(text="player_vs_player", command=remove_buttons_player_vs_player)
player_vs_player_button.place(x=0,y=0)

player_vs_PC_button = Button(text="player_vs_PC")
player_vs_PC_button.place(x=0,y=30)

root.mainloop()