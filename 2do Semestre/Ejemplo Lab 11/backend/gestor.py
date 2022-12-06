from cancion import Cancion
from usuario import Usuario
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.canciones=[]
        self.usuarios.append(Usuario('Jackeline','Benitez','admin','jacks128'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby123','kirby'))

    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:   
                return x
        return None

    
    def agregar_cancion(self,nombre,artista,imagen,album):
        nuevo=Cancion(nombre,artista,imagen,album)
        self.canciones.append(nuevo)
        return True

    def obtener_canciones(self):
        json=[]
        for i in self.canciones:
            cancion={
                'name':i.name,
                'artist':i.artist,
                'image':i.image,
                'album':i.album
            }
            json.append(cancion)
        return json

    def eliminar_cancion(self,n):
        for i in self.canciones:
            if i.name==n:
                tmp=i.getCancion()
                self.canciones.remove(tmp)
                return True
        return False

    def procesar_archivo(self,f):
        return {'Estado':'Procesado correctamente'}