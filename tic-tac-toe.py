from tkinter import Tk,ttk,Button
from tkinter import messagebox
from tkinter import *
from random import randint

ActivePlayer = 1
p1 = []
p2 = []
mov = 0

# function for instructions button
def open_popup():
   top= Toplevel(root)
   top.title("Instructions")
   top.geometry("570x580")
   top.resizable(0,0)
   canvas= Canvas(top, width= 1000, height= 750)
   canvas.pack()   

   canvas.create_text(280, 150, text="INSTRUCTIONS:\n", fill="black", font=('mistral 50 bold'))
   canvas.create_text(279, 230, text="\n 1. The game is played on a grid that's 3 squares by 3 squares.", fill="black", font=('Monaco 10 '))
   canvas.create_text(155, 250, text="\n 2. The player 1 will be the 'X'", fill="black", font=('Monaco 10 '))
   canvas.create_text(155, 270, text="\n 3. The player 2 will be the 'O'", fill="black", font=('Monaco 10 '))
   canvas.create_text(279, 300, text="\n 4. The first player to get 3 of her marks in a row (up, down, \n            across, or diagonally) is the winner.", fill="black", font=('Monaco 10 '))
   canvas.create_text(279, 336, text="\n 5. When all 9 squares are full, the game is over. If no player\n          has 3 marks in a row, the game ends in a tie.", fill="black", font=('Monaco 10 '))
   btn = Button(top, text='Ready to Play? \n Start the Game!', width=30, height=3, bd='5', command=top.destroy, font=("Mistral 20"), bg="pink")
   btn.place(x=105, y=400)


def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(['disabled'])

from PIL import ImageTk, Image

# functions for winner message
def message():
    global my_img
    top = Toplevel()   
    top.resizable(0,0)
    top.title("Congratulations!!")
    my_img = ImageTk.PhotoImage(Image.open("congrats.png"))
    Label(top, image=my_img).pack()

def message2():
    global my_img
    top = Toplevel()
    top.resizable(0,0)
    top.title("Congratulations!!")
    my_img = ImageTk.PhotoImage(Image.open("congrats 2.png"))
    Label(top, image=my_img).pack()

def message3():
    global my_img
    top = Toplevel()
    top.resizable(0,0)
    top.title("Draw!!")
    my_img = ImageTk.PhotoImage(Image.open("draw.png"))
    Label(top, image=my_img).pack()


def CheckWinner():
    global mov 
    winner = 0

    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and ( 9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and ( 9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and ( 7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner ==1:
        message()
      
    elif winner ==2:
        message2()

    elif mov ==9:
        message3()


def ButtonClick(id):
    global ActivePlayer
    global p1,p2
    global mov

    if(ActivePlayer ==1):
        SetLayout(id,"X")
        p1.append(id)
        mov +=1
        ActivePlayer =2

    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id)
        mov +=1
        ActivePlayer =1
    CheckWinner()


def AutoPlay():
    global p1; global p2
    Empty = []
    for cell in range(9):
        if(not((cell +1 in p1) or (cell +1 in p2))):
            Empty.append(cell+1)
    try:
        RandIndex = randint(0,len(Empty) -1)
        ButtonClick(Empty[RandIndex])
    except:
        pass



def EnableAll():
    b1.config(text= " ")
    b1.state(['!disabled'])
    b2.config(text= " ")
    b2.state(['!disabled'])
    b3.config(text= " ")
    b3.state(['!disabled'])
    b4.config(text= " ")
    b4.state(['!disabled'])
    b5.config(text= " ")
    b5.state(['!disabled'])
    b6.config(text= " ")
    b6.state(['!disabled'])
    b7.config(text= " ")
    b7.state(['!disabled'])
    b8.config(text= " ")
    b8.state(['!disabled'])
    b9.config(text= " ")
    b9.state(['!disabled'])


def Restart():
    global p1,p2,mov,ActivePlayer
    p1.clear(); p2.clear()
    mov,ActivePlayer = 0,1
    EnableAll()

# function for disabling the exit button of a window
def disable_event():
   pass

# function for exit button
def Exit():
    response = messagebox.askquestion("Exit", "Are you sure?")
    root.protocol("WM_DELETE_WINDOW", disable_event)
    if response == "yes":
        quit()
    else:
        return None



root = Tk()
root.overrideredirect(True)

# adding background color
root.configure(bg='#621940')

#Adding styles and colors for the button
style = ttk.Style()
style.theme_use('alt')
style.configure('my.TButton', background = '#ffb997', foreground = 'black', width = 15, borderwidth=1, focusthickness=3, focuscolor='none', font=("Chiller", 33, "bold"))
style.map('TButton', background=[('active','#f67e7d')])


b1 = ttk.Button(root, text=" ", style="my.TButton")
b1.grid(row=1, column=0, sticky="nwse", ipadx=50,ipady=50)
b1.config(command = lambda : ButtonClick(1))

b2 = ttk.Button(root, text=" ",style ="my.TButton")
b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
b2.config(command = lambda : ButtonClick(2))

b3= ttk.Button(root, text=" ",style="my.TButton")
b3.grid(row=1, column=2, sticky="snew", ipadx=50,
        ipady=50)
b3.config(command = lambda : ButtonClick(3))

b4 = ttk.Button(root, text=" ",style="my.TButton")
b4.grid(row=2, column=0, sticky="snew", ipadx=50,
        ipady=50)
b4.config(command = lambda : ButtonClick(4))

b5 = ttk.Button(root, text=" ",style="my.TButton")
b5.grid(row=2, column=1, sticky="snew", ipadx=50,
        ipady=50)
b5.config(command = lambda : ButtonClick(5))

b6 = ttk.Button(root, text=" ",style="my.TButton")
b6.grid(row=2, column=2, sticky="snew", ipadx=50,
        ipady=50)
b6.config(command = lambda : ButtonClick(6))

b7 = ttk.Button(root, text=" ",style="my.TButton")
b7.grid(row=3, column=0, sticky="snew", ipadx=50,
        ipady=50)
b7.config(command = lambda : ButtonClick(7))

b8 = ttk.Button(root, text=" ",style="my.TButton")
b8.grid(row=3, column=1, sticky="snew", ipadx=50,
        ipady=50)
b8.config(command = lambda : ButtonClick(8))

b9 = ttk.Button(root, text=" ",style="my.TButton")
b9.grid(row=3, column=2, sticky="snew", ipadx=50,
        ipady=50)
b9.config(command = lambda : ButtonClick(9))


# adding image for the button
click_btn= PhotoImage(file='newgame.png')
click_btn2 = PhotoImage(file='quit.png')

img_label= Label(image=click_btn)
img_label2 = Label(image=click_btn2)

# Modifying the buttons color and structure
Button(image=click_btn, font=('Mistral', 25, 'bold', 'underline'), bg='#de6fa1', fg='white',
            border=10, width=6,command = lambda :Restart()).grid(row=0, column=0, sticky="we")

# Adding buttons for exit and instructions            
b10 = Button(image=click_btn2, command= Exit, font=('Mistral', 25, 'bold', 'underline'), bg='#843b62', fg='white',
            border=10, width=6,)
b10.grid(row=0, column=2, sticky="snew")
b11 = Button(text= "Instructions", command= open_popup, font=('Mistral', 25, 'bold', 'underline'), bg='#a63a7a', fg='white',
            border=10, width=6,)
b11.grid(row=0, column=1, sticky="snew")


root.mainloop()