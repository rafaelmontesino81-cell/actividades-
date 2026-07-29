# Factorial de un numero 
factorial = int(input("Ingrese numero para factorial: "))
num = 1
if num < 0:
    print("No se puede calcular factorial de numero negativo")
else:
    for i in range(1, num + 1):
        factorial += i
print("El factorial de", num, "es", factorial)