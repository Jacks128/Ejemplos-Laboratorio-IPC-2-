a=1
b='dos'
c=12.6
d=True
f=[a,b,c,d,]

print(type(a),a)
a='Todos van a ganar IPC2'
print(type(a),a)

print("Ejemplo de casteo")
print(type(d),d)
d=str(d)
print(type(d),d)

print([(x, type(x)) for x in f])

def sumaditos(a,b):
    suma=a+b
    return suma

if sumaditos(12,8)==20:
    print('Vamos a ganar IPC2')
else:  
    print('Vamos a ganar despues IPC2')

print('--------------------- i t e r a c i o n e s --------------------')

n=5
while n>0:
    print(n)
    n=n-1
print('Orale pues')

'''while True:
    linea=input('> ')
    if linea=='fin':
        break
    print(linea)
print ('TERMINADO')'''

print('--------------------- i t e r a c i o n e s  2 --------------------')

'''while True:
    linea=input('> ')
    if linea[0]=='#':
        continue
    if linea=='fin':
        break
    print(linea)
print ('TERMINADO')'''

amigos=['Jose','Glenda','Susan']
for cuate in amigos:
    print('Feliz Navidad querido amigo ',cuate)
print('Y feliz año nuevo')

fruta='piña'
index=0
while index < len(fruta):
    letra=fruta[index]
    print(letra)
    index=index+1

palabra='parangaragutirimicuaro'
contador=0
for i in palabra:
    if i=='a':
        contador=contador+1
print('Cantidad de letras a: ',contador)
