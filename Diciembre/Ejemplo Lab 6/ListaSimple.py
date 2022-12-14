from Actor import Actor

class ListaSimple():
    def __init__(self):
        self.inicio=None
        self.fin=None
        self.tam=0

    def crearActor(self, nombre, edad, nacionalidad):
        nuevo=Actor(self, nombre, edad, nacionalidad)
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
            print('Nombre: ',tmp.nombre,' Edad ',tmp.edad,' Nacionalidad ',tmp.nacionalidad)
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
                    nodo_borrar=tmp.siguiente
                    tmp.siguiente=nodo_borrar.siguiente
                    nodo_borrar.siguiente=None
                    print('Actor ',nombre,' fue eliminado')
                    break
            tmp=tmp.siguiente

