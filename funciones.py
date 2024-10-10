from variables import*

import pprint

import random

import copy

import time

import os



def crear_tablero():   
    global tamaño_tablero

    linea = []
    tablero = []

    for i in range(tamaño_tablero):
        linea.append(".")
    for i in range(tamaño_tablero):
        tablero.append(linea.copy())
    return tablero


def mostrar_tablero(tablero):
    pprint.pprint(tablero)


def disparo(fila,columna,tablero):
    acertado = False
    if tablero[fila][columna] == 'B':
        acertado = True
        tablero[fila][columna] = 'X'
        #print('Tocado')
    else:
        tablero[fila][columna] = '~'
        os.system("cls")
        #print('Agua')

    return acertado


def juega_usuario(tablero_ordenador):

    coordenada_fila = int(input('Introduce la primera coordenada'))
    coordenada_columna = int(input('Introduce ahora la segunda coordenada'))
    tablero = tablero_ordenador
    resultado = disparo(coordenada_fila,coordenada_columna,tablero)

    return resultado


def juega_computer(tablero_jugador):
    
    coordenada_fila = random.randint(0,9)
    coordenada_columna = random.randint(0,9)
    tablero = tablero_jugador

    print()
    print("Turno ordenador:")
    resultado = disparo(coordenada_fila,coordenada_columna,tablero)
    
    return resultado


def posicion_correcta(tablero,fila, columna,tamaño,direccion):
    global tamaño_tablero

    #Verificamos dirección arriba
    if direccion == "Arriba":
        #print("probando direccion arriba")
        if fila - tamaño < 0:
            #print("parametro", fila , tamaño, "menor que cero")
            return False # El barco se sale del tablero
         #Verificar que no haya colisiones
        for i in range(tamaño):
            if tablero[fila - i][columna] != ".":
                #print("encontrado barco en posición", fila - i, columna)
                return False # Ya hay un barco en esa posición
               
    # Verificamos dirección abajo
    elif direccion == "Abajo":
        if fila + tamaño > tamaño_tablero:
            return False # El barco se sale del tablero
        #Verificar que no haya colisiones
        for i in range(tamaño):
            if tablero[fila + i][columna] != ".":
                return False # Ya hay un barco en esa posición
        
    #Verificamos dirección izquierda
    elif direccion == "Izquierda":
        if columna - tamaño < 0:
            return False # El barco se sale del tablero
        #Verificar que no haya colisiones
        for i in range(tamaño):
            if tablero[fila][columna - i] != ".":
                return False # Ya hay un barco en esa posición
    
    #Verificamos dirección derecha
    elif direccion == "Derecha":
        if columna + tamaño > tamaño_tablero:
            return False # El barco se sale del tablero
        #Verificar que no haya colisiones
        for i in range(tamaño):
            if tablero[fila][columna + i] != ".":
                return False # Ya hay un barco en esa posición
    #print("posición encontrada")
    return True


def colocar_barco(tablero,fila,columna,tamaño,direccion):
    if direccion =="Arriba":
        for i in range(tamaño):
            tablero[fila - i][columna]="B"
    elif direccion == "Abajo":
        for i in range(tamaño):
            tablero[fila + i][columna]= "B"
    elif direccion == "Izquierda":
        for i in range(tamaño):
            tablero[fila][columna - i]= "B"
    elif direccion == "Derecha":
        for i in range(tamaño):
            tablero[fila][columna + i]= "B"


def posicionar_barcos_aleatoriamente(tablero):

    for barco,tamaño in flota.items():
        colocado = False
        #print("Intentamos colocar", barco,"de tamaño", tamaño) 
        while not colocado:
            fila = random.randint(0,9)
            columna = random.randint(0,9)
            direccion = random.choice(["Arriba", "Abajo","Izquierda","Derecha"])
            #print("probando coordenadas aleatorias",fila, columna,"y direccion", direccion)
            if posicion_correcta(tablero,fila, columna,tamaño,direccion):
                colocar_barco(tablero,fila,columna,tamaño,direccion)
                #pprint.pprint(tablero)
                colocado = True


def actualizar_tablero_mis_disparos(tablero_ordenador):
    tablero_mis_disparos = copy.deepcopy(tablero_ordenador) #Crear un copia profunda del tablero del ordenador
    for i, fila in enumerate(tablero_mis_disparos): #Iterar sobre las filas y columnas del tablero
        for j, celda in enumerate(fila):
            if celda == "B": #Reemplazar "B" por "."
                tablero_mis_disparos[i][j] = "."
             
    return tablero_mis_disparos


def actualizar_tablero_disparos_ordenador(tablero_jugador):
    tablero_disparos_ordenador = copy.deepcopy(tablero_jugador) #Crear un copia profunda del tablero jugador

    return tablero_disparos_ordenador


def contar_barcos_hundidos(tablero): #¿Cuántas casillas de barcos se han alcanzado?
    hundidos = sum(fila.count("X") for fila in tablero)
    return hundidos 

