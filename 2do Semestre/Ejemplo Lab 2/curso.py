class Curso:
    nombre="IPC 2"
    duracion=100
    nota=61

    '''def __init__(self,nombre,creditos,duracion,area,nota):
        self.nombre=nombre
        self.creditos=creditos
        self.duracion=duracion
        self.area=area
        self.nota=nota'''
    
    def __init__(self,catedratico):
        self.catedratico=catedratico

    def obtener_Nota(self):
        return self.nota

    def imprimir2(self):
        print(self.nombre)
        print(self.creditos)
        print(self.duracion)
        print(self.area)
        print(self.nota)

    def imprimir3(self):
        print(self.nombre)
        print(self.duracion)
        print(self.nota)
        print(self.catedratico)

    '''def imprimir_Atributos(self):
        return self.nombre, self.creditos, self.duracion, self.area, self.nota
'''

class Lab(Curso):
    nombre="Laboratorio IPC 2"
    duracion=140
    nota=80

class Practica(Curso):
    nombre="Practica IPC 2"
    duracion=30
    nota=61