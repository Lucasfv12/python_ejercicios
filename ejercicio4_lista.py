#Definir una lista que almacene 
# por asignación los nombres de 
# 5 personas. #Contar cuantos de 
# esos nombres 
# tienen 5 o más caracteres.

contadorNombres = 0

lista_nombres = ["Lucas", "Karina", "Pablo", "Abi", "Meli"]
for nombre in lista_nombres:
    if len(nombre) >= 5:
        contadorNombres+=1
        
print(f"Son {contadorNombres} los nombres con 5 o más caracteres")
        
        