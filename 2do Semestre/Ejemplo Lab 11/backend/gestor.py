from cancion import Cancion
from usuario import Usuario
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.canciones=[]
        self.usuarios.append(Usuario('Jackeline','Benitez','admin','jacks128'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby123','kirby'))

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None
    
    '''agregar_cancion(self,Neverita,Bad Bunny,www.neverita.com,Un Verano Sin Ti)'''
    def agregar_cancion(self,nombre,artista,imagen,album):
        nuevo=Cancion(nombre,artista,imagen,album)
        self.canciones.append(nuevo)
        return True
