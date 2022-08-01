import curso
'''print("-------Clase default-------")
print(Curso.nombre)
print(Curso.duracion)
print(Curso.creditos)
print(Curso.area)

prerequisito = Curso()
print("-----Objeto prerrequisito sin asignar nada-----")
print(prerequisito.nombre)
print(prerequisito.creditos)
print(prerequisito.duracion)
print(prerequisito.area)

print("----Objeto prerrequisito---")
prerequisito.nombre="Mate Computo 1"
prerequisito.duracion=50
prerequisito.area="ciencias de la computacion"
prerequisito.creditos=5
prerequisito.nota=61

print(prerequisito.nombre)
print(prerequisito.creditos)
print(prerequisito.duracion)
print(prerequisito.area)

print("----Objeto postrequisito---")
postrequisito= Curso()
postrequisito.nombre="Organizacion Computacional"
postrequisito.creditos=3
postrequisito.duracion=100
postrequisito.area="ciencias de la computacion"

print(postrequisito.nombre)
print(postrequisito.creditos)
print(postrequisito.duracion)
print(postrequisito.area)

print("Notas de pre y post requisito")
print("prerequisito:")
print(prerequisito.obtener_Nota())
print("postrequisito:")
print(postrequisito.obtener_Nota())'''

'''print("----Objeto prerrequisito---")
prerequisito=Curso("IPC 1",4,100,"desarrollo de software",91)
print(prerequisito.nombre)
print(prerequisito.creditos)
print(prerequisito.duracion)
print(prerequisito.area)
print(prerequisito.nota)

print("----Objeto postrequisito---")
postrequisito=Curso("Estructuras de Datos",5,100,"desarrollo de software",0)
postrequisito.imprimir2()'''

print("----Objeto Laboratorio---")
laboratorio=curso.Lab(catedratico="Katherine")
laboratorio.imprimir3()

print("----Objeto Practica---")
practica=curso.Practica(catedratico="Jacky")
print(" La {} dura: {} minutos, la imparte {} y se debe aprobar con nota de {}".format(
    practica.nombre,
    practica.duracion,
    practica.catedratico,
    practica.nota
))

print(f" La {practica.nombre} dura: {practica.duracion} minutos, la imparte {practica.catedratico} y se debe aprobar con nota de {practica.nota}")



