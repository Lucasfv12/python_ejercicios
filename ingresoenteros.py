contadorEnteros = 0
numeros = []

for i in range(6):
    num = int(input("Ingrese 1 número enteros"))
    numeros.append(num)

for mayor in numeros:
    if mayor >= 10:
        contadorEnteros += 1

print(f"Tenés {contadorEnteros} mayores o iguales a 10")