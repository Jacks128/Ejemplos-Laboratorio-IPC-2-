from xml.dom import minidom

mydoc=minidom.parse('items.xml')
items=mydoc.getElementsByTagName('item') 

print('Item #2 attribute:')
print(items[1].attributes['name'].value)


print('\nAll Atributes:')
for elem in items:
    print(elem.attributes['name'].value)

print('\nItem #2 data:')
print(items[1].firstChild.data)    

print('\n All item data: ')
for elem in items:
    print(elem.firstChild.data)