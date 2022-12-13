class Ordenes():
    def __init__(self, nombre, apellido, telefono, cantidad, tipo_postre, tiempo_prep, tiempo_desp):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.cantidad=cantidad
        self.tipo_postre=tipo_postre
        self.tiempo_prep=tiempo_prep
        self.tiempo_desp=tiempo_desp
        self.siguiente=None
        self.anterior=None