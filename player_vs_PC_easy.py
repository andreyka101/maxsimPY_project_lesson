import random
def player_vs_PC_easy(dist_button):
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




def f_PC_easy(dist_button):
    free_button_arr = []
    for key , button_i  in dist_button.items():
        if(button_i["text"] == " "):
            free_button_arr.append(key)
    
    if(len(free_button_arr) == 0): return
    choice_PC = random.randint(1 , len(free_button_arr))
    dist_button[free_button_arr[choice_PC - 1]].config(text="o")


