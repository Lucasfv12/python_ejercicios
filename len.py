def crear_contraseña_random(num):
    caracteres = "abcdefghij"  # 10 letras, índice 0 al 9
    num_entero = str(num)
    
    # Tomemos el último dígito del número:
    ultimo_digito = int(num_entero[-1])  # -1 significa el último carácter
    
    letra = caracteres[ultimo_digito]
    return f"Tu contraseña es: {letra}_segura"

print(crear_contraseña_random(256))  # Usa el 3 → 'd'


