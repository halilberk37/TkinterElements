from tkinter import *

pencere = Tk()
pencere.geometry("500x300")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")

giris1 = Entry(pencere).pack()

giris2 = Entry(pencere,bg="Aqua",fg = "red", font = "Helvetica 12 bold italic", justify = "center", bd = 3)
giris2.pack(side = LEFT)

giris3 = Entry(pencere,show = "*").pack(side = RIGHT)
state = "disabled"
state = "normal"
giris4 = Entry(pencere,state = state)
giris4.pack(side = BOTTOM)
mainloop()