from ListaDoble import ListaDoble


class Actor: #Clase Nodo
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
        self.lista_peliculas=ListaDoble()
        self.siguiente = None
        
    def getPeliculas(self):
        return self.lista_peliculas   