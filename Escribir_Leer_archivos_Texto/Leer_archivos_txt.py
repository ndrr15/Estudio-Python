# archivo = open('pruebaLlenado_escritura.txt','r')

# for linea in archivo:
#     print(linea.rstrip())

# cerrado = archivo.closed
# print ("el archivo esta cerrado ",cerrado)

# archivo.close()

# cerrado = archivo.closed
# print ("el archivo esta cerrado ",cerrado)

# lista = open ('pruebaLlenado_escritura.txt', 'r').readlines()
# print(lista)

archivo = open("letras.txt",'rb+')
posicionActual = archivo.tell()
print(posicionActual)
archivo.seek(5,0)
posicionActual = archivo.tell()
print(posicionActual)
cadena = archivo.read(3).decode('utf-8')
print(cadena)
posicionActual = archivo.tell()
print(posicionActual)
archivo.seek(2,1)
cadena = archivo.read(3).decode('utf-8')
print(cadena)

archivo.close()