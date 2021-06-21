from tkinter import *
from tkinter import simpledialog, messagebox
from Matrix import *



def iniciar_juego():
    root.withdraw()

    win = Toplevel()
    win.geometry('500x500')
    win.title("PANEL DE JUEGO")


def obtener_datos():
    root.withdraw()
    global P1Color,P2Color,Ftablero,Ctablero

    Ftablero = simpledialog.askstring("Input", "INGRESE EL NUMERO DE FILAS DE SU TABLERO", parent=root)
    Ctablero = simpledialog.askstring("Input", "INGRESE EL NUMERO DE COLUMNAS DE SU TABLERO", parent=root)
    lCabecera = listaCabecera()
    try:
        for i in range(int(Ctablero) + 1):
            lCabecera.insertar(NodoCabecera(i))
        for i in range(int(Ftablero) + 1):
            lCabecera.insertarY(NodoCabecera(i))

        p1 = simpledialog.askstring("Input", "JUGADOR1: INGRESE NOMBRE O ALIAS", parent=root)
        p2 = simpledialog.askstring("Input", "JUGADOR2: INGRESE NOMBRE O ALIAS", parent=root)

        win = Toplevel()
        win.geometry('380x300')
        win.title("Seleccion de colores")
        label1 = Label(win, text="BIENVENIDOS",bg="black",fg="white")
        label1.pack(fill=X)
        lblj1 = Label(win, text="JUGADOR 1",bg="black",fg="white")
        lblj2 = Label(win, text="JUGADOR 2",bg="black",fg="white")
        lblj1.place(x=30,y=70)
        lblj2.place(x=250, y=70)
        name1 = Label(win, text=str(p1))
        name2 = Label(win, text=str(p2))
        name1.place(x=30,y=100)
        name2.place(x=250, y=100)

        azul = Label(win, text="AZUL",bg="blue",fg="white")
        azul.place(x=120,y=120,width=60,height=60)
        rojo = Label(win, text="ROJO", bg="red", fg="white")
        rojo.place(x=180, y=120, width=60, height=60)
        amarillo = Label(win, text="AMARILLO", bg="yellow")
        amarillo.place(x=120, y=180, width=60, height=60)
        verde = Label(win, text="VERDE", bg="green")
        verde.place(x=180, y=180, width=60, height=60)
        P1Color = Entry(win)
        P1Color.place(x=20,y=180, width=80, height=60)
        P2Color = Entry(win)
        P2Color.place(x=260, y=180, width=80, height=60)
        continuar = Button(win, text="CONTINUAR", bg="black", fg="white", command=validar)
        continuar.place(x=135, y=250)
    except:
        messagebox.showwarning("ERROR", "NO INGRESO TAMAÑO DE TABLERO")


def validar():
    if P1Color.get() == P2Color.get():
        messagebox.showwarning("ERROR","LOS COLORES NO DEBEN DE SE IGUALES")
    else:
        iniciar_juego()

def cerrarVentana():
    pass

def abrir_partida():
    # Code to be written
    pass

def emptyfunc():
    # Code to be written
    pass

def guardar_partida():
    # Code to be written
    pass

def ayuda():
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
root.geometry("350x200")
root.config(background="green")

# Main Menu
mainmenu = Menu(root,background='#ff8000', foreground='black', activebackground='white', activeforeground='black')

# Menu 1
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Abrir partida", command=abrir_partida())
filemenu.add_command(label="Guardar partida", command=guardar_partida)
filemenu.add_separator()
filemenu.add_command(label="Ayuda", command=ayuda)
mainmenu.add_cascade(label="Menu", menu=filemenu)

# Menu 3
table = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Tablero", menu=table, command=tablero)

# Menu 4
reportes = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Reportes", menu=reportes, command=reporte)

# Menu 5
'''
panel = Menu(mainmenu, tearoff=0)
panel.add_command(label="Ingresar coordenadas", command=emptyfunc)
panel.add_command(label="Cantidad de puntos", command=emptyfunc)
panel.add_command(label="Pieza por colocar", command=emptyfunc)
panel.add_command(label="Cantidad de puntos", command=emptyfunc)
panel.add_command(label="Contador", command=emptyfunc)
panel.add_separator()
panel.add_command(label="Finalizar turno", command=fin_turno)
mainmenu.add_cascade(label="Panel", menu=panel)
'''

root.config(menu=mainmenu)

btnStart = Button(root, text="INICIAR PARTIDA",bg="black", fg="white", command=obtener_datos)
btnStart.place(x=120,y=30,width=110,height=80)



root.mainloop()