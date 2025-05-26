def retornar_nota(estudiante):
    return estudiante[1]

lista_estudiantes= [('Edward', 4.2), 
                    ('Pepe', 2.5),
                    ('María', 3.1),
                    ('Carlos', 4.5)]

lista_ordenada = sorted(lista_estudiantes, key=retornar_nota)
print(lista_ordenada)