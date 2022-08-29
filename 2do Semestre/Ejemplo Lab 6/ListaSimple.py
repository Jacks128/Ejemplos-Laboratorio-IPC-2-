from tkinter.messagebox import NO
from Actor import Actor

class ListaSimple():
    def __init__(self):
        self.inicio=None
        self.fin=None   
        self.tam=0

    def crearActor(self,nombre,edad,nacionalidad):
        nuevo=Actor(nombre,edad,nacionalidad)
        self.tam+=1
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo

    def mostrarActores(self):
        tmp=self.inicio
        while tmp is not None:
            print("Nombre: ",tmp.nombre,' Edad: ',tmp.edad,' Nacionalidad: ',tmp.nacionalidad)
            tmp=tmp.siguiente

    def eliminarActor(self,nombre):
        tmp=self.inicio
        while tmp is not None:
            if tmp.nombre==nombre:
                self.inicio=tmp.siguiente
                tmp.siguiente=None
                print('Actor ',tmp.nombre,' fue eliminado')
                break
            elif tmp.siguiente is not None:
                if tmp.siguiente.nombre==nombre:
                    nodo_a_borrar=tmp.siguiente
                    tmp.siguiente=nodo_a_borrar.siguiente
                    nodo_a_borrar.siguiente=None
                    print('Actor ',nombre,' fue eliminado')
                    break
            tmp=tmp.siguiente

    def getActor(self,nombre):
        tmp=self.inicio
        while tmp is not None:
            if tmp.nombre==nombre:
                return tmp
            tmp=tmp.siguiente
        return None