#conversion_moneda

conversion = float(input("Ingrese la cantidad a convertir en pesos Mexicanos: "))
print("1. USA")
print("2. EUR")
print("3. THB")
print("4. JPY")
print("5. KRW")
print("6. AUD")
print("7. PEN")
print("8. CAD")
print("9. VES")
print("10. ARS")
opciones = int(input("Seleccione la moneda a convetir: "))
match opciones: 
    case 1:
        resultado = conversion / 17.47
        moneda = "USA"
    case 2:
        resultado = conversion / 19.86
        moneda = "EUR"
    case 3:
        resultado = conversion / 0.52
        moneda = "THB"
    case 4: 
        resultado = conversion / 0.11
        moneda = "JPY"
    case 5: 
        resultado = conversion / 0.012
        moneda = "KRW"
    case 6:
        resultado = conversion / 12.17
        moneda = "AUD"
    case 7:
        resultado = conversion / 5.14
        moneda = "PEN"
    case 8:
        resultado = conversion / 12.37
        moneda = "CAD"
    case 9: 
        resultado = conversion / 0.0235
        moneda = "VES"
    case 10:
        resultado = conversion / 0.012
        moneda = "ARS"
print("La conversion de pesos Mexicanos a", moneda, "es", resultado, moneda)