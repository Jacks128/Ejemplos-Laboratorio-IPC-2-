from usuario import Usuario
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.usuarios.append(Usuario('Jacky','Benitez','admin','admin'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby','kirby'))
    
    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None
