import os

from graphviz import Digraph


class NodoCabecera:
    def __init__(self, data):
        self.posX = data
        self.posY = data
        self.next = None
        self.abajo = None


class NodoLista:
    def __init__(self, data):
        self.data = data
        self.abajo = None
        self.next = None


class listaCabecera:
    def __init__(self):
        self.head = None
        self.next = None
        self.abajo = None

    def insertar(self, nuevoNodo):
        if self.head:
            ultimo = self.head
            while ultimo.next != None:
                ultimo = ultimo.next

            ultimo.next = nuevoNodo
        else:
            self.head = nuevoNodo

        print('x')

    def insertarY(self, nuevoNodo):
        if self.head:
            ultimo = self.head
            while ultimo.abajo != None:
                ultimo = ultimo.abajo

            ultimo.abajo = nuevoNodo
        else:
            self.head = nuevoNodo

        print('y')

    def mostrar(self):
        temp = self.head
        while temp != None:
            print(temp.posX, end='->')
            temp = temp.next

        print('Null')

    def mostrarY(self):
        temp = self.head
        aux = temp.abajo
        while aux != None:
            print(aux.posY, end='->')
            aux = aux.abajo

        print('Null')


class listaEnLista:
    def __init__(self):
        self.head = None
        self.abajo = None
        self.next = None

    def insertar(self, posX, posY, lista, nuevoNodo):
        lTemporal = lista.head
        lTemporalY = lista.head

        while lTemporal.posX != int(posX):
            lTemporal = lTemporal.next

        while lTemporalY.posY != int(posY):
            lTemporalY = lTemporalY.abajo

        listaX = lTemporal
        listaY = lTemporalY

        while listaX.abajo != None:
            listaX = listaX.abajo

        while listaY.next != None:
            listaY = listaY.next

        if listaX:
            tempUltimo = listaX
            while tempUltimo.abajo != None:
                tempUltimo = tempUltimo.abajo

            tempUltimo.abajo = nuevoNodo
        else:
            listaX = nuevoNodo
            listaX.abajo = nuevoNodo

        print(':)')

        if listaY:
            tempUltimo = listaY
            while tempUltimo.next != None:
                tempUltimo = tempUltimo.next

            tempUltimo.next = nuevoNodo
        else:
            listaY = nuevoNodo
            listaY.next = nuevoNodo

    def mostrar(self, lista, posX):
        listaCabecera = lista.head
        while listaCabecera.posX != int(posX):
            listaCabecera = listaCabecera.next

        print('La cabecera X es ', listaCabecera.posX)
        temp = listaCabecera.abajo
        while temp != None:
            print(temp.data, end='->')
            temp = temp.abajo

        print('Null')

    def mostrarY(self, lista, posY):
        listaCabecera = lista.head
        while listaCabecera.posY != int(posY):
            listaCabecera = listaCabecera.abajo

        print('La cabecera Y es ', listaCabecera.posY)
        temp = listaCabecera.next
        while temp != None:
            print(temp.data, end='->')
            temp = temp.next

        print('Null')

    def graphviz_matrix(self, lista):
        listaCabecera = lista.head
        listaCabeceraY = lista.head
        tempx = listaCabecera.next
        tempxx = listaCabecera.next
        dot = Digraph("Vertical")
        tod = Digraph("Horizontal")
        tod.attr(rank='same')
        aux = 0
        listaCabeceraY = listaCabeceraY.abajo
        tempy = listaCabeceraY.abajo
        tempyy = listaCabeceraY.abajo

        while listaCabecera.next:
            if aux == 0:
                tod.node("x=" + str(listaCabecera.posX) + "\ny=" + str(listaCabeceraY.posY),
                         "x=" + str(listaCabecera.posX) + "\ny=" + str(listaCabeceraY.posY))
                tod.node("x=" + str(listaCabecera.next.posX), "x=" + str(listaCabecera.next.posX))
                tod.edge("x=" + str(listaCabecera.posX) + "\ny=" + str(listaCabeceraY.posY),
                         "x=" + str(listaCabecera.next.posX))
                listaCabecera = listaCabecera.next
                aux = 1
            else:
                tod.node("x=" + str(listaCabecera.posX), "x=" + str(listaCabecera.posX))
                tod.node("x=" + str(listaCabecera.next.posX), "x=" + str(listaCabecera.next.posX))
                tod.edge("x=" + str(listaCabecera.posX), "x=" + str(listaCabecera.next.posX))
                listaCabecera = listaCabecera.next
        aux = 0
        while listaCabeceraY.abajo:
            if aux == 0:
                dot.node("y=" + str(listaCabeceraY.abajo.posY), "y=" + str(listaCabeceraY.abajo.posY))
                dot.edge("x=" + str(0) + "\ny=" + str(listaCabeceraY.posY),
                         "y=" + str(listaCabeceraY.abajo.posY))
                listaCabeceraY = listaCabeceraY.abajo
                aux = 1
            else:
                dot.node("y=" + str(listaCabeceraY.posY), "y=" + str(listaCabeceraY.posY))
                dot.node("y=" + str(listaCabeceraY.abajo.posY), "y=" + str(listaCabeceraY.abajo.posY))
                dot.edge("y=" + str(listaCabeceraY.posY), "y=" + str(listaCabeceraY.abajo.posY))
                listaCabeceraY = listaCabeceraY.abajo

        while tempx:
            aux = 0
            Cdata = tempx.abajo
            while Cdata:
                if aux == 0:
                    dot.node("x" + str(tempx.posX) + "y" + str(tempy.posY), str(Cdata.data))
                    dot.edge("x=" + str(tempx.posX), "x" + str(tempx.posX) + "y" + str(tempy.posY))
                    dot.edge("x" + str(tempx.posX) + "y" + str(tempy.posY), "x=" + str(tempx.posX))
                    if Cdata.abajo:
                        dot.edge("x" + str(tempx.posX) + "y" + str(tempy.posY),
                                 "x" + str(tempx.posX) + "y" + str(tempy.abajo.posY))
                        dot.edge("x" + str(tempx.posX) + "y" + str(tempy.abajo.posY),
                                 "x" + str(tempx.posX) + "y" + str(tempy.posY))
                    aux = 1
                    Cdata = Cdata.abajo
                    tempy = tempy.abajo
                else:
                    dot.node("x" + str(tempx.posX) + "y" + str(tempy.posY), str(Cdata.data))
                    if Cdata.abajo:
                        dot.node("x" + str(tempx.posX) + "y" + str(tempy.abajo.posY), str(Cdata.abajo.data))
                        dot.edge("x" + str(tempx.posX) + "y" + str(tempy.abajo.posY),
                                 "x" + str(tempx.posX) + "y" + str(tempy.posY))
                        dot.edge("x" + str(tempx.posX) + "y" + str(tempy.posY),
                                 "x" + str(tempx.posX) + "y" + str(tempy.abajo.posY))
                    Cdata = Cdata.abajo
                    tempy = tempy.abajo
            tempx = tempx.next

        while tempyy:
            aux = 0
            Fdata = tempyy.next
            while Fdata:
                if aux == 0:
                    tod.node("x" + str(tempxx.posX) + "y" + str(tempyy.posY), str(Fdata.data))
                    tod.edge("y=" + str(tempyy.posY), "x" + str(tempxx.posX) + "y" + str(tempyy.posY))
                    tod.edge("x" + str(tempxx.posX) + "y" + str(tempyy.posY), "y=" + str(tempyy.posY))
                    if Fdata.next:
                        tod.edge("x" + str(tempxx.posX) + "y" + str(tempyy.posY),
                                 "x" + str(tempxx.next.posX) + "y" + str(tempyy.posY))
                        tod.edge("x" + str(tempxx.next.posX) + "y" + str(tempyy.posY),
                                 "x" + str(tempxx.posX) + "y" + str(tempyy.posY))
                    aux = 1
                    Fdata = Fdata.next
                    tempxx = tempxx.next
                else:
                    dot.node("x" + str(tempxx.posX) + "y" + str(tempyy.posY), str(Fdata.data))
                    if Fdata.next:
                        dot.node("x" + str(tempxx.next.posX) + "y" + str(tempyy.posY), str(Fdata.next.data))
                        tod.edge("x" + str(tempxx.next.posX) + "y" + str(tempyy.posY),
                                 "x" + str(tempxx.posX) + "y" + str(tempyy.posY))
                        tod.edge("x" + str(tempxx.posX) + "y" + str(tempyy.posY),
                                 "x" + str(tempxx.next.posX) + "y" + str(tempyy.posY))
                    Fdata = Fdata.next
                    tempxx = tempxx.next

            tempyy = tempyy.abajo

        dot.subgraph(tod)
        dot.render('matrixxx', view=True)

    def graphviz_x(self, lista, posX):
        listaCabecera = lista.head
        dot = Digraph(comment='The Round Table')
        while listaCabecera.posX != int(posX):
            listaCabecera = listaCabecera.next
        dot.node("x=" + str(listaCabecera.posX), "x=" + str(posX))
        temp = listaCabecera.abajo
        c = 0
        while temp is not None:
            if c == 0:
                dot.node(str(c), str(temp.data))
                dot.edge("x=" + str(listaCabecera.posX), str(c))
                dot.edge(str(c), "x=" + str(listaCabecera.posX))
                c = 1
                temp = temp.abajo
            else:
                dot.node(str(c), str(temp.data))
                temp = temp.abajo
                c += 1
        c = 0
        temp = listaCabecera.abajo
        while temp is not None:
            if temp.abajo is not None:
                dot.edge(str(c), str(c + 1))
                dot.edge(str(c + 1), str(c))
                temp = temp.abajo
                c += 1
            else:
                temp = temp.abajo
                continue

        dot.render('pruebL0LX', view=True)


