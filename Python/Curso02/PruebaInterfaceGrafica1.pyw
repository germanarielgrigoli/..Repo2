from tkinter import *
raiz = Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(True,True)
#raiz.geometry("650x350")
raiz.config(bg="blue")
raiz.iconbitmap("appicon.ico")
raiz.config(bd="35")
raiz.config(relief="groove")
raiz.config(cursor="hand2")
miFrame=Frame()
#miFrame=Frame(fill="y",expand="true")
#miFrame=Frame(fill="both",expand="true")
miFrame.pack(side="bottom", anchor="e")
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd="35")
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")
raiz.mainloop()
