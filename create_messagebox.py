from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.geometry("500x500")
pencere.title("Halil İbrahim BERK <> Python Tkinter")
pencere.config(bg="brown")

messagebox.showinfo("Bilgi","Bu Bir bilgi mesajıdır.")

messagebox.showerror("Hata","Yanlış Giriş")

messagebox.showwarning("Uyarı","Bu bir Uyarı mesajıdır.")

messagebox.askquestion("Soru","Gerçekten çıkmak istiyor musunuz?")

messagebox.askokcancel()

messagebox.askretrycancel()

messagebox.askyesno()

messagebox.askyesnocancel()

mainloop()