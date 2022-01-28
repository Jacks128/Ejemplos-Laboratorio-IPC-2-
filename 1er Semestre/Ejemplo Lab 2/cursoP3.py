class Curso:

  
#TERCERA PARTE -  init: metodo que absolutamente todas las clases en python. Se utiliza para definir 
#el comportamiento cuando se crea una instancia de una clase. 

    def __init__(self,nombre,creditos,duracion,area,nota):
        self.nombre=nombre
        self.creditos=creditos
        self.duracion=duracion
        self.area=area
        self.nota=nota


    def obtener_Nota(self):
        return self.nota   