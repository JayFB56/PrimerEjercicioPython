# Crea un programa que permita ingresar un número indefinido de 
# **notas**, y al finalizar, calcule el **promedio** de todas ellas.

suma_notas = 0
contador = 0

while True:
    nota = input("Ingresa una nota o 'fin' para terminar: ")

    if nota == "fin":
        break

    try:
        nota = float(nota)  
        suma_notas += nota  
        contador += 1        
    except ValueError:
        print("Por favor, ingresa un numero valido.") 

if contador > 0:
    promedio = suma_notas / contador
    print(f"El promedio de las notas es: {promedio:.2f}")
else:
    print("No se ingresaron notas.")
