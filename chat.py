#Pedí al usuario que ingrese números enteros positivos uno a uno. 
# Cuando el usuario ingrese un 0, se termina la carga. Luego, mostrales:

#Cuántos números fueron ingresados (sin contar el 0).

#Cuál fue el mayor número ingresado.

#Cuál fue el promedio de todos los números.

lista_numeros = []

numeros = int(input("Ingresá un número"))

while numeros != 0:
    lista_numeros.append(numeros)
    numeros = int(input("Ingresá otro número"))
    


