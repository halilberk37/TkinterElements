from tkinter import *
from tkinter.ttk import *
pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")

etiket = Label(pencere, font = "Helvetica 20 bold")
etiket.pack(pady = 40)

cubuk = Progressbar(pencere,orient = HORIZONTAL, length = 400, mode = "determinate")

def bar():
    import time
    a = 1
    while a <= 100:
        cubuk["value"] = a
        etiket.config(text = str(a))
        pencere.update_idletasks()
        time.sleep(0.05)
        a+=1
    time.sleep(2)
    etiket.config(text="Yüklendi...")


cubuk.pack(pady = 10)
buton=Button(pencere,text = "Yükle", command=bar).pack(pady=10)

mainloop()