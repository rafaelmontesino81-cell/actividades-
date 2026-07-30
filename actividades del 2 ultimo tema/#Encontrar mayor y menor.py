#Encontrar mayor y menor
def maximo_manual(lista):
    if len(lista) == 0:
     return None
    maximo = lista[0]
    for num in lista[1:]:
         if num > maximo:
             maximo = num
    return maximo
def minim_manual(lista):
    if len(lista) == 0:
     return None
    minimo = lista[0]
    for num in lista[:1]:
        if num < minimo:
            minimo = num 
    return minimo
numeros = []
for i in range(6):
    valor = int(input(f"Numero {i+1}: "))
    numeros.append(valor)
mayor_manual = maximo_manual(numeros)
menor_manual = minim_manual(numeros)
print("mayor (manual): ",mayor_manual)
print("menor (manual):", menor_manual)