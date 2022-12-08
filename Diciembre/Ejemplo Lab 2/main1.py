from curso1 import Curso
'''print("----Clase default----")
print(Curso.nombre)
print(Curso.area)
print(Curso.codigo)
print(Curso.creditos)
print(Curso.nota)
print(Curso.periodos)

print("----Objeto prerrequisito----")
prerrequisito=Curso()
print(prerrequisito.nombre)
print(prerrequisito.area)
print(prerrequisito.codigo)
print(prerrequisito.creditos)
print(prerrequisito.nota)
print(prerrequisito.periodos)

print("----Objeto prerrequisito IPC1----")

prerrequisito.nombre="IPC 1"
prerrequisito.area="desarrollo de software"
prerrequisito.codigo=770
prerrequisito.creditos=4
prerrequisito.nota=95
prerrequisito.periodos=10

print(prerrequisito.nombre)
print(prerrequisito.area)
print(prerrequisito.codigo)
print(prerrequisito.creditos)
print(prerrequisito.nota)
print(prerrequisito.periodos)

print("----Objeto postrequisito Compi 1----")

postrequisito=Curso()
postrequisito.nombre="Compiladores 1"
postrequisito.area="desarrollo de software"
postrequisito.codigo=777
postrequisito.creditos=4
postrequisito.nota=61
postrequisito.periodos=5

print(postrequisito.nombre)
print(postrequisito.area)
print(postrequisito.codigo)
print(postrequisito.creditos)
print(postrequisito.nota)
print(postrequisito.periodos)

print("----Notas----")
print(postrequisito.obtener_nota())
print(prerrequisito.obtener_nota())''' 

print("----Objeto prerrequisito----")
prerrequisito=Curso("Logica de Sistemas",2,1,795,100,"Metodologia de Sistemas")
prerrequisito.imprimir_datos()

print("----Objeto postrequisito----")
postrequisito=Curso("Orga",3,2,964,61,"Area de Computacion")
postrequisito.imprimir_datos()