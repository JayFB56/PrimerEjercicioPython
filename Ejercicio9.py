# Escribe un programa que convierta una cantidad de **horas** 
# ingresada por el usuario a su equivalente en **días**, 
# **horas**, **minutos** y **segundos**.

horas = int(input("Ingrese la cantidad de horas: "))
dias = horas // 24  
horasRes = horas % 24  
minutos = horasRes * 60
segundos = minutos * 60  

print(f'{horas} horas son equivalentes a:')
print(f'{dias} dias, {horasRes} horas, {minutos} minutos y {segundos} segundos.')
