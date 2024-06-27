from tkinter import *

pencere = Tk()
pencere.geometry("500x500+700+500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")

etiket1 = Label(pencere,text="Etiket1")
etiket1.pack()

etiket2 = Label(pencere,text="Etiket2",fg="white",bg="black")
etiket2.pack(side = LEFT)

etiket3 = Label(pencere,text="Etiket3",fg="black",bg="white",font="sans 20")
etiket3.pack(side = RIGHT)

etiket4 = Label(pencere,text="Etiket4",width=20,height=10).pack(side = BOTTOM)




mainloop()