# Escribe un programa que calcule el *área* y el *perímetro* 
# de un círculo, dado el valor de su radio. El programa debe validar 
# que el radio sea un valor positivo.

radio = int(input('Ingrese el radio del circulo: '))
pi = 3.1416
area = pi*pow(radio, 2)
perimetro = 2*pi*radio

print('El area del circulo es: ', area)
print('El perimetro del circulo es: ', perimetro)