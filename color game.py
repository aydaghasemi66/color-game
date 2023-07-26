from tkinter import *
import random
from tkinter import messagebox

win = Tk()
win.geometry('400x350')
win.resizable(0, 0)
win.title('Color Game')

# Variables========================================
colors = ['red', 'yellow', 'blue', 'black', 'gray','white','orange','pink']
timee = 30
scoree = 0

# Functions========================================
def start_game(event):
    global timee
    if timee == 30:
        countdown()
    next_color()

def next_color():
    global timee, scoree
    if timee > 0:
        if e1.get().lower() == colors[1]:
            scoree += 1
        e1.delete(0, END)
        random.shuffle(colors)
        color.config(fg=str(colors[1]), text=str(colors[0]))
        score.config(text='امتیاز: ' + str(scoree))

def countdown():
    global timee
    if timee > 0:
        timee -= 1
        time.config(text='زمان: ' + str(timee))
    else:
        messagebox.showinfo("پایان بازی", "زمان شما به پایان رسید!")
        return
    time.after(1000, countdown)

# Labels==============================================
color = Label(win, font="tahoma 30 bold", text=" ",bg = "#40E0D0")
color.place(x=135, y=150)
l1 = Label(win, font="tahoma 12 bold", text="رنگ هر کلمه را به زبان انگلیسی وارد کنید ",bg="#40E0D0")
l1.place(x=30, y=20)
time = Label(win, font="tahoma 12 bold", text="زمان: 30",bg= "#40E0D0")
time.place(x=150, y=90)
score = Label(win, font="tahoma 12 bold", text="0 :امتیاز",bg= "#40E0D0")
score.place(x=150, y=70)


# Buttons=============================================
win.bind('<Return>', start_game)

e1 = Entry(width=30)
e1.place(x=100, y=250)
e1.focus_set()
win.config(background="#40E0D0")
win.mainloop()





