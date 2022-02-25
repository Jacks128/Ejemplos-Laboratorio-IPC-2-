class Pelicula:
    def __init__(self, nombre, papel, anio, duracion):
        self.nombre=nombre
        self.papel=papel
        self.anio=anio
        self.duracion=duracion
        self.siguiente=None
        self.anterior=None