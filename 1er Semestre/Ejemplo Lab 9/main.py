from MatrizDispera import MatrizDispersa

matriz =MatrizDispersa(0)

def insertaTodo():
    with open('Figura3.txt') as archivo:
        l=0
        c=0
        lineas=archivo.readlines()
        for linea in lineas:
            columnas=linea
            l+=1
            for col in columnas:
                if col != '\n':
                    c+=1
                    matriz.insert(l,c,col)
            c=0
            matriz.graficarDibujo('toad')

def insertaSeleccion():
    with open('Figura3.txt') as archivo:
        l=0
        c=0
        lineas=archivo.readlines()
        for linea in lineas:
            columnas=linea
            l+=1
            for col in columnas:
                if col != '\n':
                    c+=1
                    if col=='*':
                        matriz.insert(l,c,col)
            c=0
            matriz.graficarDibujo('toad')
insertaTodo()
#insertaSeleccion()