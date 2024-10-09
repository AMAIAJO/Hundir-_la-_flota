from funciones import*

from variables import*

import time


cerrar_juego = False
while not cerrar_juego: #Bucle principal
    opcion = input("Selecciona un opción (1-2):\n1.Jugar\n2.Salir del juego")

    if opcion == "1":
        # Creo tablero
        tablero_jugador = crear_tablero()
        tablero_ordenador = crear_tablero()
        tablero_mis_disparos = crear_tablero()

        print("Creando tablero para jugador")
        pprint.pprint(tablero_jugador)
        print()
        #pprint.pprint(tablero_mis_disparos)
        time.sleep(0.5)

        # Coloco aleatoriamente los barcos
        posicionar_barcos_aleatoriamente(tablero_jugador) 
        print("Tu flota ha sido posicionada aleatoriamente de la siguiente manera:")
        pprint.pprint(tablero_jugador)
        print()
        time.sleep(0.5)

        posicionar_barcos_aleatoriamente(tablero_ordenador)
        #pprint.pprint(tablero_ordenador)

        # Empieza el juego
        barcos_hundidos_jugador = 0
        barcos_hundidos_ordenador = 0
        

        while barcos_hundidos_jugador < total_barcos and barcos_hundidos_ordenador < total_barcos:
            print("Tablero del contrincante:")
            tablero_mis_disparos = actualizar_tablero_mis_disparos(tablero_ordenador)
            pprint.pprint(tablero_mis_disparos)
            time.sleep(0.5)

            # Turno del jugador
            while True:
                tirada = juega_usuario(tablero_ordenador)
                if tirada == True:
                     tablero_mis_disparos = actualizar_tablero_mis_disparos(tablero_ordenador)
                     pprint.pprint(tablero_mis_disparos)
                     time.sleep(0.5)
                     barcos_hundidos_jugador += 1
                     print(f"Has hundido: {barcos_hundidos_jugador}/{total_barcos}")
                
                else:
                     tablero_mis_disparos = actualizar_tablero_mis_disparos(tablero_ordenador)
                     pprint.pprint(tablero_mis_disparos)
                     time.sleep(0.5)
                     break
                
            # Verificar si el jugador ha ganado
            if barcos_hundidos_jugador == total_barcos:
                    print("¡Enhorabuena! Has hundido todos los barcos")
                    break

            #Turno del ordenador
            while True:
                tirada = juega_computer(tablero_jugador)
                if tirada == True:
                    barcos_hundidos_ordenador += 1
                    print(f"Barcos hundidos por el ordenador: {barcos_hundidos_ordenador}/{total_barcos}")
                
                else:
                    break
        

             # Verificar si el ordenador ha ganado
            if barcos_hundidos_ordenador == total_barcos:
                    print("Lo siento, has perdido :( El ordenador ha hundido todos tus barcos")
                    break

    elif opcion == "2":
        cerrar_juego = True
        print("Saliendo del juego")

    else:
        print("Opción no válida. Por favor selecciona 1 o 2")