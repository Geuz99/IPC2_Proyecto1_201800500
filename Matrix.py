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
        dot = Digraph("Vertical")
        tod = Digraph("Horizontal")
        tod.attr(rank='same')
        aux = 0
        listaCabeceraY = listaCabeceraY.abajo
        while listaCabecera.next:
            if aux == 0:
                dot.node("x=" + str(listaCabecera.posX) + "\ny=" + str(listaCabeceraY.posY),
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

        c = 0
        Cdata = tempx.abajo
        while tempx:
            while Cdata:
                if c == 0:
                    dot.node(str(c), str(Cdata.data))
                    dot.edge("x=" + str(tempx.posX), str(c))
                    dot.edge(str(c), "x=" + str(tempx.posX))
                    c = 1
                    Cdata = Cdata.abajo
                else:
                    dot.node(str(c), str(Cdata.data))
                    Cdata = Cdata.abajo
                    c += 1
            Cdata = tempx.abajo
            c = 0
            while Cdata:
                if Cdata.abajo:
                    dot.edge(str(c), str(c + 1))
                    dot.edge(str(c + 1), str(c))
                    Cdata = Cdata.abajo
                    c += 1
                else:
                    Cdata = Cdata.abajo
                    continue

            tempx = tempx.next

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

    def graphviz_y(self, lista, posY):
        listaCabecera = lista.head
        dot = Digraph(comment='The Round Table')
        while listaCabecera.posY != int(posY):
            listaCabecera = listaCabecera.abajo
        dot.node("y=" + str(listaCabecera.posY), "y=" + str(posY))
        temp = listaCabecera.next
        c = 0
        while temp is not None:
            if c == 0:
                dot.node(str(c), str(temp.data))
                dot.edge("y=" + str(listaCabecera.posY), str(c))
                dot.edge(str(c), "y=" + str(listaCabecera.posY))
                c = 1
                temp = temp.next
            else:
                dot.node(str(c), str(temp.data))
                temp = temp.next
                c += 1
        c = 0
        temp = listaCabecera.next
        while temp is not None:
            if temp.next is not None:
                dot.edge(str(c), str(c + 1))
                dot.edge(str(c + 1), str(c))
                temp = temp.next
                c += 1
            else:
                temp = temp.next
                continue

        dot.render('pruebL0LY', view=True)

    def GG(self, lista):
        listaCabeceraX = lista.head
        graph = open("prueba.dot", "w")
        graph.write("digraph G {\n")
        graph.write("node [shape=box]")

        while listaCabeceraX.next is not None:
            temp = listaCabeceraX.abajo
            m = "x=" + str(temp)
            nfila = int(temp.posX)
            namex = "x" + str(temp.posX)
            m2 = namex + "[label=\"" + str(m) + "\"}\n"
            graph.write(m2)
            while temp is not None:
                namenode = "nodo" + str(temp.posX) + str(temp.posY)
                y = "\"" + str(temp.data) + "\""
                node = namenode + "[label=\"" + y + "]"
                graph.write(node + "\n")
                graph.write(namex + "->" + namenode + "\n")
                graph.write(namenode + "->" + namex + "\n")

                namex = namenode
                temp = temp.abajo
            if nfila > 1:
                graph.write("x" + str(nfila - 1) + "->" + "x" + str(nfila) + "\n")
                graph.write("x" + str(nfila) + "->" + "x" + str(nfila - 1) + "\n")
                graph.write('{rank="same";' + "x" + str(nfila - 1) + ";" + "x" + str(nfila) + "\n")

                listaCabeceraX = listaCabeceraX.next

            listaCabeceraY = lista.head
            while listaCabeceraY is not None:
                temp = listaCabeceraY.next
                ncolumna = "y" + str(temp.posY)
                rank = ncolumna + ";"
                while temp is not None:
                    nf = "nodo" + str(temp.posX) + str(temp.posY)
                    graph.write(ncolumna + "->" + nf + "\n")
                    graph.write(nf + "->" + ncolumna + "\n")
                    rank = rank + str(nf) + ";"
                    ncolumna = nf
                    temp = temp.next

                graph.write('{rank="same";' + rank + "}\n")

                listaCabeceraY = listaCabeceraY.abajo

            graph.write("}")
            graph.close()
            os.system('dot - Tpdf Grafica.dot -o Grafica.pdf')
            try:
                os.startfile("Grafica.pdf")
            except:
                print("algo paso")


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
