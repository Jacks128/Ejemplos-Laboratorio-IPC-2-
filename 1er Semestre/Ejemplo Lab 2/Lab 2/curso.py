class Curso:
    nombre="IPC 2"
    duracion=100
    nota=61

    def __init__(self,catedratico):
        self.catedratico=catedratico
    
    def obtener_Nota(self):
        return self.nota    

class Lab(Curso):
    nombre="Lab de IPC2"
    duracion=100
    nota=100

class Practica(Curso): 
    nombre="Practica IPC2"
    duracion=30
    nota=61   
