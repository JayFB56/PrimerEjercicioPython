#Escribe un programa que calcule el **perímetro** y 
# el **área** de un rectángulo, dados su largo y ancho. 
# El programa debe validar que ambos valores sean positivos.


largo = float(input('Ingrese el largo del rectángulo: '))
ancho = float(input('Ingrese el ancho del rectángulo: '))

if largo <= 0 or ancho <= 0:
    print('El largo y el ancho deben ser valores positivos')
else:
    perimetro = 2 * (largo + ancho)
    area = largo * ancho

    print(f'El área del rectángulo es: {area}')
    print(f'El perímetro del rectángulo es: {perimetro}')
