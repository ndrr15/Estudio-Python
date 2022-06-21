cadena = "abcdefghijklmnopqrstuvwxyz"
archivo = open('letras.txt','w')
archivo.write(cadena)
archivo.close() 

nuevoArchivo = open('pruebaLlenado_escritura.txt','w')
contador = 0

while contador < 5:
    texto = input('escribeme: ')
    nuevoArchivo.write(texto +'\n')
    contador = contador + 1
    
nuevoArchivo.close()    