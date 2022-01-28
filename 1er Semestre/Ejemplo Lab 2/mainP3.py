from curso import Curso

print("-------Objeto prerrequisito-------")
prerequisito = Curso("IPC 1",4,100,"Area de desarrollo",61)
print(prerequisito.nombre)    
print(prerequisito.creditos)    
print(prerequisito.duracion)    
print(prerequisito.area) 
print(prerequisito.nota)


print("-------Objeto postrequesito-------")
postrequesito = Curso("Orga",3,100,"Area de computacion",0)
print(postrequesito.nombre)    
print(postrequesito.creditos)    
print(postrequesito.duracion)    
print(postrequesito.area) 
print(postrequesito.nota)