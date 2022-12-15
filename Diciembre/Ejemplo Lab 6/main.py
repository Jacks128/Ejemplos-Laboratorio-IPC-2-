from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET
from colorama import Fore, Back, Style

def cargaMasiva(ruta,actores):
    tree=ET.parse(ruta)
    root=tree.getroot()
    for elemento in root:
        actores.crearActor(elemento.attrib['nombre'],elemento.attrib['edad'],elemento.attrib['nacionalidad'])
        print('Actor ',elemento.attrib['nombre'],' ha sido insertado')
        for subelemento in elemento.iter('pelicula'):
            actor=actores.getActor(elemento.attrib['nombre'])
            actor.lista_peliculas.insertarPelicula(subelemento.attrib['nombre'],subelemento.attrib['papel'],subelemento.attrib['anio'],subelemento.text)
            print('La pelicula ',subelemento.attrib['nombre'],' es protagonizada por ',actor.nombre)
    
def menu():
    opcion=''
    lista_actores=ListaSimple()
    while opcion!='8':
        print(Fore.LIGHTMAGENTA_EX+'----------- M E N U -----------')
        print(Fore.CYAN+'1. Ingresar actor')
        print(Fore.CYAN+'2. Ver actores')
        print(Fore.CYAN+'3. Eliminar actor')
        print(Fore.CYAN+'4. Asignar pelicula')
        print(Fore.CYAN+'5. Ver peliculas protagonizados por x Actor')        
        print(Fore.CYAN+'6. Cargar archivo')
        opcion=input(Fore.YELLOW+'Ingresar una opcion:  ')
        print(Fore.CYAN+opcion)

        if opcion=='1':
            name=input(Fore.LIGHTGREEN_EX+'Ingrese el nombre del actor: ')
            age=input(Fore.LIGHTGREEN_EX+'Ingrese la edad del actor: ')
            country=input(Fore.LIGHTGREEN_EX+'Ingrese la nacionalidad del actor: ')
            lista_actores.crearActor(name,age,country)
        elif opcion=='2':
            print(Fore.MAGENTA+'------------ A C T O R E S ------------', 'Total: ',lista_actores.tam)
            lista_actores.mostrarActores()
            print(Fore.MAGENTA+'---------------------------------------')
        elif opcion=='3':
            x=input(Fore.LIGHTWHITE_EX+'Ingrese el nombre del actor que desea eliminar ')
            lista_actores.eliminarActor(x)
        elif opcion=='4':
            nombre=input(Fore.GREEN+'Ingrese nombre del Actor a quien pertenece la pelicula: ')
            actor=lista_actores.getActor(nombre)
            if actor is None:
                print(Fore.RED+'> nombre incorrecto o no existente')
            else:
                pelicula=input(Fore.LIGHTYELLOW_EX+'Ingresar nombre de la Pelicula: ')
                papel=input(Fore.LIGHTYELLOW_EX+'Ingresar papel del actor en la pelicula: ')
                anio=input(Fore.LIGHTYELLOW_EX+'Ingresar el anio de la Pelicula: ')
                tiempo=input(Fore.LIGHTYELLOW_EX+'Ingresar minutos que dura la Pelicula: ')
                actor.lista_peliculas.insertarPelicula(pelicula,papel,anio,tiempo)
        elif opcion=='5':
            actorcito=input(Fore.LIGHTRED_EX+'Ingresar nombre del actor: ')
            actor=lista_actores.getActor(actorcito)
            if actor is None:
                print(Fore.RED+'> nombre incorrecto o no existente')
            else:
                print(Fore.LIGHTGREEN_EX+'Actor: ',actor.nombre)
                print(Fore.LIGHTGREEN_EX+'--------- P E L I C U L A S ---------')
                actor.lista_peliculas.mostrarPelicula()
        elif opcion=='6':
            Filename=input(Fore.LIGHTBLACK_EX+'Ingrese el nombre del archivo: ')
            file='./'+Filename
            cargaMasiva(file, lista_actores)
        else:
            break

menu()
