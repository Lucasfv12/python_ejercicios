meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
    "Noviembre", "Diciembre")

def recibir_mes(numero_mes):
    return meses[numero_mes - 1:]

print(recibir_mes(9))