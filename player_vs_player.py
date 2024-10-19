def player_vs_player_fun_game(dist_button):
    str_o_x = "x"
    for i in range(2):
        if(i == 1):
            str_o_x = "o"
        if (dist_button['button_X1_Y1']["text"] == str_o_x and dist_button['button_X1_Y2']["text"] == str_o_x and dist_button['button_X1_Y3']["text"] == str_o_x):
            dist_button['button_X1_Y1'].config(bg="#FF4040")
            dist_button['button_X1_Y2'].config(bg="#FF4040")
            dist_button['button_X1_Y3'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X2_Y1']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X2_Y3']["text"] == str_o_x):
            dist_button['button_X2_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X2_Y3'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X3_Y1']["text"] == str_o_x and dist_button['button_X3_Y2']["text"] == str_o_x and dist_button['button_X3_Y3']["text"] == str_o_x):
            dist_button['button_X3_Y1'].config(bg="#FF4040")
            dist_button['button_X3_Y2'].config(bg="#FF4040")
            dist_button['button_X3_Y3'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X1_Y1']["text"] == str_o_x and dist_button['button_X2_Y1']["text"] == str_o_x and dist_button['button_X3_Y1']["text"] == str_o_x):
            dist_button['button_X1_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y1'].config(bg="#FF4040")
            dist_button['button_X3_Y1'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X1_Y2']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X3_Y2']["text"] == str_o_x):
            dist_button['button_X1_Y2'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X3_Y2'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X1_Y3']["text"] == str_o_x and dist_button['button_X2_Y3']["text"] == str_o_x and dist_button['button_X3_Y3']["text"] == str_o_x):
            dist_button['button_X1_Y3'].config(bg="#FF4040")
            dist_button['button_X2_Y3'].config(bg="#FF4040")
            dist_button['button_X3_Y3'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X1_Y1']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X3_Y3']["text"] == str_o_x):
            dist_button['button_X1_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X3_Y3'].config(bg="#FF4040")
            return [str_o_x , "ok"]

        if (dist_button['button_X3_Y1']["text"] == str_o_x and dist_button['button_X2_Y2']["text"] == str_o_x and dist_button['button_X1_Y3']["text"] == str_o_x):
            dist_button['button_X3_Y1'].config(bg="#FF4040")
            dist_button['button_X2_Y2'].config(bg="#FF4040")
            dist_button['button_X1_Y3'].config(bg="#FF4040")
            return [str_o_x , "ok"]