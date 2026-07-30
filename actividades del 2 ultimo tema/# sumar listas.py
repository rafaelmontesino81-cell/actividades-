# sumar listas
def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += 1
    return suma
numeros = []
for i in range(5):
     valor = int(input(f"Ingresa numero (i+1): "))
     numeros.append(valor)

total = sumar_lista(numeros)
total_sum = sum(numeros)#usando funcion bult-in

print("suma con bucle: ",total)
print("suma con sum(): ",total_sum)
