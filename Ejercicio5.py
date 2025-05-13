# Desarrolla un programa que convierta una cantidad dada en 
# **millas** a su equivalente en **kilómetros** y **metros**.

millas = int(input('Ingrese el valor en millas: '))
kilometros = millas*1.609
metros = millas*1609

print(f'{millas} millas en kilometros es {kilometros}')
print(f'{millas} millas en metros es {metros}')