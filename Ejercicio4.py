# Crea un programa que calcule la **potencia de un número**, 
# dados una base y un exponente ingresados por el usuario. 
# El programa debe permitir al usuario realizar múltiples cálculos sin reiniciar.

def calcular_potencia(base, exponente):
    return base ** exponente

while True:
    base = float(input('Ingrese la base: '))
    exponente = int(input('Ingrese el exponente: '))

    resultado = calcular_potencia(base, exponente)
    
    print(f'{base} elevado a {exponente} es: {resultado}')
    
    otra_operacion = input('¿Desea realizar otro calculo? (si/no): ').strip().lower()
    
    if otra_operacion != 'si':
        print('Nos Vemos!!!')
        break
