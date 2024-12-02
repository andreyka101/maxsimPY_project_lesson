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


    bool_progress_indicator = True
    for y_index in range(1,4):
        if(dist_button[f'button_X1_Y{y_index}']["text"] == dist_button[f'button_X3_Y{y_index}']["text"] and dist_button[f'button_X1_Y{y_index}']["text"] != " " and bool_progress_indicator and dist_button[f'button_X2_Y{y_index}']["text"] == " "):
            dist_button[f'button_X2_Y{y_index}'].config(text="o")
            bool_progress_indicator = False
        for x_index  in range(1,3):
            if(dist_button[f'button_X{x_index}_Y{y_index}']["text"] == dist_button[f'button_X{x_index+1}_Y{y_index}']["text"] and dist_button[f'button_X{x_index}_Y{y_index}']["text"] != " " and bool_progress_indicator and (dist_button[f'button_X1_Y{y_index}']["text"] == " " or dist_button[f'button_X2_Y{y_index}']["text"] == " " or dist_button[f'button_X3_Y{y_index}']["text"] == " ")):
                # dist_button[f'button_X{x_index}_Y{y_index}'].config(bg="#3e8bff")
                # dist_button[f'button_X{x_index+1}_Y{y_index}'].config(bg="#3e8bff")
                bool_progress_indicator = False
                if(x_index == 1):
                    dist_button[f'button_X3_Y{y_index}'].config(text="o")
                else:
                    dist_button[f'button_X1_Y{y_index}'].config(text="o")
    for x_index in range(1,4):
        if(dist_button[f'button_X{x_index}_Y1']["text"] == dist_button[f'button_X{x_index}_Y3']["text"] and dist_button[f'button_X{x_index}_Y1']["text"] != " " and bool_progress_indicator and dist_button[f'button_X{x_index}_Y2']["text"] == " "):
            dist_button[f'button_X{x_index}_Y2'].config(text="o")
            bool_progress_indicator = False
        for y_index  in range(1,3):
            if(dist_button[f'button_X{x_index}_Y{y_index}']["text"] == dist_button[f'button_X{x_index}_Y{y_index+1}']["text"] and dist_button[f'button_X{x_index}_Y{y_index}']["text"] != " " and bool_progress_indicator and (dist_button[f'button_X{x_index}_Y1']["text"] == " " or dist_button[f'button_X{x_index}_Y2']["text"] == " " or dist_button[f'button_X{x_index}_Y3']["text"] == " ")):
                bool_progress_indicator = False
                # dist_button[f'button_X{x_index}_Y{y_index}'].config(bg="#3e8bff")
                # dist_button[f'button_X{x_index}_Y{y_index+1}'].config(bg="#3e8bff")
                if(y_index == 1):
                    dist_button[f'button_X{x_index}_Y3'].config(text="o")
                else:
                    dist_button[f'button_X{x_index}_Y1'].config(text="o")
    
    
    if(dist_button[f'button_X1_Y1']["text"] == dist_button[f'button_X2_Y2']["text"] and dist_button[f'button_X2_Y2']["text"] != " " and bool_progress_indicator and dist_button[f'button_X3_Y3']["text"] == " "):
        bool_progress_indicator = False
        dist_button[f'button_X3_Y3'].config(text="o")

    if(dist_button[f'button_X3_Y3']["text"] == dist_button[f'button_X2_Y2']["text"] and dist_button[f'button_X2_Y2']["text"] != " " and bool_progress_indicator and dist_button[f'button_X1_Y1']["text"] == " "):
        bool_progress_indicator = False
        dist_button[f'button_X1_Y1'].config(text="o")

    if(dist_button[f'button_X3_Y1']["text"] == dist_button[f'button_X2_Y2']["text"] and dist_button[f'button_X2_Y2']["text"] != " " and bool_progress_indicator and dist_button[f'button_X1_Y3']["text"] == " "):
        bool_progress_indicator = False
        dist_button[f'button_X1_Y3'].config(text="o")

    if(dist_button[f'button_X1_Y3']["text"] == dist_button[f'button_X2_Y2']["text"] and dist_button[f'button_X2_Y2']["text"] != " " and bool_progress_indicator and dist_button[f'button_X3_Y1']["text"] == " "):
        bool_progress_indicator = False
        dist_button[f'button_X3_Y1'].config(text="o")


    if(dist_button['button_X2_Y2']["text"] == " " and bool_progress_indicator):
        bool_progress_indicator = False
        dist_button['button_X2_Y2'].config(text="o")
    elif(len(arr_corner_buttons_all) != 0 and num_bool_hard_1 and bool_progress_indicator):
        bool_progress_indicator = False
        num_bool_hard_1 = False
        rund = random.randint(0,len(arr_corner_buttons_all) -1)
        arr_corner_buttons_all[rund].config(text="o")
    print(bool_progress_indicator)


    if(bool_progress_indicator):
        free_button_arr = []
        for key , button_i  in dist_button.items():
            if(button_i["text"] == " "):
                free_button_arr.append(key)
        
        if(len(free_button_arr) == 0): return
        choice_PC = random.randint(1 , len(free_button_arr))
        dist_button[free_button_arr[choice_PC - 1]].config(text="o")

    bool_progress_indicator = True


    


