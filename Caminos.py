def caminos_tablero(fila, col, n, m, memo=None):
    if memo is None:
        memo = {}

    # caso base: se salió del tablero
    if fila >= n or col >= m:
        return 0

    # caso base: llegó a la esquina inferior derecha
    if fila == n - 1 and col == m - 1:
        return 1

    # si ya se calculó, se reutiliza
    if (fila, col) in memo:
        return memo[(fila, col)]

    # caso recursivo: bajar o ir a la derecha
    abajo = caminos_tablero(fila + 1, col, n, m, memo)
    derecha = caminos_tablero(fila, col + 1, n, m, memo)

    memo[(fila, col)] = abajo + derecha
    return memo[(fila, col)]


n = int(input("Ingrese la cantidad de filas: "))
m = int(input("Ingrese la cantidad de columnas: "))

if n < 1 or m < 1:
    print("Filas y columnas deben ser mayores que 0")
else:
    print("Cantidad de caminos:", caminos_tablero(0, 0, n, m))
