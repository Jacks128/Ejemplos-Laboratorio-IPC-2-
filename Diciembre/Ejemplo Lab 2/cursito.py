class Curso:
    nombre="IPC 2"
    periodos=5
    nota=90

    def __init__(self,catedratico):
        self.catedratico=catedratico

    def imprimir_datos(self):
        print("La {} tiene {} periodos a la semana, lo imparte {} y se debe aprobar con la nota de {}".format(
            self.nombre,
            self.periodos,
            self.catedratico,
            self.nota
        ))

class Lab(Curso):
    nombre="Laboratorio de IPC 2"
    periodos=5
    nota=100

class TrabajoDirigido(Curso):
    nombre="Trabajo Dirigido IPC2"
    periodos=1
    nota=70

class Practica(Curso):
    nombre="Practica Computo 2"
    periodos=2
    nota=80


