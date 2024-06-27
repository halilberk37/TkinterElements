from tkinter import *

pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")

menu = Menu(pencere)

pencere.config(menu = menu)

dosya = Menu(menu)

menu.add_cascade(label = "Dosya",menu = dosya)

dosya.add_command(label = "Aç")
dosya.add_command(label = "Kaydet")
dosya.add_command(label = "Farklı Kaydet...")
dosya.add_command(label = "Çıkış", command = pencere.destroy)

yeni = Menu(dosya)
dosya.add_cascade(label = "Yeni",menu = yeni)

yeni.add_command(label = "Metin Belgesi")
yeni.add_command(label = "Resim Belgesi")
yeni.add_command(label = "pdf dökümanı")

dosya2 = Menu(menu)
menu.add_cascade(label="Düzen",menu=dosya2)
dosya2.add_command(label="Bul")




mainloop()