
#Lista enlazada
#Una lista enlazada simple contiene dos valores-> el valor actual del nodo y un enlace al siguiente nodo
#Siempre el ultimo dato apuntara a nulo en este tipo de listas
from lista_simple import ListaSimple

lista=ListaSimple()

lista.agregarPrimero(771,'IPC2',5)
lista.agregarPrimero(800,'Lenguajes',5)
lista.agregarPrimero(200,'Orga',5)
lista.agregarUltimo(200,'Mate computo',5)

print("recorrido agregando primeros")
lista.recorrido()