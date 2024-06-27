from tkinter import *

pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")

def ekle():
    metin = giris.get()
    liste.insert(END,metin)
    giris.delete(0,END)

cerceve1 = Frame(pencere, width = 50, height = 20)
cerceve1.pack(side = LEFT)
sb = Scrollbar(cerceve1)

cerceve2 = Frame(pencere, width = 50, height = 20)
cerceve2.pack(side = RIGHT)


liste = Listbox(cerceve1,width = 20,height = 5,bg = "Aqua",bd=4,yscrollcommand=sb.set)
liste.pack(pady=10,side=LEFT)

sb.config(command = liste.yview)
sb.pack(side = RIGHT, fill = Y)

giris = Entry(cerceve2)
giris.pack(pady=10)

dugme1 = Button(cerceve2,text="Ekle",command = ekle)
dugme1.pack(pady=10)

mainloop()