from tkinter import *

pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")

def fonk1(deger1):
    etiket.config(text = "Değer : "+deger1)

def fonk2(deger2):
    etiket1.config(text = "Değer: "+deger2)


deger1 = IntVar()
deger2 = IntVar()

slider1 = Scale(pencere,
                label ="Ses",
                from_=0, to = 200,
                tickinterval = 20,
                length=200,
                variable = deger1,
                command = fonk1, showvalue = 0)
slider1.pack(side =LEFT)

etiket = Label(pencere,
               text = "Değer : 0",
               font = "Helvetica 10 bold")
etiket.pack()

slider2 = Scale(pencere, label="parlaklık",
                from_ = 0, to=30,
                orient = HORIZONTAL,
                resolution = 0.5,length=100, variable = deger2,
                command = fonk2, showvalue = 1)
slider2.pack(side = BOTTOM)

etiket1 = Label(pencere,
                text = "Değer : 0",
                font = "Helvetica 10 bold")
etiket1.pack(side = BOTTOM)
pencere.mainloop()







mainloop()