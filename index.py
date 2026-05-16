from tkinter import *

root = Tk()
root.geometry('180x100')
root.title("Main Window")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top,text="This is the top level window")
    l2.pack()

   

l = Label(root, text="This is the root window")
btn = Button(root, text="Click here to open another window", command=topwin,
bg="blue", fg="white")

l.pack()
btn.pack()

root.mainloop()