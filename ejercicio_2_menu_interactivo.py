# Menú de control del robot
while True:
    print("A. Mover a la derecha")
    print("B. Mover a la izquierda")
    print("C. Mover hacia el frente")
    print("D. Mover hacia atrás")
    print("E. Apagar")

    Orden = input("Ingrese un código de comando: ")

    match Orden:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            print("Apagando el robot...")
            break  # finaliza el bucle 
        case _:
            print("Comando no reconocido. Intente de nuevo.")
