class Curso:
    nombre="IPC 2"
    duracion=100
    nota=61

  
#TERCERA PARTE -  init: metodo que absolutamente todas las clases en python. Se utiliza para definir 
#el comportamiento cuando se crea una instancia de una clase. EN ESTE PUNTO BORRAR ATRIBUTOS DE CLASS

    def __init__(self,catedratico):
        self.catedratico=catedratico



    def obtener_Nota(self):
        return self.nota   

class Lab(Curso):
    nombre="Laboratorio IPC 2"   
    duracion=140
    nota=80  


class Practica(Curso):
    nombre="Practica Computo 2"   
    duracion=30
    nota=61      
    
class TrabajoDirigido(Curso):
    nombre="Lab Quimica"   
    duracion=30
    nota=61      
        
      