def contar_vocales(texto):
    # caso base: texto vacío
    if texto == "":
        return 0

    if texto[0] in "aeiouáéíóúüAEIOUÁÉÍÓÚÜ":
        cantidad = 1
    else:
        cantidad = 0

    # caso recursivo: se revisa el resto del texto
    return cantidad + contar_vocales(texto[1:])


texto = input("Ingrese un texto: ")

print("Cantidad de vocales:", contar_vocales(texto))
