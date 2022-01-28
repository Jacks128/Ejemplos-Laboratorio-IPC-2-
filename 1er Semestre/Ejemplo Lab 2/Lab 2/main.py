import curso
'''
print("-----Clase default-----")
print(Curso.nombre)
print(Curso.creditos)
print(Curso.duracion)
print(Curso.area)

print("-----Objeto prerrequisito-----")
prerrequisito=Curso()
prerrequisito.nombre="Mate Computo 1"
prerrequisito.duracion=50
prerrequisito.area="area de computacion"
prerrequisito.creditos=5
prerrequisito.nota=85
''' 
'''print(prerrequisito.nombre)    
print(prerrequisito.creditos)    
print(prerrequisito.duracion)    
print(prerrequisito.area) '''

'''print("-----Objeto postrequisito-----")
postrequisito=Curso()
postrequisito.nombre="IO 1"
postrequisito.duracion=50
postrequisito.area="area de metodologia sistemas"
postrequisito.creditos=5

print(postrequisito.nombre)    
print(postrequisito.creditos)    
print(postrequisito.duracion)    
print(postrequisito.area) 

print("-----Nota prerrequisito-----")
print(prerrequisito.obtener_Nota())'''

'''prerrequisito=Curso("IPC 1",4,100,"Area de desarrollo",70)
print("-----Objeto prerrequisito-----")
print(prerrequisito.nombre)    
print(prerrequisito.creditos)    
print(prerrequisito.duracion)    
print(prerrequisito.area)

postrequisito=Curso("Orga",3,100,"Area de computacion",0)
print("-----Objeto postrequisito-----")
print(postrequisito.nombre)    
print(postrequisito.creditos)    
print(postrequisito.duracion)    
print(postrequisito.area) '''

print("-------Objeto Laboratorio-------")
laboratorio=curso.Lab("Jacky")
print(laboratorio.nombre)    
print(laboratorio.duracion)    
print(laboratorio.catedratico) 
print(laboratorio.nota)

print("-------Objeto Practica-------")
practica=curso.Practica(catedratico="Byron")
print(" {} dura: {} minutos, la imparte {} y se debe aprobar con nota de {} ".format(
    practica.nombre,
    practica.duracion,
    practica.catedratico,
    practica.nota
))
