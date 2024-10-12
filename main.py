from tkinter import *
from player_vs_player import player_vs_player_fun_start
root = Tk()
root.geometry("600x500")
def remove_buttons_player_vs_player():
    player_vs_player_fun_start()
    player_vs_player_button.place(x=-100,y=-100)
    player_vs_PC_button.place(x=-100,y=-100)
def remove_buttons_player_vs_PC():
    # player_vs_player_fun_start()
    player_vs_player_button.place(x=-100,y=-100)
    player_vs_PC_button.place(x=-100,y=-100)

player_vs_player_button = Button(text="player_vs_player", command=remove_buttons_player_vs_player)
player_vs_player_button.place(x=0,y=0)

player_vs_PC_button = Button(text="player_vs_PC", command=remove_buttons_player_vs_PC)
player_vs_PC_button.place(x=0,y=30)




text_lab = Label(text="None",font=("Arial", 14))
text_lab.place(x=200 , y =50)
# https://haxor.no/en/article/tkinter-events
def fun_games(event):
    button_id = event.widget
    # text_lab.config(text=button_id)
    if(button_id["text"] == " "):
        button_id.config(text= "x")
    


dist_button_games = {}
for x_index in range (1,4):
    print(x_index)
    for y_index in range (1,4):
        dist_button_games[f'button_X{x_index}_Y{y_index}'] = Button(text=" ", bg="#fcb678" )
        dist_button_games[f'button_X{x_index}_Y{y_index}'].place(x=140 + (60 * x_index),y=100 + (60 * y_index) , width=50, height=50)
        dist_button_games[f'button_X{x_index}_Y{y_index}'].bind("<Button-1>" , fun_games)


print(dist_button_games)

root.mainloop()