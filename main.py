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
    text_lab.config(bg="#eeff61")
def remove_buttons_player_vs_PC():
    # player_vs_player_fun_start()
    player_vs_player_button.place(x=-100,y=-100)
    player_vs_PC_button.place(x=-100,y=-100)
    render_button_games()
    text_lab.place(x=200 , y =50)
    root.config(bg="#eeff61")
    text_lab.config(bg="#eeff61")

player_vs_player_button = Button(text="player_vs_player", command=remove_buttons_player_vs_player)
player_vs_player_button.place(x=0,y=0)

player_vs_PC_button = Button(text="player_vs_PC", command=remove_buttons_player_vs_PC)
player_vs_PC_button.place(x=0,y=30)





def restart_fun():
    game_restart_button.place(x=-111,y=-111)
    global move_symbol
    move_symbol = True
    text_lab.config(text="ходит игрок X")
    root.config(bg="#eeff61")
    text_lab.config(bg="#eeff61")
    for x in range(1,4):
        for y in range(1,4):
            dist_button_games[f'button_X{x}_Y{y}'].config(text = " " , bg= "#fcb678")




move_symbol = True
text_lab = Label(text="ходит игрок X",font=("Arial", 14))
game_restart_button = Button(text="restart", command=restart_fun) 
# https://haxor.no/en/article/tkinter-events
def fun_games(event):
    global move_symbol
    button_id = event.widget
    dist_answer = player_vs_player_fun_game(dist_button_games)
    if(button_id["text"] == " " and (not dist_answer["end"])):
        move_symbol
        if(move_symbol):
            move_symbol = False
            button_id.config(text= "x")
            root.config(bg="#37b9fb")
            text_lab.config(bg="#37b9fb")
            text_lab.config(text="ходит игрок O")
        else:
            move_symbol = True
            button_id.config(text= "o")
            root.config(bg="#eeff61")
            text_lab.config(bg="#eeff61")
            text_lab.config(text="ходит игрок X")
        dist_answer = player_vs_player_fun_game(dist_button_games)
            
        if(dist_answer["end"]):
            text_lab.config(text="победил игрок " + dist_answer["symbol"].title())
            game_restart_button.place(x = 260 , y = 400)


dist_button_games = {}
def render_button_games():
    for x_index in range (1,4):
        for y_index in range (1,4):
            dist_button_games[f'button_X{x_index}_Y{y_index}'] = Button(text=" ", bg="#fcb678" , font=("Arial", 25))
            dist_button_games[f'button_X{x_index}_Y{y_index}'].place(x=140 + (60 * x_index),y=100 + (60 * y_index) , width=50, height=50)
            dist_button_games[f'button_X{x_index}_Y{y_index}'].bind("<Button-1>" , fun_games)


print(dist_button_games)

root.mainloop()