# Calculadora_de_calificaciones
parciales = float(input("Ingresa tu calificacion del parcial (0 - 100) :"))
proyecto = float(input("Ingresa tu calificacion de proyectos (0 - 100) :"))
examen = float(input("Ingresa calificacion del examen (0 - 100) :"))

if (parciales <0 or parciales >100) or (proyecto < 0 or parciales >100) or (examen < 0 or examen > 100):
    print ("Error: Las calificaciones deben estar entre 0 y 100")

else:
    promedio = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
    print("La calificacion final es:", promedio)