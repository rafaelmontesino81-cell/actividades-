# contador de digitos 
numero = int (input("Ingrese un numero:"))
if numero == 0:
   digitos = 1
else:
   digitos = 0
   if numero < 0:
        numero = abs(numero)
while numero != 0:
        numero //= 10
        digitos += 1
print("El numero de digitos es:", digitos)