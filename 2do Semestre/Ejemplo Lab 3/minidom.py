#Mini DOM
from xml.dom import minidom

mydocument=minidom.parse('items.xml')
items=mydocument.getElementsByTagName('item')

print('Atributo del item 2, en la posicion 1')
print(items[1].attributes['size'].value)

print('\n Todos los atributos')
for elem in items:
    print(elem.attributes['name'].value)

print('\nData item 1')
print(items[0].firstChild.data)

print('\nData de todos los items')
for elem in items:
    print(elem.firstChild.data)
