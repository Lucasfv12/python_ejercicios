num1 = int(input('Ingresá un número'))
num2 = int(input('Ingresá otro número'))

if num1 > num2:
    resta = num1 - num2
    suma = num1 + num2
    print (f'La resta entre num1 y num2 es {resta}')
    print (f'La suma entre num1 y num2 es {suma}')
else:
    print('el primer numero no es mayor que el segundo.')

