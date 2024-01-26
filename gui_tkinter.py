from tkinter import *
from tkinter.ttk import Button, Label, Frame

root = Tk()
frm = Frame(root, padding=10)
frm.grid()
titulo = Label(frm, text="Hola Mundo")
titulo.grid(column=0, row=0)
btn_cerrar = Button(frm, text= "Cerrar ventana", command = root.destroy)
btn_cerrar.grid(column=1,row=0)

root.mainloop()