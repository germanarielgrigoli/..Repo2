from tkinter import *
raiz=Tk()
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

cuadroTexto=Entry(miFrame, textvariable=minombre)
cuadroTexto.grid(row=0,column=1)
cuadroTexto.config(justify="center")

nombreTexto=Entry(miFrame)
nombreTexto.grid(row=1,column=1)
nombreTexto.config(show="*")

apellidoTexto=Entry(miFrame)
apellidoTexto.grid(row=2,column=1)

cajaTexto=Text(miFrame, width=20, height=5)
cajaTexto.grid(row=3,column=1, padx=10, pady=5)


scrollVert=Scrollbar(miFrame,command=cajaTexto.yview)
scrollVert.grid(row=3,column=2,sticky="nsew")

cajaTexto.config(yscrollcommand=scrollVert.set)

#cuadroTexto.place(x=100,y=100)
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=5)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0, sticky="e", padx=10, pady=5)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=2,column=0, sticky="e", padx=10, pady=5)
#nombreLabel.place(x=100,y=100)

cajaLabel=Label(miFrame,text="comentarios:")
cajaLabel.grid(row=3,column=0, sticky="e", padx=10, pady=5)

def codigoBoton():
	minombre.set("German")

botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()