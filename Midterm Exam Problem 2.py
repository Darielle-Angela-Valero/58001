from tkinter import*
class name:
    def __init__(self,win):
        self.lbl1 = Label(win, text = "My Full Name")
        self.lbl1.place(x=170,y=40)

        self.lbl2 = Label(win, text="Enter Given Name:")
        self.lbl2.place(x=70, y=75)

        self.lbl3 = Label(win, text ="Enter Middle Name:")
        self.lbl3.place(x=70,y=105)

        self.lbl4 = Label(win, text="Enter Last Name:")
        self.lbl4.place(x=70, y=135)

        self.lbl5 = Label(win, text ="My Full Name is:")
        self.lbl5.place(x=70, y=175 )

        self.entry1 = Entry(win,bd =2)
        self.entry1.place(x=255, y=105)

        self.entry2 = Entry(win, bd=2)
        self.entry2.place(x=255, y=75)

        self.entry3 = Entry(win, bd=2)
        self.entry3.place(x=255, y=135)

        self.entry4 = Entry(win, bd=2)
        self.entry4.place(x=255, y=175)

        self.btn = Button(text= "Show Full Name")
        self.btn.place(x=170,y=210)
        self.btn.bind("<Button-1>", self.fullname)

    def fullname(self, fullname):
        self.entry4.delete(0, 'end')
        fn  = str(self.entry1.get())
        sn = str(self.entry2.get())
        ln = str(self.entry3.get())
        result = sn + fn + ln
        self.entry4.insert(END, str(result))


window = Tk()
window.geometry("500x400+10+10")
window.title("Midterm Exam Problem 2")
mywin = name(window)
window.mainloop()

