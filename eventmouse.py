from tkinter import *

def bul(event):
    etiket["text"] = "x = {}, y = {}".format(event.x,event.y)

pencere = Tk()
pencere.geometry("600x400")
etiket1 = Label(pencere,font="Comic 15 bold")
etiket1.pack(pady = 10)

etiket =Label(pencere,text="Sol tık yap kordinat bul",
              font = "Comic 15 bold")
etiket.pack(pady = 30)

pencere.bind("<Button-1>",bul) #Sol tık
pencere.bind("<Button-2>",bul) #orta tık
pencere.bind("<Button-3>",bul) #sağ tık
pencere.mainloop()