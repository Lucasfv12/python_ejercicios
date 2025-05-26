##Ingresar una oración que pueden tener letras tanto 
# en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. Crear un segundo string 
# con toda la oración en minúsculas para que sea más fácil 
# disponer la condición que verifica que es una vocal.

contador_vocal = 0

oracion = input("Ingresá una oración: ").lower()
for vocal in oracion:
    if vocal in "aeiou":
        contador_vocal+=1
print("La cantidad de vocales es de: ", contador_vocal)
        