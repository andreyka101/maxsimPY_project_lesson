import threading
import time 
from tkinter import *
import random

root = Tk()
root.geometry('600x500')

canV = Canvas(width=600, height=500, bg='white')
canV.pack()

points1=0
points2=0
turn1=True
numbers_of_pair= []
old_numbers_of_pair= [0,0]




def game(cards_arr):
    images_list = ["green", "green","blue","blue", "yellow","yellow", "red","red", "pink","pink", "orange","orange"]
    images_list_left = ["green", "green","blue","blue", "yellow","yellow", "red","red", "pink","pink", "orange","orange"]
#     images_list = ['blue', 'blue','blue','blue','blue','blue','red','red','red','red','red','red',]
#     images_list_left = ['blue', 'blue','blue','blue','blue','blue','red','red','red','red','red','red',]
    images_list_left = images_list
    for i in range(len(cards_arr)):
        canV.create_rectangle(cards_arr[i]["card_x"], cards_arr[i]["card_y"], cards_arr[i]["card_x"]+50, cards_arr[i]["card_y"]+50, fill="black")
        if len(images_list_left) == 0:
            random_color = 0
        else:
             random_color = random.randint(0, len(images_list_left)-1)
        cards_arr[i]["filling"] = images_list_left[random_color]
        images_list_left.pop(random_color)
        print(images_list_left)
        print(cards_arr)
cards_arr = [ {"card_x" :150, "card_y" : 150, "filling":None, "opened": False},  {"card_x" :150, "card_y" : 210, "filling":None, "opened": False}, {"card_x" :150, "card_y" : 270, "filling":None,"opened": False}, {"card_x" :210, "card_y" : 150, "filling":None,"opened": False},  {"card_x" :210, "card_y" : 210, "filling":None, "opened": False}, {"card_x" :210, "card_y" : 270, "filling":None,"opened": False}, {"card_x" :270, "card_y" : 150, "filling":None,"opened": False},  {"card_x" :270, "card_y" : 210, "filling":None, "opened": False}, {"card_x" :270, "card_y" : 270, "filling":None,"opened": False}, {"card_x" :330, "card_y" : 150, "filling":None,"opened": False},  {"card_x" :330, "card_y" : 210, "filling":None, "opened": False}, {"card_x" :330, "card_y" : 270, "filling":None,"opened": False}, ]
def b1(event):
    global old_numbers_of_pair
    global cards_of_pair
    global numbers_of_pair
    global turn1
    global points1
    global points2
    global bool_end
    x = event.x
    y = event.y
    if cards_arr[old_numbers_of_pair[0]]["opened"] == False:
        canV.create_rectangle(cards_arr[old_numbers_of_pair[0]]["card_x"] , cards_arr[old_numbers_of_pair[0]]["card_y"] , cards_arr[old_numbers_of_pair[0]]["card_x"]+50 ,cards_arr[old_numbers_of_pair[0]]["card_y"]+50, fill="black")
        bool_end = False

    if cards_arr[old_numbers_of_pair[1]]["opened"] == False:
        canV.create_rectangle(cards_arr[old_numbers_of_pair[1]]["card_x"] , cards_arr[old_numbers_of_pair[1]]["card_y"] , cards_arr[old_numbers_of_pair[1]]["card_x"]+50 ,cards_arr[old_numbers_of_pair[1]]["card_y"]+50, fill="black")
    for i in range(len(cards_arr)):
        if cards_arr[i]["card_x"]+50 >= x >= cards_arr[i]["card_x"] and cards_arr[i]["card_y"]+50 >= y >= cards_arr[i]["card_y"] and cards_arr[i]["opened"] == False:
            canV.create_rectangle(cards_arr[i]["card_x"] , cards_arr[i]["card_y"] , cards_arr[i]["card_x"]+50 ,cards_arr[i]["card_y"]+50, fill=cards_arr[i]["filling"])
            numbers_of_pair.append(i)
    if len(numbers_of_pair) == 2:
        if cards_arr[numbers_of_pair[0]]["filling"] == cards_arr[numbers_of_pair[1]]["filling"]:
            cards_arr[numbers_of_pair[0]]["opened"] = True
            cards_arr[numbers_of_pair[1]]["opened"] = True
            if turn1:
                points1+=1
                text1.config(text='Пары первого игрока: '+str(points1))
            else:
                points2+=1
                text2.config(text='Пары второго игрока: '+str(points2))
        else:
            bool_end = True
            def fun_time():
                print("start")
                time_start = int(time.time())
                # global old_numbers_of_pair
                while(time_start+3 > int(time.time()) and bool_end):
                    pass
                canV.create_rectangle(cards_arr[old_numbers_of_pair[0]]["card_x"] , cards_arr[old_numbers_of_pair[0]]["card_y"] , cards_arr[old_numbers_of_pair[0]]["card_x"]+50 ,cards_arr[old_numbers_of_pair[0]]["card_y"]+50, fill="black")

                canV.create_rectangle(cards_arr[old_numbers_of_pair[1]]["card_x"] , cards_arr[old_numbers_of_pair[1]]["card_y"] , cards_arr[old_numbers_of_pair[1]]["card_x"]+50 ,cards_arr[old_numbers_of_pair[1]]["card_y"]+50, fill="black")
                print("end")
            old_numbers_of_pair = numbers_of_pair
            thread_1 = threading.Thread(target=fun_time)
            thread_1.start()

            

            
            if turn1:
                turn1=False
                text_turn.config(text='Ход второго игрока')
            else:
                turn1=True
                text_turn.config(text='Ход первого игрока')
        numbers_of_pair= []

root.bind("<Button-1>" , b1)
text1 = Label(text="Пары первого игрока: 0")
text1.place(h=11 , x=100 , y = 85)
text2 = Label(text="Пары второго игрока: 0")
text2.place(h=11 , x=400 , y = 85)
text_turn = Label(text="Ход первого игрока")
text_turn.place(h=30 , x=200 , y = 50)
button = Button(text="RESTART", command=game(cards_arr))
button.place(h=61 , w=61 , x=250 , y = 350)

root.mainloop()