# Vocales o consonantes 
while True:
    letra = input("Ingresa letra (enter para terminar):")
    if letra == "":
        break
    if letra.lower() in "aeiou":
        print("Es vocal")
    else:
        print("Es consonante")
        