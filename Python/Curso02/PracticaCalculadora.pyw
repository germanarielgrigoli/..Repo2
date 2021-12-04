import tkinter as tk
ventana=tk.Tk()

lista = tk.Listbox()
lista.insert(0, "Python", "C", "C++", "Java")
lista.place(x=10, y=10, height=100)
def imprimir_seleccion():
    print(lista.get(lista.curselection()))
boton = tk.Button(text="Imprimir seleccion", 
command=imprimir_seleccion)
boton.place(x=10, y=130)

ventana.mainloop()