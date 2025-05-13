#Escribe un programa que permita calcular el 
# **interés compuesto** de un capital inicial, 
# una tasa de interés anual y un número de años.

def interesCompuesto(capital_inicial, tasa_interes, años):
    monto_final = capital_inicial * (1 + tasa_interes / 100) ** años
    return monto_final

while True:
    capital_inicial = float(input('Ingrese el capital inicial: '))
    tasa_interes = float(input('Ingrese la tasa de interés anual (%): '))
    años = int(input('Ingrese el numero de años: '))
    monto_final = interesCompuesto(capital_inicial, tasa_interes, años)

    interes_generado = monto_final - capital_inicial
    
    print(f'El monto final después de {años} años es: {monto_final:.2f}')
    print(f'El interes generado es: {interes_generado:.2f}')
