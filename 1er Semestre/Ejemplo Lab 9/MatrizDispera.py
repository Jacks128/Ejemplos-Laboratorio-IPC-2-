from Nodo_Encabezado import Nodo_Encabezado
from Lista_Encabezado import Lista_Encabezado
import os
import webbrowser

class Nodo_Interno(): 
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.coordenadaX = x 
        self.coordenadaY = y  
        self.arriba = None
        self.abajo = None
        self.derecha = None  
        self.izquierda = None  


class MatrizDispersa():
    def __init__(self, capa):
        self.capa = capa
        self.filas = Lista_Encabezado('fila')
        self.columnas = Lista_Encabezado('columna')

    def insert(self, pos_x, pos_y, caracter):
        nuevo = Nodo_Interno(pos_x, pos_y, caracter) 
        nodo_X = self.filas.getEncabezado(pos_x)
        nodo_Y = self.columnas.getEncabezado(pos_y)

        if nodo_X == None: 
            nodo_X = Nodo_Encabezado(pos_x)
            self.filas.insertar_nodoEncabezado(nodo_X)

        if nodo_Y == None: 
            nodo_Y = Nodo_Encabezado(pos_y)
            self.columnas.insertar_nodoEncabezado(nodo_Y)

        # ----- INSERTAR NUEVO EN FILA
        if nodo_X.acceso == None: 
            nodo_X.acceso = nuevo
        else: 
            if nuevo.coordenadaY < nodo_X.acceso.coordenadaY: 
                nuevo.derecha = nodo_X.acceso              
                nodo_X.acceso.izquierda = nuevo
                nodo_X.acceso = nuevo
            else:
                tmp : Nodo_Interno = nodo_X.acceso     
                while tmp != None:                      
                    if nuevo.coordenadaY < tmp.coordenadaY:
                        nuevo.derecha = tmp
                        nuevo.izquierda = tmp.izquierda
                        tmp.izquierda.derecha = nuevo
                        tmp.izquierda = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp.coordenadaX and nuevo.coordenadaY == tmp.coordenadaY:
                        break;
                    else:
                        if tmp.derecha == None:
                            tmp.derecha = nuevo
                            nuevo.izquierda = tmp
                            break;
                        else:
                            tmp = tmp.derecha 
                            
        if nodo_Y.acceso == None: 
            nodo_Y.acceso = nuevo
        else: 
            if nuevo.coordenadaX < nodo_Y.acceso.coordenadaX:
                nuevo.abajo = nodo_Y.acceso
                nodo_Y.acceso.arriba = nuevo
                nodo_Y.acceso = nuevo
            else:
                tmp2 : Nodo_Interno = nodo_Y.acceso
                while tmp2 != None:
                    if nuevo.coordenadaX < tmp2.coordenadaX:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY == tmp2.coordenadaY: 
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo



    def graficarDibujo(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')

        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( 
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( 
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)


    def graficarDot(self, nombre):
        grafo = 'digraph T{ \nnode[shape=box fontname="Arial" fillcolor="white" style=filled ]'
        grafo += '\nroot[label = \"capa: '+ str(self.capa) +'\", group=1]\n'
        grafo += '''label = "{}" \nfontname="Arial Black" \nfontsize="15pt" \n
                    \n'''.format('MATRIZ DISPERSA')

        x_fila = self.filas.primero
        while x_fila != None:
            grafo += 'F{}[label="F{}",fillcolor="plum",group=1];\n'.format(x_fila.id, x_fila.id)
            x_fila = x_fila.siguiente

        x_fila = self.filas.primero
        while x_fila != None:
            if x_fila.siguiente != None:
                grafo += 'F{}->F{};\n'.format(x_fila.id, x_fila.siguiente.id)
                grafo += 'F{}->F{};\n'.format(x_fila.siguiente.id, x_fila.id)
            x_fila = x_fila.siguiente

        y_columna = self.columnas.primero
        while y_columna != None:
            group = int(y_columna.id)+1
            grafo += 'C{}[label="C{}",fillcolor="powderblue",group={}];\n'.format(y_columna.id, y_columna.id, str(group))
            y_columna = y_columna.siguiente
        
        cont = 0
        y_columna = self.columnas.primero
        while y_columna is not None:
            if y_columna.siguiente is not None:
                grafo += 'C{}->C{}\n'.format(y_columna.id, y_columna.siguiente.id)
                grafo += 'C{}->C{}\n'.format(y_columna.siguiente.id, y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente

        y_columna = self.columnas.primero
        x_fila = self.filas.primero
        grafo += 'root->F{};\n root->C{};\n'.format(x_fila.id, y_columna.id)
        grafo += '{rank=same;root;'
        cont = 0
        y_columna = self.columnas.primero
        while y_columna != None:
            grafo += 'C{};'.format(y_columna.id)
            cont += 1
            y_columna = y_columna.siguiente
        grafo += '}\n'
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont += 1
            while aux2 != None:

                if aux2.caracter == '*':
                    grafo += 'N{}_{}[label="{}",group="{}", fillcolor="black"];\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.caracter, int(aux2.coordenadaY)+1)          
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        aux = self.filas.primero
        aux2 = aux.acceso
        cont = 0
        while aux is not None:
            rank = '{'+f'rank = same;F{aux.id};'
            cont = 0
            while aux2 != None:
                if cont == 0:
                    grafo += 'F{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->F{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id)
                    cont += 1
                if aux2.derecha != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux2.derecha.coordenadaX, aux2.derecha.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.derecha.coordenadaX, aux2.derecha.coordenadaY, aux2.coordenadaX, aux2.coordenadaY)

                rank += 'N{}_{};'.format(aux2.coordenadaX, aux2.coordenadaY)
                aux2 = aux2.derecha
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
            grafo += rank+'}\n'
        aux = self.columnas.primero
        aux2 = aux.acceso
        cont = 0
        while aux != None:
            cont = 0
            grafo += ''
            while aux2 != None:
                if cont == 0:
                    grafo += 'C{}->N{}_{};\n'.format(aux.id, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->C{};\n'.format(aux2.coordenadaX, aux2.coordenadaY, aux.id) 
                    cont += 1
                if aux2.abajo != None:
                    grafo += 'N{}_{}->N{}_{};\n'.format(aux2.abajo.coordenadaX, aux2.abajo.coordenadaY, aux2.coordenadaX, aux2.coordenadaY)
                    grafo += 'N{}_{}->N{}_{};\n'.format( aux2.coordenadaX, aux2.coordenadaY,aux2.abajo.coordenadaX, aux2.abajo.coordenadaY)
                aux2 = aux2.abajo
            aux = aux.siguiente
            if aux != None:
                aux2 = aux.acceso
        grafo += '}'

        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as f:
            f.write(grafo)
        result = "matriz_{}.pdf".format(nombre)
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)