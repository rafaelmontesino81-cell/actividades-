# conteo de numeros 
n = int(input("Ingrese cantidad de numeros: "))
mayores = 0
menores = 0
iguales = 0
for i in range(n):
    numero = int(input("Ingrese un numero:"))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales +=1
print("Numeros mayores a 0:", mayores)
print("Numeros menores a 0:", menores)
print("Numeros iguales a 0:", iguales)