from Pelicula import Pelicula

class ListaDoble():
    def __init__(self):
        self.inicio=None
    
    def insertarPelicula(self,nombre,papel,anio,duracion):
        nuevo=Pelicula(nombre,papel,anio,duracion)
        if self.inicio is None:
            self.inicio=nuevo
        else:
            tmp=self.inicio
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nuevo
            nuevo.anterior=tmp

    def mostrarPelicula(self):
        tmp=self.inicio
        while tmp is not None:
            print('Nombre: ',tmp.nombre,' Papel ',tmp.papel,' Anio ',tmp.anio)
            tmp=tmp.siguiente