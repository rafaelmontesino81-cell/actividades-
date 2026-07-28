# Calcular precio con descuento
precio_original = float(input("Ingrese precio original: "))
if precio_original < 100:
    descuento = 0.00
elif precio_original <= 200:
    descuento = 0.10
elif precio_original <= 400:
     descuento = 0.15
else: 
    descuento = 0.20
#calcular el precio final con descuento
preciofinal = precio_original - (precio_original * descuento)
print("El precio final con descuento es: ", preciofinal)