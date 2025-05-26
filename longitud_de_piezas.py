#y luego ingrese la longitud de cada perfil
#


loteCompleto = 0
aptas = 0
cantidad = int(input("Diga cuántas piezas va a procesar: "))

while loteCompleto<cantidad:
    longitud = float(input("Ingrese la longitud de la pieza: "))
    if longitud>=1.20 and longitud <=1.30:
        aptas+=1
    loteCompleto+=1
print("Existen ", aptas," piezas entre 1.2 y 1.3")
