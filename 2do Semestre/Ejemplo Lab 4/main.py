#Lista enlazada
#Una lista enlazada simple contiene dos valores-> el valor actual del nodo y un enlace al siguiente nodo
#Siempre el ultimo dato apuntara a nulo en este tipo de listas

from lista_simple import ListaSimple

lista=ListaSimple()

lista.agregarPrimero(771,'IPC2',4)
lista.agregarPrimero(800,'Lenguajes',5)
lista.agregarUltimo(200,"Orga",7)
lista.agregarUltimo(200,"Estructuras",7)

print('Imprimiendo recorrido')
lista.recorrido()