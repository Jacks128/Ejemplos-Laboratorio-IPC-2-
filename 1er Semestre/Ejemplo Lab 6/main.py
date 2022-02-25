from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET
from colorama import Fore, Back, Style

def cargarArchivo(ruta,actores):
    tree=ET.parse(ruta)
    root=tree.getroot()
    for elemento in root:
        print('Actor ',elemento.attrib['nombre'], 'ha sido insertado. ')
        actores.crearActor(elemento.attrib['nombre'], elemento.attrib['edad'],elemento.attrib['nacionalidad']) #inserta al actor
        for subelemento in elemento.iter('pelicula'):
            actor=actores.getActor(elemento.attrib['nombre']) #se busca al actor
            actor.lista_peliculas.insertar(subelemento.attrib['nombre'],subelemento.attrib['papel'],subelemento.attrib['anio'],subelemento.text)
            print('La pelicula ',subelemento.attrib['nombre'], 'es protagonizada por ',actor.nombre)

def menu():
    opcion=''
    Lista_Actores=ListaSimple()
    while opcion!='8':
        print(Fore.CYAN+'----------- M E N U -----------')
        print(Fore.CYAN+'1. Ingresar actor')
        print(Fore.CYAN+'2. Ver actores favoritos')
        print(Fore.CYAN+'3. Eliminar actor')
        print(Fore.CYAN+'4. Asignar Pelicula')
        print(Fore.CYAN+'5. Ver peliculas protagonizadas de Actores')
        print(Fore.CYAN+'6. Cargar Archivo')
        opcion=input(Fore.YELLOW+'Ingrese una opcion')
        print(opcion)

        if opcion=='1':
            c=input(Fore.BLUE+'Ingrese nombre de Actor: ')
            n=input(Fore.BLUE+'Ingrese edad de Actor: ')
            o=input(Fore.BLUE+'Ingrese nacionalidad de Actor: ')
            Lista_Actores.crearActor(c,n,o)
        elif opcion=='2':
            print(Fore.GREEN+'---------- Actores Favoritos ----------', 'Total:',Lista_Actores.tam)
            Lista_Actores.mostrarActores()
            print(Fore.GREEN+'-------------------------------------------')
        elif opcion=='4':
            nombre = input(Fore.GREEN+'Ingresar nombre de Actor: ')
            actor = Lista_Actores.getActor(nombre)
            if actor is None: 
                print(Fore.RED+'> nombre incorrecto o no registrado')
            else: 
                name = input(Fore.BLUE+'Ingrese nombre de Pelicula:')
                papel = input(Fore.BLUE+'Ingrese papel de Actor:')
                anio = input(Fore.BLUE+'Ingrese anio de pelicula:')                
                min = input(Fore.BLUE+'Ingrese cantidad de minutos de pelicula:')
                actor.lista_peliculas.insertar(name,papel,anio,min)   
        elif opcion == '3':
            car = input(Fore.BLUE+'Ingrese nombre de actor a eliminar: ')            
            Lista_Actores.eliminarActor(car)
        elif opcion == '5':
            car = input(Fore.BLUE+'Ingrese nombre de actor: ')
            actor = Lista_Actores.getActor(car)
            if actor is None: 
                print(Fore.RED+'> Nombre incorrecto o no registrado')
            else:
                print(Fore.GREEN+'Actor:', actor.nombre)
                print(Fore.GREEN+'-------Peliculas-------')
                actor.lista_peliculas.mostrarPelicula()
        elif opcion == '6':
            Filename = input(Fore.BLUE+'Ingrese nombre de archivo:')
            file = './' + Filename
            cargarArchivo(file, Lista_Actores)
        else:
            break

menu()
             
