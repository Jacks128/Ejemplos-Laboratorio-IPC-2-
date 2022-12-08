class Curso:

    def __init__(self,nombre,creditos,periodos,codigo,nota,area):
        self.nombre=nombre
        self.creditos=creditos
        self.periodos=periodos
        self.codigo=codigo
        self.nota=nota
        self.area=area

    def obtener_nota(self):
        return self.nota

    def imprimir_datos(self):
        print(self.nombre)
        print(self.area)
        print(self.codigo)
        print(self.creditos)
        print(self.nota)
        print(self.periodos)

    

    