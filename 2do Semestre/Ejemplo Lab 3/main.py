#Element Tree

import xml.etree.ElementTree as ET

tree=ET.parse('items.xml')
root=tree.getroot()

print('Atributo item 2')
print(root[0][1].attrib)

print('\nTodos los atributos')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

print('\nData item 2')
print(root[0][1].text)

print('\nTodos los datos')
for elem in root:
    for subelem in elem:
        print(subelem.text)
