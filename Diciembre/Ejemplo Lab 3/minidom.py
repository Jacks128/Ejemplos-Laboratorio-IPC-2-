from xml.dom import minidom

mydoc=minidom.parse('Entrada.xml')

book = mydoc.getElementsByTagName('Book')
print("Atributos de Libro: ")
'''for i in range(0,len(book)) :
    print(book[i].attributes['id'].value)'''

for i in book:
    print(i.attributes['id'].value)

print("Valores de Autor: ")
author=mydoc.getElementsByTagName('Author')

for i in author:
    print(i.firstChild.data)
    print(i.childNodes[0].data)




