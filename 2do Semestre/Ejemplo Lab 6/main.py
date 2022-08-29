from sre_parse import parse_template
from unicodedata import name
from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET
from colorama import Fore, Back, Style

def CargarArchivo(ruta,actores):
    tree=ET.parse(ruta)
    root=tree.getroot()
    for elemento in root:
        actores.crearActor(elemento.attrib['nombre'],elemento.attrib['edad'], elemento.attrib['nacionalidad'])
        print('Actor', elemento.attrib['nombre'],' ha sido insertado')
        for subelemento in elemento.iter('pelicula'):
            actor=actores.getActor(elemento.attrib['nombre'])
            actor.lista_peliculas.insertarPelicula(subelemento.attrib['nombre'],subelemento.attrib['papel'],subelemento.attrib['anio'],subelemento.text)
            print('La pelicula ',subelemento.attrib['nombre'],' es protagonizada por ',actor.nombre)

def menu():
    opcion=''
    Lista_Actores=ListaSimple()
    while opcion!='8':
        print(Fore.MAGENTA+'-------------Menu-------------')
        print(Fore.CYAN+'1. Ingresar actor')
        print(Fore.CYAN+'2. Ver Actores')
        print(Fore.CYAN+'3. Eliminar actor')
        print(Fore.CYAN+'4. Asignar Pelicula')
        print(Fore.CYAN+'5. Ver peliculas protagonizadas por Actores')
        print(Fore.CYAN+'6. Cargar Archivo')
        opcion=input(Fore.YELLOW+'Ingrese una opcion: ')
        print(opcion)

        if opcion=='1':
            c=input(Fore.BLUE+'Ingrese nombre de actor: ')
            n=input(Fore.BLUE+'Ingrese edad de Actor: ')
            o=input(Fore.BLUE+'Ingrese nacionalidad del Actor: ')
            Lista_Actores.crearActor(c,n,o)
        elif opcion=='2':
            print(Fore.GREEN+'-----------------A c t o r e s----------------', 'Total:',Lista_Actores.tam)
            Lista_Actores.mostrarActores()
            print(Fore.GREEN+'--------------------------------------------------------')
        elif opcion=='3':
            x=input(Fore.BLUE+'Ingrese nombre del actor que quiere eliminar')
            Lista_Actores.eliminarActor(x)
        elif opcion=='4':
            nombre=input(Fore.GREEN+'Ingresar nombre de Actor:')
            actor=Lista_Actores.getActor(nombre)
            if actor is None:
                print(Fore.RED+'> nombre incorrecto o no registrado')
            else:
                name=input(Fore.BLUE+'Ingrese nombre de Pelicula:')
                papel=input(Fore.BLUE+'Ingrese papel en la Pelicula:')
                anio=input(Fore.BLUE+'Ingrese año de la Pelicula:')
                dur=input(Fore.BLUE+'Ingrese duracion en minutos de la Pelicula:')
                actor.lista_peliculas.insertarPelicula(name,papel,anio,dur)
        elif opcion=='5':
            y=input(Fore.BLUE+'Ingrese nombre del actor: ' )
            actor=Lista_Actores.getActor(y)
            if actor is None:
                print(Fore.RED+'> nombre incorrecto o no registrado')
            else:
                print(Fore.GREEN+'Actor: ',actor.nombre)
                print(Fore.GREEN+'----------Peliculas---------')
                actor.lista_peliculas.mostrarPelicula()
        elif opcion=='6':
            Filename=input(Fore.BLUE+'Ingrese nombre de archivo: ')
            file='./'+Filename
            CargarArchivo(file, Lista_Actores)
        else:
            break

menu()
