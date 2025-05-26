while True:
    numero = int(input('Dame un número y te diré si es par o impar: '))
    if numero % 2 == 0:
        print(f'el {numero} es un número par')
    else:
        print(f'el {numero} es un número impar')
    
    repetir = input('Querés darme otro número. Responde con s/n').strip().lower() 
    if repetir != "s":
            print('Hasta la próxima')
            break