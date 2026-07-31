#Remplazar caracter
texto = input("Escribe un texto: ")
viejo = input("Carácter que deseas reemplazar: ")
nuevo = input("Nuevo carácter: ")

resultado = texto.replace(viejo, nuevo)

print("Resultado:")
print(resultado)