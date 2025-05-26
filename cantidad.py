lista = [1,2,3]

tupla = (1,2,3)

lista.append(4)

print(lista)

lista.pop(-1)
print(lista)

diccionario = {"Nombre": "Lucas"}
print(diccionario["Nombre"])
diccionario.update({"Apellido": "Vergara", "Edad":"34 años"})
print(diccionario)
diccionario["Curso"] = "Matematica"
print(diccionario)
del diccionario["Curso"]
print(diccionario)

diccionario.clear()
print(diccionario)