#contar letras "a" en una palabra 
palabra = input("Ingrese la palabra:").lower()
contador = 0
for letra in palabra: 
    if letra == "a":
        contador += 1
print("La cantidad de letras 'a' en la palabra es:", contador)