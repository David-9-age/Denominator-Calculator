from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Denomination counter")
root.configure(bg='light green')
root.geometry("650x400")

label1 = Label(
    root,
    text = "Hey user! Welcome to Denomination Counter App.",
    bg='light blue'
    font=('Arial', l2)
)
label1.place(relx=0.5, y=200, anchor=CENTER)
def msg():
    Msgbox= messagebox.showinfo("Alert", "Do you want t calculate denomination count?")
    if Msgbox == "ok":
        topwin()
button1= Button(
    root,
    text="Lets get started!",
    command=msg,
    bg="blue",
    fg="white"
)
button1.place(x=250, y=260)

def topwin():
    top = TopLevel()
    top.title("Denomination Calculator")
    top.configure(bg="Red")
    top.geometry("650x400")
    label = Label(top, text="Enter total Amount", bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text="Number of notes for each denomination" , bg="light blue")

    l1 = Label(top, text="1000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 =Entry(top)
    t2 =Entry(top)
    t3 =Entry(top)

    def calculator():
        try:
            amount = int(entry.get())

            note1000 = amount // 1000
            amount %=1000

            note500 = amount // 500
            amount %=500

            note1000 = amount //100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
            

    