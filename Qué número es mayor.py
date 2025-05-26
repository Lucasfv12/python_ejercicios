num1 = int(input('Dame un número'))
num2 = int(input('Dame otro número'))
num3 = int(input('dame otro número'))

if num1 > num2 and num1 > num3:
    print(f'El número más alto es el {num1}')
elif num2 > num1 and num2 > num3:
    print(f'El numero más alto es el {num2}')
else:
    print(f'El número más alto es el {num3}')