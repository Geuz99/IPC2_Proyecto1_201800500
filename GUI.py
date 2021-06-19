from tkinter import *


def emptyfunc():
    # Code to be written
    pass

def abrir_partida():
    # Code to be written
    pass

def guardar_partida():
    # Code to be written
    pass

def ayuda():
    # Code to be written
    pass

def iniciar_juego():
    # Code to be written
    pass

def tablero():
    # Code to be written
    pass

def reporte():
    # Code to be written
    pass

def fin_turno():
    # Code to be written
    pass


root = Tk()
root.title("Ventana Principal")
root.iconbitmap('usacIcono.ico')
root.geometry("600x600")

# Main Menu
mainmenu = Menu(root)

# Menu 1
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Abrir partida", command=abrir_partida)
filemenu.add_command(label="Guardar partida", command=guardar_partida)
filemenu.add_separator()
filemenu.add_command(label="Ayuda", command=ayuda)
mainmenu.add_cascade(label="Menu", menu=filemenu)

# Menu 2
stargame = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Inicar Juego", menu=stargame, command=iniciar_juego)

# Menu 3
table = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Tablero", menu=table, command=tablero)

# Menu 4
reportes = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Reportes", menu=reportes, command=reporte)

# Menu 5
panel = Menu(mainmenu, tearoff=0)
panel.add_command(label="Ingresar coordenadas", command=emptyfunc)
panel.add_command(label="Cantidad de puntos", command=emptyfunc)
panel.add_command(label="Pieza por colocar", command=emptyfunc)
panel.add_command(label="Cantidad de puntos", command=emptyfunc)
panel.add_command(label="Contador", command=emptyfunc)
panel.add_separator()
panel.add_command(label="Finalizar turno", command=fin_turno)
mainmenu.add_cascade(label="Panel", menu=panel)

root.config(menu=mainmenu)
root.mainloop()