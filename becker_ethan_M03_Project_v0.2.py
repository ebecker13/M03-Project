import tkinter as tk




#greeting
window = tk.Tk()
greeting = tk.Label(text="Hello, select amount of players")
greeting.pack()
#player count select 
window = tk.Tk()
frame = tk.Frame(master=window, width=600, height=600)
frame.pack()
#2 plaer button 
TwoPlayers = tk.Button(master=frame, text="2 players", bg="red")
TwoPlayers.place(x=0, y=10)
#3 player button
ThreePlayers = tk.Button(master=frame, text="3 players", bg="yellow")
ThreePlayers.place(x=0, y=20)
#4 player button
FourPlayers = tk.Button(master=frame, text="4 players", bg="blue")
FourPlayers.place(x=0, y=50)

def player_count_2(event):
#2 player window
    print("2 players")
#player 1 vars 
    def increase1():
        value1 = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value1 + 1}"
    def decrease1():
        value1 = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value1 - 1}"
#player 2 vars 
    def increase2():
        value2 = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value2 + 1}"
    def decrease2():
        value2 = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value2 - 1 }"


#create 2 player window   
    window = tk.Tk()
    window.rowconfigure(1, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#Create buttons and counter and labels for all player
    
    #player 1
#pl label
    P1label = tk.Label(text="Player1")
    P1label.config(font =("Courier", 14))
    P1label.grid(row=0,column=1)
#p1 munis button
    btn_decrease1 = tk.Button(master=window, text="-", command=decrease1)
    btn_decrease1.grid(row=1, column=0, sticky="nsew")
#p1 value button
    lbl_value1 = tk.Label(master=window, text="0")
    lbl_value1.grid(row=1, column=1)
#p1 plus button
    btn_increase1 = tk.Button(master=window, text="+", command=increase1)
    btn_increase1.grid(row=1, column=2, sticky="nsew")
    #player2
#p2 label
    P2label = tk.Label(text="Player2")
    P2label.config(font =("Courier", 14))
    P2label.grid(row=2,column=1)
#p2 munis button
    btn_decrease2 = tk.Button(master=window, text="-", command=decrease2)
    btn_decrease2.grid(row=3, column=0, sticky="nsew")
#p2 va;ue button
    lbl_value2 = tk.Label(master=window, text="0")
    lbl_value2.grid(row=3, column=1)
#p2 plus button
    btn_increase2 = tk.Button(master=window, text="+", command=increase2)
    btn_increase2.grid(row=3, column=2, sticky="nsew")
#back button
    btn_back = tk.Button( master=window,  text="back", bg="red", command=window.destroy  )
    btn_back.grid(row=9, column=1, sticky="nsew")
    btn_back.bind("<Button-1>", back)
        
def player_count_3(event):
# 3 player window
    print("3 players")
#player 1 vars 
    def increase1():
        value1 = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value1 + 1}"
    def decrease1():
        value1 = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value1 - 1}"
#player 2 vars 
    def increase2():
        value2 = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value2 + 1}"
    def decrease2():
        value2 = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value2 - 1 }"
#player 3 vars
    def increase3():
        value3 = int(lbl_value3["text"])
        lbl_value3["text"] = f"{value3 + 1}"
    def decrease3():
        value3 = int(lbl_value3["text"])
        lbl_value3["text"] = f"{value3 - 1 }"


#create 3 player window
    window = tk.Tk()
    window.rowconfigure(1, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)
    
#Create buttons and counter and labels for all player
    
   #player 1
#pl label
    P1label = tk.Label(text="Player1")
    P1label.config(font =("Courier", 14))
    P1label.grid(row=0,column=1)
#p1 munis button
    btn_decrease1 = tk.Button(master=window, text="-", command=decrease1)
    btn_decrease1.grid(row=1, column=0, sticky="nsew")
#p1 value button
    lbl_value1 = tk.Label(master=window, text="0")
    lbl_value1.grid(row=1, column=1)
#p1 plus button
    btn_increase1 = tk.Button(master=window, text="+", command=increase1)
    btn_increase1.grid(row=1, column=2, sticky="nsew")
    #player2
#p2 label
    P2label = tk.Label(text="Player2")
    P2label.config(font =("Courier", 14))
    P2label.grid(row=2,column=1)
#p2 munis button
    btn_decrease2 = tk.Button(master=window, text="-", command=decrease2)
    btn_decrease2.grid(row=3, column=0, sticky="nsew")
#p2 va;ue button
    lbl_value2 = tk.Label(master=window, text="0")
    lbl_value2.grid(row=3, column=1)
#p2 plus button
    btn_increase2 = tk.Button(master=window, text="+", command=increase2)
    btn_increase2.grid(row=3, column=2, sticky="nsew")
    #player3
#p3 label
    P3label = tk.Label(text="Player3")
    P3label.config(font =("Courier", 14))
    P3label.grid(row=4,column=1)
