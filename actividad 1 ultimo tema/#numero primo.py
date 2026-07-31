#numero primo
numero = int(input("Ingresa un número: "))

contador = 0
i = 1

while i <= numero:
    if numero % i == 0:
        contador += 1
    i += 1

if contador == 2:
    print("Es un número primo.")
else:
    print("No es un número primo.")