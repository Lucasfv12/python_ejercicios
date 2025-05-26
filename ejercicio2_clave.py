#Solicitar el ingreso de una clave por 
# teclado y almacenarla en una cadena 
# de caracteres. Controlar que el string
# ingresado tenga entre 10 y 20 
# caracteres para que sea válido, 
# en caso contrario mostrar un mensaje 
# de error.

clave = input("Ingresá tu clave: ")
longitud = len(clave)
if longitud >= 10 and longitud <= 20:
    print("La clave es válida")
else:
    print("La clave no tiene la cantidad de valores correspondientes")