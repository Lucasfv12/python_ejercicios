texto = input("ingresá una palabra: ")

texto_invertido = ""

for letra in texto:
    texto_invertido = letra + texto_invertido
    
print("El texto en reverso:", texto_invertido)    

if texto == texto_invertido:
    print(f"Bingo! Tu palabra {texto} es un palindromo")