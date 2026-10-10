def imprimir_patron(n):
    # caso base: no hay filas que imprimir
    if n <= 0:
        return

    # caso recursivo: primero las filas anteriores
    imprimir_patron(n - 1)

    # luego la fila actual
    print("*" * n)


n = int(input("Ingrese un número: "))

imprimir_patron(n)
