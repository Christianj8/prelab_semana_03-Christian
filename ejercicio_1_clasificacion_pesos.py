# Lista de pesos, en kilogramos, generada por el sistema de pesaje automatico
pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]

# Ponemos el contador fuera del bucle para que no se reinicie en cada vuelta
piezas_validas = 0

for peso in pesos_piezas:
    if peso <= 0:
        print("Error de lectura: Flujo negativo descartado.")
    elif peso <= 13:
        print("Pieza Ligera aprobada.")
        piezas_validas = piezas_validas + 1
    else:
        print("Pieza Pesada aprobada.")
        piezas_validas = piezas_validas + 1

print("Piezas válidas que pasaron la prueba:", piezas_validas)
