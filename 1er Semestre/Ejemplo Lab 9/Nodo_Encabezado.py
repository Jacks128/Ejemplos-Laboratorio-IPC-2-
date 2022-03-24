class Nodo_Encabezado():
    def __init__(self,id):
        self.id:int = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None 