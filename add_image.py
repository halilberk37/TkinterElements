from tkinter import *

pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")
resim = PhotoImage(file = "D:\Özel Çözüm Koleji Genel Büyük Deposu\Çözüm Koleji Tasarımlar\İkonlar\lab-microscope.png")

etiket1 = Label(pencere,text="Etiket1",image = resim).pack()

dugme1 = Button(pencere,text="Giriş")
dugme1.pack(side = LEFT)

dugme2 = Button(pencere,text = "Çıkış",command = pencere.destroy,image = resim)
dugme2.pack(side = RIGHT)

mainloop()