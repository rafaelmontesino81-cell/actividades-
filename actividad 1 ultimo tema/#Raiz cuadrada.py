#Raiz cuadrada
import math

numero = float(input("Ingresa un número: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("La raíz cuadrada es:", raiz)
else:
    print("No existe raíz cuadrada real para números negativos.")