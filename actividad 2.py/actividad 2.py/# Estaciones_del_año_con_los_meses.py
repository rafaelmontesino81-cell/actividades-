# Estaciones_del_año_con_los_meses
estacion = int(input("Ingrese el numero del mes (1 - 12): "))
match estacion: 
    case 12 | 1 | 2:
        estacion = "Invierno"
    case 3 | 4 | 5:
        estacion = "Primavera"
    case 6 | 7 | 8:
        estacion = "Verano"
    case 9 | 10 | 11:
        estacion = "Otoño"
    case _ :
        estacion = "Mes no valiedo"
print ("La estacion del año es: ", estacion)