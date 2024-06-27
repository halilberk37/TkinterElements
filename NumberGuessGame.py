from tkinter import *
import random

def basla():
    global sayi
    sayi = random.randint(1,300)
    etiket1.destroy()
    baslaButon.destroy()
    global etiket2
    etiket2 = Label(font = "Helvatica 20 bold")
    etiket2.pack(pady=15)
    global giris
    giris = Entry()
    giris.pack(pady=15)
    dugme = Button(text = "Tahmin Et", command = tahmin_et)
    dugme.pack(pady=15)

def tahmin_et():
    tahmin = int(giris.get())
    giris.delete(0,END)

    if tahmin == sayi:
        etiket2.config(text = "Bildiniz... Tebrikler!")
    elif tahmin < sayi:
        etiket2.config(text = "Yukarı")
    elif tahmin > sayi:
        etiket2.config(text ="Aşağı")




pencere = Tk()
pencere.geometry("500x200")

etiket1 = Label(pencere,
                text="1 ile 300 arasında bir sayı tuttum,butona bas ve oyuna başla!",
                font="Verdana, 12 bold")
etiket1.place(relx = 0.1, rely = 0.3)

baslaButon = Button(text = "Başla",
                    width = 10,
                    command=basla)
baslaButon.place(relx = 0.4 , rely = 0.6)
mainloop()