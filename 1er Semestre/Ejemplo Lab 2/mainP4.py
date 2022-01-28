import curso

print("-------Objeto Laboratorio-------")
laboratorio = curso.Lab(catedratico="Jacky")
print(laboratorio.nombre)    
print(laboratorio.duracion)    
print(laboratorio.catedratico) 
print(laboratorio.nota)


print("-------Objeto Practica-------")
practica = curso.Practica(catedratico="Pedro")
print("{} dura: {} minutos, la imparte {} y se debe aprobar con nota de {}".format(
    practica.nombre,
    practica.duracion,
    practica.catedratico,
    practica.nota
))
