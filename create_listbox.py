from tkinter import *

pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")
def ekle():
    metin = giris.get() #Entry içindeki ifade.
    liste.insert(END,metin)
    giris.delete(0,END)

liste = Listbox(pencere,width = 20, height = 10, bg = "Aqua",bd = 4)
liste.pack(pady=10)

giris = Entry()
giris.pack(pady = 10)

dugme1 = Button(text ="Ekle", command = ekle)
dugme1.pack(pady = 10)

dugme2 = Button(text ="Çıkış", command = pencere.destroy)
dugme2.pack(pady = 10)



mainloop()