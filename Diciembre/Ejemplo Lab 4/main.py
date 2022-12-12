from lista_simple import ListaSimple

lista=ListaSimple()
listaCola=ListaSimple()

lista.agregarPrimero('1000','Quetzales',65451561651,25,'soltera') #primer lugar
lista.agregarPrimero('TV','Plasma',3216546516,23,'soltera')       #segundo lugar  
lista.agregarPrimero('Vale 500','en la MP',455316413,50,'casada') #tercer lugar

print('Lista con comportamiento de pila')
lista.recorrido()
listaCola.agregarPrimero('Diego','Ozuna',65451561651,25,'soltera') #primero en llegar=
listaCola.agregarUltimo('Diego','Mendoza',65451561651,25,'soltera') #primero en llegar
listaCola.agregarUltimo('Juan','Perez',3216546516,23,'soltera')       #segundo en llegar  
listaCola.agregarUltimo('Patricia','Fernandez',455316413,50,'casada') #tercero en llegar

print('Lista con comportamiento de cola')
listaCola.recorrido()