from tkinter import *
from tkinter import ttk

pencere = Tk()
tablo = ttk.Treeview(pencere)

tablo["columns"] = ("A","B")

tablo.column("#0",width = 150)
tablo.column("A",width = 150)
tablo.column("B",width = 100)

tablo.heading("#0",text = "Kayıt No")
tablo.heading("A",text = "Kitap Adı")
tablo.heading("B",text = "Yazarı")

tablo.insert("","end","Tarih",text = "Tarih")
tablo.insert("Tarih","end",text="001",values = ("Kitap3","Yazar3"))
tablo.insert("Tarih","end",text="002",values = ("Kitap4","Yazar4"))
tablo.insert("Tarih","end",text="003",values = ("Kitap4","Yazar4"))

tablo.insert("","end","Felsefe",text = "Felsefe")
tablo.insert("Felsefe","end",text="001",values = ("Kitap3","Yazar3"))
tablo.insert("Felsefe","end",text="002",values = ("Kitap4","Yazar4"))
tablo.insert("Felsefe","end",text="003",values = ("Kitap4","Yazar4"))


tablo.pack()
mainloop()
