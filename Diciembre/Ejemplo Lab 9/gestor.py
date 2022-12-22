from usuario import Usuario
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.usuarios.append(Usuario('Jackeline','Benitez','admin','admin'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby123','kirby'))
        self.usuarios.append(Usuario('Pedro','Coral','pedrito123','pedroElEscamoso'))

#                             admin,admin
    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None
