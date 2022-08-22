from lista_circular_doble import ListaCircularDoble

lista=ListaCircularDoble()

lista.agregar_inicio(771,'IPC 2',4)
lista.agregar_inicio(2009,'Practicas Finales',0)
lista.agregar_inicio(1,'Logica',1)
lista.agregar_final(200,'Mate Aplicada 3',5)
lista.agregar_final(201,'Mate Aplicada 5',5)

'''lista.eliminar_final()
lista.eliminar_inicio()'''

print('inicio - final')
lista.recorrer_inicio_fin()

print('final - inicio')
lista.recorrer_fin_inicio()

print("Datos encontrado", lista.buscar(771,'55555',4))

lista.crearReporte()