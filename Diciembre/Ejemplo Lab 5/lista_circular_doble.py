from ordenes import Ordenes

class ListaCircularDobleEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False

    def agregarPrimero(self, nombre, apellido, telefono, cantidad, tipo_postre, tiempo_prep, tiempo_desp):
        nuevo=Ordenes(nombre, apellido, telefono, cantidad, tipo_postre, tiempo_prep, tiempo_desp)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            tmp=nuevo
            tmp.siguiente=self.primero
            self.primero.anterior=tmp
            self.primero=tmp
        self.unir_nodos()

    def agregarUltimo(self, nombre, apellido, telefono, cantidad, tipo_postre, tiempo_prep, tiempo_desp):
        nuevo=Ordenes(nombre, apellido, telefono, cantidad, tipo_postre, tiempo_prep, tiempo_desp)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            tmp=self.ultimo
            self.ultimo=tmp.siguiente=nuevo
            self.ultimo.anterior=tmp
        self.unir_nodos()

    def unir_nodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero

    def eliminar_inicio(self):
        if self.estaVacia():
            print("La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
           self.primero=self.primero.siguiente 
        self.unir_nodos()
    
    def eliminar_ultimo(self):
        if self.estaVacia():
            print("La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            self.ultimo=self.ultimo.anterior
        self.unir_nodos()

    def recorrer_inicio_fin(self):
        tmp=self.primero
        while tmp:
            print(tmp.nombre, tmp.apellido, tmp.tipo_postre, tmp.cantidad, "--->")
            tmp=tmp.siguiente
            if tmp==self.primero:
                break

    def recorrer_fin_inicio(self):
        tmp=self.ultimo
        while tmp:
            print(tmp.nombre, tmp.apellido, tmp.tipo_postre, tmp.cantidad, "--->")
            tmp=tmp.anterior
            if tmp==self.ultimo:
                break

    def buscar(self,nombre,apellido):
        busqueda=Ordenes(nombre,apellido,0,0, 0, 0, 0)

        aux=self.primero
        while aux:
            if aux.nombre==busqueda.nombre and aux.apellido==busqueda.apellido:
                return True
            else:
                aux=aux.siguiente
                if aux==self.primero:
                    return False
