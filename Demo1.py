from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My first GUI")

btn1 = Button(text = "Click me", fg = "Red", bg = "Yellow")
btn1.place(x=200,y=200)
txtfld = Entry(window, border = 2)
txtfld.place(x=250, y=250)



window.mainloop()