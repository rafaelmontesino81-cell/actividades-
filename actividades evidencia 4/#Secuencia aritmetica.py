#Secuencia aritmetica 
inicio = int(input("Primer numero: "))
diferencia = int(input("Diferencia: "))
limite = int(input("limite maximo: "))
num = inicio 
while True:
    print(num, end="")
    num += diferencia
    if num > limite:
        break 
    print("\nSecuencia aritmetica desde", inicio, "hasta", limite)