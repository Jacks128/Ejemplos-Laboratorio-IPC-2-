from cgi import print_environ
from curso import Curso

class ListaSimple():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        return self.primero==None

    def agregarPrimero(self,codigo,nombre,creditos):
        nuevo=Curso(codigo,nombre,creditos)

        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp

    def agregarUltimo(self,codigo,nombre,creditos):
        nuevo=Curso(codigo,nombre,creditos)

        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=self.primero
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevo    


    def recorrido(self):
        temp=self.primero
        while temp != None:
            print(temp.codigo,temp.nombre,temp.creditos)
            temp=temp.siguiente