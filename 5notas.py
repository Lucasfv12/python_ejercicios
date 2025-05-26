#Escribir un programa que solicite ingresar 5 notas de alumnos y
#nos informe cuántos tienen notas mayores o iguales a 7 
#cuántos menores.

mayor = 0
menor = 0
alumno = 1



while alumno < 5:
    print("La nota del alumno numero : " ,alumno)
    nota = int(input("Ingresar notas de alumnos"))
    alumno+=1
    if nota >=7:
        mayor+=1
    else:
        menor+=1
        
    

