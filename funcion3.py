#Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres primeros.
#En el bloque principal del programa definir una tupla con los nombres de meses.
#Mostrar por pantalla los primeros tres caracteres de cada mes."

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
    "Noviembre", "Diciembre")

def recibe_cadena(cadena):
    return cadena[:3]

for m in meses:
    print(recibe_cadena(m))