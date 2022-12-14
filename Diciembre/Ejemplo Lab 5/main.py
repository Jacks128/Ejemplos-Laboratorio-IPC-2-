from lista_circular_doble import ListaCircularDobleEnlazada

lista=ListaCircularDobleEnlazada()
listaCola=ListaCircularDobleEnlazada()

lista.agregarPrimero("Jacky","Benitez",56919369,2,"Galletas Jengibre","30 m","2 h")
lista.agregarPrimero("Jeny","Perez",5432123,4,"Pastel Danes","30 m","2 h")
lista.agregarPrimero("Kirby","Star",2654612,3,"Pastel de Frutas","30 m","2 h")
lista.agregarPrimero("Antonio","Gonzalez",54114124,1,"Galletas Jengibre","30 m","2 h")

print("-----------Recorrido de Inicio a Fin------------")
lista.recorrer_inicio_fin()
print("-----------Recorrido de Fin a Inicio------------")
lista.recorrer_fin_inicio()

listaCola.agregarUltimo("Spider","man",56919369,2,"Galletas Jengibre","30 m","2 h")
listaCola.agregarUltimo("Iron","man",5432123,4,"Pastel Danes","30 m","2 h")
listaCola.agregarUltimo("Hulk"," ",2654612,3,"Pastel de Frutas","30 m","2 h")
listaCola.agregarUltimo("Capitan ","America",54114124,1,"Galletas Jengibre","30 m","2 h")

print("-----------Recorrido de Inicio a Fin------------")
listaCola.recorrer_inicio_fin()
print("-----------Recorrido de Fin a Inicio------------")
listaCola.recorrer_fin_inicio()
print("Orden encontrada: ",listaCola.buscar("Spider","man"))

listaCola.eliminar_inicio()
listaCola.eliminar_ultimo()

print("-----------Recorrido de Inicio a Fin Despues de Eliminar------------")
listaCola.recorrer_inicio_fin()

print("Orden encontrada: ",listaCola.buscar("Spider","man"))

lista.crearReporte()