import xml.etree.ElementTree as ET

tree=ET.parse('Entrada.xml')
root=tree.getroot()

print(root)

print("Atributo Price dentro de Book")
print(root[0][3].attrib)

print('Valor de Price en Book')
print(root[0][3].text)


print('Valor de ambos Book')
for i in root:
    for j in i:
        print(j.text)