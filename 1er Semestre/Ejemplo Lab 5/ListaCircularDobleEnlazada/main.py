from lista_circular_doble_enlazada import ListaCircularDobleEnlazada
lista=ListaCircularDobleEnlazada()

lista.agregarPrimero(12,'IPC2',5)
lista.agregarPrimero(13,'Lenguajes',5)
lista.agregarPrimero(14,'Orga',5)
lista.agregarPrimero(18,'Logica',5)
lista.agregarUltimo(15,'Deporte',5)
lista.agregarUltimo(16,'Quimica',5)
lista.agregarUltimo(17,'Fisica',5)

print("------DE FIN A INICIO ------")
lista.recorrer_fin_inicio()
print("------DE INICIO A FIN------")
lista.recorrer_inicio_fin()

print("Dato Encontrado: ", lista.buscar(20,'Fisica',5))

lista.eliminar_inicio()
lista.eliminar_ultimo()
print("------DE FIN A INICIO ------")
lista.recorrer_fin_inicio()
print("------DE INICIO A FIN------")
lista.recorrer_inicio_fin()

lista.crearReporte()