def main():
    lCabecera = listaCabecera()
    lLista = listaEnLista()
    opcion = -1

    cantidadCabecera = input('Cantidad de nodos cabecera en x: ')
    for i in range(int(cantidadCabecera) + 1):
        lCabecera.insertar(NodoCabecera(i))
    cantidadCabeceraY = input('Cantidad de nodos cabecera en y: ')
    for i in range(int(cantidadCabeceraY) + 1):
        lCabecera.insertarY(NodoCabecera(i))
    lCabecera.mostrar()
    lCabecera.mostrarY()

    while opcion != 0:
        opcion = int(input('ingrese'))
        if opcion == 1:
            posX = input("Ingresar valor de la posición X: ")
            posY = input("Ingresar valor de la posición Y: ")
            val = input('Ingresar valor para guardar: ')
            lLista.insertar(posX, posY, lCabecera, NodoLista(val))

        #   impX = input("Ingrese el valor para imprimir de la posicion X: ")
        #   impY = input("Ingrese el valor para imprimir de la posicion Y: ")
        #   lLista.mostrar(lCabecera, impX)
        #   lLista.mostrarY(lCabecera, impY)

        if opcion == 2:
            lLista.graphviz_matrix(lCabecera)


def imprimirCabeceras(lista, lCabecera):
    # impX = input("Ingrese el valor para imprimir de la posicion X: ")
    # impY = input("Ingrese el valor para imprimir de la posicion Y: ")
    lista.printMatrix(lCabecera)


# lista.mostrar(lCabecera, impX)
# lista.mostrarY(lCabecera, impY)
# lista.graphviz_x(lCabecera, impX)
# lista.graphviz_y(lCabecera, impY)


main()

