#Crea un programa que convierta una temperatura de 
# **Celsius a Fahrenheit** o de **Fahrenheit a Celsius**, 
# dependiendo de la elección del usuario.

op = int(input('Ingrese una opción; (1)Fahrenheit - (2)Celsius: '))
temperatura = int(input('Ingrese la temperatura: '))

if op == 1:
    fahre = 1.8 * temperatura + 32
    print(f'La temperatura de {temperatura} Fahrenheit en Celsius es {fahre}')
else:
    celsius = (temperatura - 32) / 1.8
    print(f'La temperatura de {temperatura} Celsius en Fahrenheit es {celsius}')
