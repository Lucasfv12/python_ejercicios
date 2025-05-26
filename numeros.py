#Pedí números hasta que el usuario ingrese un número negativo. Mostrá la suma total de los números positivos ingresados.

numeros_lista = []

numero = int(input("Ingresá un número: "))

while numero >= 0:
    numeros_lista.append(numero)
    numero = int(input("Ingresá otro número"))
    
print("la suma total de los números ingresados es: " ,sum(numeros_lista))
        