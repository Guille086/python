from tkinter import *

class Ventana():
    def __init__(self):
        self.ventana = Tk()
        self.dato_campo = StringVar()
        self.ventana.geometry("550x200+100+100")
        self.ventana.title("Cargar localidades")
        Label(self.ventana, text = 'Localidad').grid(pady=10, row=0, column=0)
        self.nombre_localidad = Entry(self.ventana, textvariable=self.dato_campo, width=50).grid(padx=10, row=0, column=1)
        Button(self.ventana, text='Guardar', width=10, command=self.cargar_lista).grid(pady=10, row=0, column=2)
        Label(self.ventana, text="Lista de localidades").grid(pady=10, row=1, column=0)
        self.tabla = Tabla(self.ventana)
    def mostrar(self):
        self.ventana.mainloop()
    
    def cargar_lista(self):
        localidad = self.dato_campo.get()
        self.tabla.cargar_tabla(localidad)

    def get_ventana_localidad(self):
        return self.dato_campo.get()
    
class Tabla():
    tabla = None
    ventana = None

    def __init__(self, ventana):
        self.tabla = Entry(ventana)
        self.ventana = ventana
        self.num_fila = 1
    
    def cargar_tabla(self, localidad):
        if localidad != "":
            self.tabla = Entry(self.ventana, width=20, fg='black', font=('Arial',10,'bold'))
            self.tabla.grid(row=self.num_fila, column=1)
            lista = [self.num_fila,localidad]
            self.tabla.insert(END, lista)
            self.num_fila += 1
        else:
            return self.ventana
    


if __name__ == "__main__":
    ventana_localidad = Ventana()
    ventana_localidad.mostrar()