#p3 munis button
    btn_decrease3 = tk.Button(master=window, text="-", command=decrease3)
    btn_decrease3.grid(row=5, column=0, sticky="nsew")
#p3 va;ue button
    lbl_value3 = tk.Label(master=window, text="0")
    lbl_value3.grid(row=5, column=1)
#p3 plus button
    btn_increase3 = tk.Button(master=window, text="+", command=increase3)
    btn_increase3.grid(row=5, column=2, sticky="nsew")
#back button
    btn_back = tk.Button( master=window,  text="back", bg="red", command=window.destroy  )
    btn_back.grid(row=9, column=1, sticky="nsew")
    btn_back.bind("<Button-1>", back)
def player_count_4(event):
# 4 player window
    print("4 players")

#player 1 vars 
    def increase1():
        value1 = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value1 + 1}"
    def decrease1():
        value1 = int(lbl_value1["text"])
        lbl_value1["text"] = f"{value1 - 1}"
#player 2 vars 
    def increase2():
        value2 = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value2 + 1}"
    def decrease2():
        value2 = int(lbl_value2["text"])
        lbl_value2["text"] = f"{value2 - 1 }"
#player 3 vars 
    def increase3():
        value3 = int(lbl_value3["text"])
        lbl_value3["text"] = f"{value3 + 1}"
    def decrease3():
        value3 = int(lbl_value3["text"])
        lbl_value3["text"] = f"{value3 - 1 }"
#player 4 vars 
    def increase4():
        value4 = int(lbl_value4["text"])
        lbl_value4["text"] = f"{value4 + 1}"
    def decrease4():
        value4 = int(lbl_value4["text"])
        lbl_value4["text"] = f"{value4 - 1 }"


        
#create 4 player window
    window = tk.Tk()
    window.rowconfigure(1, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

#Create buttons and counter and labels for all player
    
   #player 1
#pl label
    P1label = tk.Label(text="Player1")
    P1label.config(font =("Courier", 14))
    P1label.grid(row=0,column=1)
#p1 munis button
    btn_decrease1 = tk.Button(master=window, text="-", command=decrease1)
    btn_decrease1.grid(row=1, column=0, sticky="nsew")
#p1 value button
    lbl_value1 = tk.Label(master=window, text="0")
    lbl_value1.grid(row=1, column=1)
#p1 plus button
    btn_increase1 = tk.Button(master=window, text="+", command=increase1)
    btn_increase1.grid(row=1, column=2, sticky="nsew")
    #player2
#p2 label
    P2label = tk.Label(text="Player2")
    P2label.config(font =("Courier", 14))
    P2label.grid(row=2,column=1)
#p2 munis button
    btn_decrease2 = tk.Button(master=window, text="-", command=decrease2)
    btn_decrease2.grid(row=3, column=0, sticky="nsew")
#p2 va;ue button
    lbl_value2 = tk.Label(master=window, text="0")
    lbl_value2.grid(row=3, column=1)
#p2 plus button
    btn_increase2 = tk.Button(master=window, text="+", command=increase2)
    btn_increase2.grid(row=3, column=2, sticky="nsew")
    #player3
#p3 label
    P3label = tk.Label(text="Player3")
    P3label.config(font =("Courier", 14))
    P3label.grid(row=4,column=1)
#p3 munis button
    btn_decrease3 = tk.Button(master=window, text="-", command=decrease3)
    btn_decrease3.grid(row=5, column=0, sticky="nsew")
#p3 value button
    lbl_value3 = tk.Label(master=window, text="0")
    lbl_value3.grid(row=5, column=1)
#p3 plus button
    btn_increase3 = tk.Button(master=window, text="+", command=increase3)
    btn_increase3.grid(row=5, column=2, sticky="nsew")
    #player4
#p4 label
    P4label = tk.Label(text="Player4")
    P4label.config(font =("Courier", 14))
    P4label.grid(row=6,column=1)
#p4 munis button
    btn_decrease4 = tk.Button(master=window, text="-", command=decrease4)
    btn_decrease4.grid(row=7, column=0, sticky="nsew")
#p4 va;ue button
    lbl_value4 = tk.Label(master=window, text="0")
    lbl_value4.grid(row=7, column=1)
#p4 plus button
    btn_increase4 = tk.Button(master=window, text="+", command=increase4)
    btn_increase4.grid(row=7, column=2, sticky="nsew")
#back button
    btn_back = tk.Button( master=window,  text="back", bg="red",command=window.destroy  )
    btn_back.grid(row=9, column=1, sticky="nsew")
    btn_back.bind("<Button-1>", back)

   
def back(event):
    return ('value1',' value2', 'value3', 'value4')



TwoPlayers.bind("<Button-1>", player_count_2)
ThreePlayers.bind("<Button-1>", player_count_3)
FourPlayers.bind("<Button-1>", player_count_4)



TwoPlayers.pack(fill=tk.X)
ThreePlayers.pack(fill=tk.X)
FourPlayers.pack(fill=tk.X)

 
window.mainloop()

