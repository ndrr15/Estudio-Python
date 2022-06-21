# FUNCION STRIP 
# **********************
asteriscos = '*************************'
print ('FUNCION STRIP')
print(asteriscos)
mensaje  = "   hola a todos    "
mensajeCorto = mensaje.strip()
print('--'+mensaje+'--')
print('--'+mensajeCorto+'--')
print(asteriscos) 
# **********************
# FUNCION LEN 
# **********************
print ('FUNCION LEN')
print(asteriscos)
nombre  = "Pepito"
caracteres = len(nombre)
print(nombre ,'tiene ', caracteres ,'caracteres')
print(asteriscos) 
# **********************
# FUNCION LOWER 
# **********************
print ('FUNCION LOWER')
print(asteriscos)
mensaje = "PePiTo TiEnE HaMbRe"
mensajeMinuscula = mensaje.lower()
print('--'+mensaje+'--')
print('--'+mensajeMinuscula+'--')
print(asteriscos) 
# **********************
# FUNCION UPPER 
# **********************
print ('FUNCION UPPER')
print(asteriscos)
mensajeMayusculas = mensaje.upper()
print('--'+mensaje+'--')
print('--'+mensajeMayusculas+'--')
print(asteriscos) 
# **********************
# FUNCION SPLIT 
# **********************
print ('FUNCION SPLIT')
print(asteriscos)
listaPalabras = mensaje.split(' ')
print('--'+mensaje+'--')
print(listaPalabras)
print(asteriscos) 
# **********************
# FUNCION COUNT 
# **********************
print ('FUNCION COUNT')
print(asteriscos)
mensaje = "en mi casa, en mi auto, en mi escuela, enmicado"
contarPalabra = mensaje.count('mi')
print(contarPalabra)
print(asteriscos) 
# **********************
# FUNCION ENDSWITH 
# **********************
print ('FUNCION ENDSWITH')
print(asteriscos)
mensaje = "en mi casa, en mi auto, en mi escuela, enmicado"
print(mensaje.endswith('ado'))
print(mensaje.endswith('ido'))
print(asteriscos) 
# **********************
# FUNCION CAPITALIZE 
# **********************
print ('FUNCION CAPITALIZE')
print(asteriscos)
mensaje = "en mi casa tengo dentro mi auto, en mi escuela, enmicado"
print(mensaje.capitalize())
print(asteriscos) 
# **********************
# FUNCION CENTER 
# **********************
print ('FUNCION CENTER')
print(asteriscos)
mensaje = "hola mundo"
print(mensaje.center(30,"-"))
print(asteriscos) 
# **********************
# FUNCION FIND e INDEX
# **********************
print ('FUNCION FIND e INDEX')
print(asteriscos)
mensaje = "me gusta jugar a las canicas"
print(mensaje.find('jugar'))
print(mensaje.find('empezar'))
print(mensaje.index('canicas'))
##print(mensaje.index('salir'))
print(asteriscos) 
# **********************
# FUNCION ISALNUM
# **********************
print ('FUNCION ISALNUM')
print(asteriscos)
mensaje1 = "TODOS 1010"
mensaje2 = "TODOS"
mensaje3 = "1000"
print(mensaje.isalnum())
print(mensaje1.isalnum())
print(mensaje2.isalnum())
print(mensaje3.isalnum())
print(asteriscos) 
# **********************
# FUNCION ISALPHA
# **********************
print ('FUNCION ISALPHA')
print(asteriscos)
mensaje1 = "TODOS1010"
mensaje2 = "TODOS"
mensaje3 = "1000"
print(mensaje.isalpha())
print(mensaje1.isalpha())
print(mensaje2.isalpha())
print(mensaje3.isalpha())
print(asteriscos) 
# **********************
# FUNCION ISDIGIT
# **********************
print ('FUNCION ISDIGIT')
print(asteriscos)
mensaje1 = "TODOS1010"
mensaje2 = "TODOS"
mensaje3 = "1000"
print(mensaje.isdigit())
print(mensaje1.isdigit())
print(mensaje2.isdigit())
print(mensaje3.isdigit())
print(asteriscos) 
# **********************
# FUNCION REPLACE
# **********************
print ('FUNCION REPLACE')
print(asteriscos)
mensaje = "me gusta jugar a las canicas"
print(mensaje.replace('gusta', "viva petro hpta"))
print(asteriscos) 
# **********************