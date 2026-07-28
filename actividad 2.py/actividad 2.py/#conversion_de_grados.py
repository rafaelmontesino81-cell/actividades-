#conversion_de_grados 

celsius = float(input("Ingrese grados en Celsius:"))
print("1. Fahrenheit")
print("2. Kelvin")
opciones = int(input("Seleccion la opcion de conversion:"))

match opciones:
    case 1:
        fahrenheit = (celsius * 9/5) + 32
        unidad = "°F"
        print("La conversion de grados es:", fahrenheit, unidad)
    case 2:
        kelvin = celsius + 273.15
        unidad = "°K"
        print("La conversion de grados es:", kelvin, unidad)

