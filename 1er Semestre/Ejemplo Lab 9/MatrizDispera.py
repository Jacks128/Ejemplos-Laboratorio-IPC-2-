from Nodo_Encabezado import Nodo_Encabezado
from Lista_Encabezado import Lista_Encabezado

class Nodo_Interno():
    def __init__(self, x,y,caracter):
        self.caracter=caracter
        self.coordenadaX=x
        self.coordenadaY=y
        self.arriba=None
        self.abajo=None
        self.derecha=None
        self.izquierda=None

class MatrizDispersa():
    def __init__(self,capa):
        self.capa=capa
        self.filas=Lista_Encabezado('fila')
        self.columnas=Lista_Encabezado('columna')

# filas = x    columnas = y
    def insert(self, pos_x, pos_y, caracter):
        nuevo=Nodo_Interno(pos_x,pos_y,caracter)
        nodo_X=self.filas.getEncabezado(pos_x)
        nodo_Y=self.filas.getEncabezado(pos_y)

        if nodo_X==None:
            nodo_X=Nodo_Encabezado(pos_x)
            self.filas.insertar_nodoEncabezado(nodo_X)

        if nodo_Y==None:
            nodo_Y=Nodo_Encabezado(pos_y)
            self.columnas.insertar_nodoEncabezado(nodo_Y)

#INSERTAR FILA
        if nodo_X.acceso==None:
            nodo_X.acceso=nuevo   
        else:
            if nuevo.coordenadaY<nodo_X.acceso.coordenadaY:
                nuevo.derecha=nodo_X.acceso
                nodo_X.acceso.izquierda=nuevo
                nodo_X.acceso=nuevo
            else:
                tmp:Nodo_Interno=nodo_X.acceso
                while tmp!=None:
                    if nuevo.coordenadaY<tmp.coordenadaY:
                        nuevo.derecha=tmp
                        nuevo.izquierda=tmp.izquierda
                        tmp.izquierda.derecha =nuevo
                        tmp.izquierda=nuevo
                        break
                    elif nuevo.coordenadaY==tmp.coordenadaX and nuevo.coordenadaY==tmp.coordenadaY:
                        break
                    else:
                        if tmp.derecha==None:
                            tmp.derecha=nuevo
                            nuevo.izquierda=tmp
                            break
                        else:
                            tmp=tmp.derecha
                             #         nodo_Y:        C1    C3      C5      C6
                             # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5; NI 1,6;
                             # nodo_X:F2 --->      NI 2,2; NI 2,3; NI 2,5; NI 2,6;

#INSERTAR COLUMNA
