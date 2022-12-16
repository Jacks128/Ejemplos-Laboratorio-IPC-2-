from Nodo_Encabezado import Nodo_Encabezado
from Lista_Encabezado import Lista_Encabezado
import os 

class Nodo_Interno():
    def __init__(self,x,y,caracter):
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
    
    def insert(self,pos_x,pos_y,caracter):
        nuevo= Nodo_Interno(pos_x,pos_y,caracter)
        nodo_X=self.filas.getEncabezado(pos_x)
        nodo_Y=self.columnas.getEncabezado(pos_y)

        if nodo_X==None:
            nodo_X=Nodo_Encabezado(pos_x)
            self.filas.insertar_nodoEncabezado(nodo_X)

        if nodo_Y==None:
            nodo_Y=Nodo_Encabezado(pos_y)
            self.columnas.insertar_nodoEncabezado(nodo_Y)

        #INSERTAR NUEVO EN LA FILA CUANDO YA EXISTEN NODOS EN ELLA

        if nodo_X.acceso==None:
            nodo_X.acceso=nuevo
        else:
            if nuevo.coordenadaY<nodo_X.acceso.coordenadaY:
                nuevo.derecha=nodo_X.acceso
                nodo_X.acceso.izquierda=nuevo
                nodo_X.acceso=nuevo
            else:
                tmp: Nodo_Interno=nodo_X.acceso
                while tmp!=None:
                    if nuevo.coordenadaY<tmp.coordenadaY:
                        nuevo.derecha=tmp
                        nuevo.izquierda=tmp.izquierda
                        tmp.izquierda.derecha=nuevo
                        tmp.izquierda=nuevo
                        break
                    elif nuevo.coordenadaX==tmp.coordenadaX and nuevo.coordenadaY==tmp.coordenadaY:
                        break
                    else:
                        if tmp.derecha==None:
                            tmp.derecha=nuevo
                            nuevo.izquierda=tmp
                            break
                        else:
                            tmp=tmp.derecha
        
        if nodo_Y.acceso==None:
            nodo_Y.acceso=nuevo
        else:
            if nuevo.coordenadaX < nodo_Y.acceso.coordenadaX:
                nuevo.abajo=nodo_X.acceso
                nodo_Y.acceso.arriba=nuevo
                nodo_Y.acceso=nuevo
            else:
                tmp2:Nodo_Interno=nodo_Y.acceso
                while tmp2!=None:
                    if nuevo.coordenadaX<tmp2.coordenadaX:
                        nuevo.abajo=tmp2
                        nuevo.arriba=tmp2.arriba
                        tmp2.arriba.abajo=nuevo
                        tmp2.arriba=nuevo
                        break
                    elif nuevo.coordenadaX==tmp2.coordenadaX and nuevo.coordenadaY==tmp2.coordenadaY:
                        break
                    else:
                        if tmp2.abajo==None:
                            tmp2.abajo=nuevo
                            nuevo.arriba=tmp2
                            break
                        else:
                            tmp2=tmp2.abajo



