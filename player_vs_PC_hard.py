import random
def player_vs_PC_hard(dist_button):
    str_o_x = "x"
    for i in range(2):
        if(i == 1):
            str_o_x = "o"
        if (dist_button['button_X1_Y1']["text"] == str_o_x and dist_button['button_X1_Y2']["text"] == str_o_x and dist_button['button_X1_Y3']["text"] == str_o_x):
            dist_button['button_X1_Y1'].config(bg="#FF4040")
            dist_button['button_X1_Y2'].config(bg="#FF4040")
            dist_button['button_X1_Y3'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X2_Y1']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X2_Y3']["text"] == str_o_x):
            dist_button['button_X2_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X2_Y3'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X3_Y1']["text"] == str_o_x and dist_button['button_X3_Y2']["text"] == str_o_x and dist_button['button_X3_Y3']["text"] == str_o_x):
            dist_button['button_X3_Y1'].config(bg="#FF4040")
            dist_button['button_X3_Y2'].config(bg="#FF4040")
            dist_button['button_X3_Y3'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X1_Y1']["text"] == str_o_x and dist_button['button_X2_Y1']["text"] == str_o_x and dist_button['button_X3_Y1']["text"] == str_o_x):
            dist_button['button_X1_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y1'].config(bg="#FF4040")
            dist_button['button_X3_Y1'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X1_Y2']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X3_Y2']["text"] == str_o_x):
            dist_button['button_X1_Y2'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X3_Y2'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X1_Y3']["text"] == str_o_x and dist_button['button_X2_Y3']["text"] == str_o_x and dist_button['button_X3_Y3']["text"] == str_o_x):
            dist_button['button_X1_Y3'].config(bg="#FF4040")
            dist_button['button_X2_Y3'].config(bg="#FF4040")
            dist_button['button_X3_Y3'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X1_Y1']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X3_Y3']["text"] == str_o_x):
            dist_button['button_X1_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X3_Y3'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }

        elif (dist_button['button_X3_Y1']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X1_Y3']["text"] == str_o_x):
            dist_button['button_X3_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X1_Y3'].config(bg="#FF4040")
            return {
                "end" : True,
                "symbol" : str_o_x,
            }
        else:
            num = 0
            for key , button_i  in dist_button.items():
                if(button_i["text"] != " "):
                    num +=1
            if(num == 9):
                return {
                    "end" : True,
                    "symbol" : "none",
                }

    
    return {
        "end" : False
    }



num_bool_hard_1 = True
def f_PC_hard(dist_button):
    global num_bool_hard_1
    arr_corner_buttons_all = [dist_button['button_X1_Y1'] , dist_button['button_X3_Y1'] , dist_button['button_X3_Y3'] , dist_button['button_X1_Y3']]
    arr_corner_buttons_all = list(filter(lambda x: x["text"] == " " , arr_corner_buttons_all))
    if(dist_button['button_X2_Y2']["text"] == " "):
        dist_button['button_X2_Y2'].config(text="o")
    elif(len(arr_corner_buttons_all) != 0 and num_bool_hard_1):
        num_bool_hard_1 = False
        rund = random.randint(0,len(arr_corner_buttons_all) -1)
        arr_corner_buttons_all[rund].config(text="o")
    else:
        for x_index in range(1,3):
            for y_index  in range(1,4):
                if(dist_button[f'button_X{x_index}_Y{y_index}']["text"] == dist_button[f'button_X{x_index+1}_Y{y_index}']["text"] and dist_button[f'button_X{x_index}_Y{y_index}']["text"] != " "):
                    dist_button[f'button_X{x_index}_Y{y_index}'].config(bg="#3e8bff")
                    dist_button[f'button_X{x_index+1}_Y{y_index}'].config(bg="#3e8bff")

    


