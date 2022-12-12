from persona import Persona

class ListaSimple():
    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def estaVacia(self):
        return self.primero==None

    def agregarPrimero(self, nombre, apellido, CUI, edad, estado_civil):
        nuevo=Persona(nombre,apellido,CUI,edad,estado_civil)
        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp


    def agregarUltimo(self, nombre, apellido, CUI, edad, estado_civil):
        nuevo=Persona(nombre,apellido,CUI,edad,estado_civil)

        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=self.primero
            while temp.siguiente is not None:
                temp=temp.siguiente
            temp.siguiente=nuevo


    def recorrido(self):
        temp=self.primero
        while temp!=None:
            print(temp.nombre, temp.apellido)
            temp=temp.siguiente