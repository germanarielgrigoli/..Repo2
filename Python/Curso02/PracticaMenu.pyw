import tkinter as tk
from tkinter import *
from tkinter import messagebox

def nuevo():
 print("Nuevo archivo.")
def acerca_de():
 print("Acerca de:")
ventana_principal = tk.Tk()
ventana_principal.title("Mi primera aplicación")

barra_de_menu = tk.Menu()

menu_archivo = tk.Menu(barra_de_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_ayuda = tk.Menu(barra_de_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)
barra_de_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_de_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
ventana_principal.config(width=300, height=200, menu=barra_de_menu)

# Siempre retornan la cadena "ok".

messagebox.showinfo(title="Información", message="Hola mundo")
messagebox.showwarning(title="Advertencia", message="Hola mundo")
messagebox.showerror(title="¡Error!", message="Hola mundo")
# Retornan True o False.
messagebox.askokcancel(title="Pregunta", message="¿Desea salir?")
messagebox.askyesno(title="Pregunta", message="¿Desea salir?")
messagebox.askretrycancel(title="Operación fallida", message="¿Qué desea hacer?")
ventana_principal.mainloop()