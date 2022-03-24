from audioop import tomono
from Nodo_Encabezado import Nodo_Encabezado

class Lista_Encabezado():
    def __init__(self,tipo):
        self.primero:Nodo_Encabezado = None
        self.ultimo:Nodo_Encabezado = None
        self.tipo=tipo
        self.size=0

    def insertar_nodoEncabezado(self, nuevo):
        self.size +=1
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            if nuevo.id < self.primero.id:
                nuevo.siguiente=self.primero
                self.primero.anterior=nuevo
                self.primero=nuevo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente=nuevo
                nuevo.anterior=self.ultimo
                self.ultimo=nuevo
            else:
                tmp:Nodo_Encabezado = self.primero
                while tmp!=None:
                    if nuevo.id<tmp.id:
                        nuevo.siguiente=tmp
                        nuevo.anterior=tmp.anterior
                        tmp.anterior.siguiente=nuevo
                        tmp.anterior=nuevo
                        break
                    elif nuevo.id>tmp.id:
                        tmp=tmp.siguiente
                    else:
                        break

    def mostrarEncabezados(self):
        tmp=self.primero
        while tmp!=None:
            print('Encabezado ', self.tipo, tmp.id)
            tmp=tmp.siguiente

    def getEncabezado(self,id)->Nodo_Encabezado:
        tmp=self.primero
        while tmp!= None:
            if id==tmp.id:
                return tmp
            tmp=tmp.siguiente
        return None                
