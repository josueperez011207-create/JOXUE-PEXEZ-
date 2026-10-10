def flatten_lista(lista):
    # caso base: lista vacía
    if lista == []:
        return []

    primero = lista[0]
    resto = flatten_lista(lista[1:])

    # caso recursivo: si el primero es lista, se aplana también
    if isinstance(primero, list):
        return flatten_lista(primero) + resto

    return [primero] + resto


lista = [1, [2, [3, 4], 5]]

print("Lista plana:", flatten_lista(lista))
