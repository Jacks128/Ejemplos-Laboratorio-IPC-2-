#ElementTree

import xml.etree.ElementTree as ET
tree=ET.parse('items.xml')
root=tree.getroot()

print('Item #2 attribute:')
print(root[0][1].attrib)

print('\nAll attributes: ')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

