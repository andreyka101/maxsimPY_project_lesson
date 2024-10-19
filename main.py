from tkinter import *
from player_vs_player import player_vs_player_fun_game
root = Tk()
root.geometry("600x500")
def remove_buttons_player_vs_player():
    player_vs_player_button.place(x=-100,y=-100)
    player_vs_PC_button.place(x=-100,y=-100)
    render_button_games()
    text_lab.place(x=200 , y =50)
    root.config(bg="#eeff61")
def remove_buttons_player_vs_PC():
    # player_vs_player_fun_start()
    player_vs_player_button.place(x=-100,y=-100)
    player_vs_PC_button.place(x=-100,y=-100)
    render_button_games()
    text_lab.place(x=200 , y =50)
    root.config(bg="#eeff61")

player_vs_player_button = Button(text="player_vs_player", command=remove_buttons_player_vs_player)
player_vs_player_button.place(x=0,y=0)

player_vs_PC_button = Button(text="player_vs_PC", command=remove_buttons_player_vs_PC)
player_vs_PC_button.place(x=0,y=30)




text_lab = Label(text="None",font=("Arial", 14))
# https://haxor.no/en/article/tkinter-events
move_symbol = True
def fun_games(event):
    global move_symbol
    button_id = event.widget
    if(button_id["text"] == " "):
        move_symbol
        if(move_symbol):
            move_symbol = False
            button_id.config(text= "x")
            root.config(bg="#37b9fb")
        else:
            move_symbol = True
            button_id.config(text= "o")
            root.config(bg="#eeff61")
            
        list_answer = player_vs_player_fun_game(dist_button_games)
        text_lab.config(text=list_answer[0])
        if(list_answer[1] == "ok"):
            dist_button_games.clear()
    


dist_button_games = {}
def render_button_games():
    for x_index in range (1,4):
        for y_index in range (1,4):
            dist_button_games[f'button_X{x_index}_Y{y_index}'] = Button(text=" ", bg="#fcb678" , font=("Arial", 25))
            dist_button_games[f'button_X{x_index}_Y{y_index}'].place(x=140 + (60 * x_index),y=100 + (60 * y_index) , width=50, height=50)
            dist_button_games[f'button_X{x_index}_Y{y_index}'].bind("<Button-1>" , fun_games)


print(dist_button_games)

root.mainloop()