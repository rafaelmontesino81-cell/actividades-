# calcular_salario_neto

salario_bruto = float(input("Ingrsa salario bruto: "))
porcentaje = float(input("% Impuestos: " ))
deducciones = float(input("Ingresa tu deduccion: "))

impuestos = salario_bruto * (porcentaje / 100)

salario_neto = salario_bruto - impuestos - deducciones
print("Tu salario neto es:", salario_neto)