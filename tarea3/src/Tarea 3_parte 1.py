# Tarea N°3 - Parte 1 - Juego Gato
# Khevin Flores Olivares

import random

# ------------------------------
# FUNCIONES AUXILIARES
# ------------------------------

def inicializarTablero(d):
    """
    Devuelve un tablero d x d representado como lista de listas,
    inicializado con el símbolo '·' en todas las casillas.
    """
    if not isinstance(d, int) or d <= 0:
        raise ValueError("d debe ser un entero positivo")
    return [['·' for _ in range(d)] for _ in range(d)]

def imprimirTablero(tablero):
    """
    Imprime el tablero en pantalla con separadores.
    Por ejemplo, un tablero 2x2:
    O | X
    -----
    X | O
    """
    if not tablero:
        print("(tablero vacío)")
        return

    filas_texto = [' | '.join(fila) for fila in tablero]
    separador = '-' * len(filas_texto[0])
    for i, linea in enumerate(filas_texto):
        print(linea)
        if i != len(filas_texto) - 1:
            print(separador)

def agregarJugada(tablero, val, fila, col):
    """
    Coloca la jugada val ('O' o 'X') en tablero[fila][col].
    Retorna True si colocó correctamente; False si la casilla ya tenía jugada.
    Lanza IndexError si fila/col fuera de rango, ValueError si val inválido.
    """
    n = len(tablero)
    if val not in ('O', 'X'):
        raise ValueError("val debe ser 'O' o 'X'")
    if not (0 <= fila < n and 0 <= col < n):
        raise IndexError("fila o columna fuera de rango")
    if tablero[fila][col] != '·':
        return False
    tablero[fila][col] = val
    return True

def encontrarGanador(tablero):
    """
    Devuelve 'O' o 'X' si alguno de los jugadores tiene
    una fila, columna o diagonal completa. Devuelve None si no hay ganador.
    """
    n = len(tablero)
    if n == 0:
        return None

    # Revisar filas
    for i in range(n):
        primero = tablero[i][0]
        if primero != '·' and all(tablero[i][j] == primero for j in range(n)):
            return primero

    # Revisar columnas
    for j in range(n):
        primero = tablero[0][j]
        if primero != '·' and all(tablero[i][j] == primero for i in range(n)):
            return primero

    # Diagonal principal
    primero = tablero[0][0]
    if primero != '·' and all(tablero[i][i] == primero for i in range(n)):
        return primero

    # Diagonal secundaria
    primero = tablero[0][n-1]
    if primero != '·' and all(tablero[i][n-1-i] == primero for i in range(n)):
        return primero

    return None

def sigueJuego(tablero):
    """
    Retorna True si el juego debe continuar:
      - No hay ganador
      - Existe al menos una casilla '·'
    Retorna False si terminó (hay ganador o empate)
    """
    if encontrarGanador(tablero) is not None:
        return False
    for fila in tablero:
        if '·' in fila:
            return True
    return False

# ------------------------------
# EJEMPLOS DE PRUEBA DE FUNCIONES (opcionales)
# ------------------------------
if __name__ == "__main__":
    # Inicializar tablero 2x2 para prueba rápida
    tablero_2 = inicializarTablero(2)
    print("Tablero 2x2 inicial:")
    imprimirTablero(tablero_2)
    print("\n")

    # Agregar jugadas
    agregarJugada(tablero_2, 'O', 0, 0)
    agregarJugada(tablero_2, 'X', 0, 1)
    agregarJugada(tablero_2, 'X', 1, 0)
    agregarJugada(tablero_2, 'O', 1, 1)

    print("Tablero 2x2 tras jugadas:")
    imprimirTablero(tablero_2)
    print("\n")

    ganador = encontrarGanador(tablero_2)
    print(f"Ganador: {ganador}")  # Debe devolver 'O' (diagonal principal)

    estado = sigueJuego(tablero_2)
    print(f"Sigue el juego: {estado}")  # Debe ser False porque ya hay ganador

# ------------------------------
# PROGRAMA PRINCIPAL: JUEGO INTERACTIVO
# ------------------------------

def jugarGato():
    """
    Juego de Gato (Tic-Tac-Toe) interactivo.
    - Tamaño del tablero definido por el usuario.
    - Jugador inicial elegido al azar.
    - Alterna turnos entre 'X' y 'O'.
    - Muestra ganador o empate al final.
    """
    
    # Elegir tamaño del tablero
    while True:
        try:
            d = int(input("Ingrese el tamaño del tablero (ej: 3 para 3x3): "))
            if d <= 0:
                print("❌ Debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("❌ Entrada inválida. Debe ingresar un número entero.")

    tablero = inicializarTablero(d)
    
    # Elegir jugador inicial al azar
    jugador = random.choice(['X', 'O'])
    print(f"\n🎲 El jugador que inicia es: {jugador}\n")

    # Loop principal de juego
    while sigueJuego(tablero):
        # Mostrar tablero actual
        imprimirTablero(tablero)
        print(f"\nTurno del jugador {jugador}")

        # Pedir coordenadas
        try:
            fila = int(input(f"Ingrese la fila (0 a {d-1}): "))
            col = int(input(f"Ingrese la columna (0 a {d-1}): "))
        except ValueError:
            print("❌ Entrada inválida. Solo se permiten números.")
            continue

        # Validar rango
        if not (0 <= fila < d and 0 <= col < d):
            print("❌ Posición fuera del rango.")
            continue

        # Intentar agregar jugada
        if not agregarJugada(tablero, jugador, fila, col):
            print("❌ Esa casilla ya está ocupada. Intenta otra.")
            continue

        # Revisar ganador
        ganador = encontrarGanador(tablero)
        if ganador:
            imprimirTablero(tablero)
            print(f"\n🎉 ¡El jugador {ganador} ganó!")
            return

        # Cambiar de jugador
        jugador = 'O' if jugador == 'X' else 'X'

    # Si se llena el tablero sin ganador
    imprimirTablero(tablero)
    print("\n🤝 ¡Empate!")

# Ejecutar juego interactivo
if __name__ == "__main__":
    jugarGato()
