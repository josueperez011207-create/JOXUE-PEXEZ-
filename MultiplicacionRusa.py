def multiplicacion_rusa(a, b, acumulado=0):
    # b negativo: se calcula con -b y se cambia el signo
    if b < 0:
        return -multiplicacion_rusa(a, -b, acumulado)

    # caso base: ya no queda nada por multiplicar
    if b == 0:
        return acumulado

    # si b es impar, se suma a al acumulado
    if b % 2 == 1:
        acumulado = acumulado + a

    # caso recursivo: se duplica a y se divide b entre 2
    return multiplicacion_rusa(a + a, b // 2, acumulado)


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("Resultado:", multiplicacion_rusa(a, b))
