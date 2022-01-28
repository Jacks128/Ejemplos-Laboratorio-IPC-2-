#PRIMERA PARTE
from curso import Curso
print("-------Clase deafult-------")
print(Curso.nombre)    
print(Curso.creditos)    
print(Curso.duracion)    
print(Curso.area)    

print("-------Objeto prerrequisito sin asignar nada-------")
prerequisito = Curso()
print(prerequisito.nombre)    
print(prerequisito.creditos)    
print(prerequisito.duracion)    
print(prerequisito.area)  

print("-------Objeto prerrequisito-------")
prerequisito.nombre="Mate Computo 1"
prerequisito.duracion=50
prerequisito.area="area de computacion"
prerequisito.nota=100

print(prerequisito.nombre)    
print(prerequisito.creditos)    
print(prerequisito.duracion)    
print(prerequisito.area) 

print("-------Objeto postrequisito-------")
postrequesito = Curso()
postrequesito.nombre="IO1"
postrequesito.creditos=5
postrequesito.duracion=50
postrequesito.area="area de metodologia de sistemas"

print(postrequesito.nombre)    
print(postrequesito.creditos)    
print(postrequesito.duracion)    
print(postrequesito.area)

#SEGUNDA PARTE poner prints en donde corresponda

print(postrequesito.obtener_Nota())
print(prerequisito.obtener_Nota())

#TERCERA ver otro main
