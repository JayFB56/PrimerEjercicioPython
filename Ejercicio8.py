# Desarrolla un programa que calcule el **precio final de un producto** 
# después de aplicarle un porcentaje de descuento. El programa 
# debe validar que el porcentaje esté entre 0 y 100.

p = float(input("Ingrese el precio original del producto: "))

while True:
    d = float(input("Ingrese el porcentaje de descuento (entre 0 y 100): "))
    
    if 0 <= d <= 100:
        break
    else:
        print("Porcentaje de descuento no valido. Debe estar entre 0 y 100.")

pf = p - (p * (d / 100))

print(f"El precio final después de aplicar el descuento es: {pf:.2f}")
