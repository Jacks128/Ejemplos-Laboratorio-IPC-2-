'''
--------D I C C I O N A R I O S --------
d={"Enero":1,"Febrero":2,"Septiembre":9,"Diciembre":12}
print(d)

d["Marzo"]=3
print(d)

#d.clear()
#print(d)

print(d.items())
print(d.keys())
print(d.values())

print(d.pop("Diciembre"))
print(d.get("Septiembre"))
print(d)

d.update({"Julio":7})
print(d)

print(len(d))

d=dict({"Enero":1,"Febrero":2,"Septiembre":9,"Diciembre":12,"Mayo":5})
print(type(d))
print(d)

#----------T U P L A S----------------
tupla=()
print(type(tupla))

tupla=(1,5,8,7,45)
print(type(tupla))
print(tupla)

tupla1=tuple((12,45,60))
print(type(tupla))

tupla2=tuple([1,5,7,8,6])
print(type(tupla))
print(tupla)

tupla3=tuple("Hola,a ganar el lab")
print(tupla)

tupla4=tupla2+tupla3
print(tupla4)

tupla5=tupla1*5
print(tupla5)

print(45 in tupla1)

print(len(tupla2))
print(max(tupla1))
print(min(tupla2))
''' 

import re
from unittest import result
cadena="Fijo todos ganaremos el lab"
patron="lab"
resultado=re.search(patron,cadena)
print(resultado)

print(resultado.start())
print(resultado.end())
print(resultado.span())

cadena1="Buscar una posicion o palabra"
patron="Buscar"
resultado=re.match(patron,cadena)
print(resultado)