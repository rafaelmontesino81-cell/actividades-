# Adivinar el numero 
import random 
numero_secreto = random.randint(1, 100)
while True: 
    intento  = int(input("Adivina el numero entre (1 - 100):"))
    if numero_secreto > intento:
        print("El intento es menor que el numero secreto")
    elif numero_secreto < intento:
        print("El intento es mayor que el numero secreto")
    else:
        print("¡Correcto! Has adivinado el numero.")
        break
print("El juego ha terminado. El numero secreto era:", numero_secreto)