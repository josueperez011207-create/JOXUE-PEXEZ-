"""
Mini-Proyecto: Explorador de Directorios (Unidad 7: Recursividad)

El sistema de archivos se representa como un diccionario anidado:
    - las carpetas son diccionarios
    - los archivos son strings con su tamaño (las "hojas" del árbol)

Cómo correrlo:
    python ExploradorRecursivo.py
"""


class ExploradorRecursivo:
    """Recorre un sistema de archivos con métodos recursivos."""

    # Factores para convertir tamaños a KB
    UNIDADES = {"kb": 1, "mb": 1024, "gb": 1024 * 1024}

    @staticmethod
    def imprimir_arbol(sistema, nivel=0, prefijo=""):
        """Muestra la estructura con indentaciones visuales.

        'nivel' indica la profundidad actual (0 = raíz) y 'prefijo' va
        acumulando la sangría: crece 4 espacios por cada nivel.

        CASOS BASE:
          - un archivo (hoja) solo se imprime, no se entra en él
          - una carpeta vacía no tiene nada que recorrer (el for no corre)
        CASO RECURSIVO:
          - una carpeta imprime su nombre y luego se llama a sí misma con
            su contenido y nivel + 1
        """
        if nivel == 0:
            print("/")

        elementos = list(sistema.items())
        for posicion, (nombre, contenido) in enumerate(elementos):
            es_ultimo = posicion == len(elementos) - 1
            conector = "`-- " if es_ultimo else "|-- "

            if isinstance(contenido, dict):
                print(prefijo + conector + nombre + "/")
                # CASO RECURSIVO: entrar a la subcarpeta
                sangria = "    " if es_ultimo else "|   "
                ExploradorRecursivo.imprimir_arbol(
                    contenido, nivel + 1, prefijo + sangria)
            else:
                # CASO BASE: es un archivo (hoja)
                print(prefijo + conector + nombre + " (" + contenido + ")")

    @staticmethod
    def buscar_archivo(sistema, nombre):
        """Devuelve la ruta del archivo (ej. 'Documentos/fotos/perro.jpg')
        o None si no existe. Si hay varios con el mismo nombre, devuelve
        el primero que encuentre.

        La ruta se va armando mientras las llamadas recursivas regresan.

        CASOS BASE:
          - 'sistema' es una hoja (no es carpeta) -> None, sin crashear
          - se encontró un archivo con ese nombre -> devuelve su nombre
          - se revisó toda la carpeta sin éxito -> None
        CASO RECURSIVO:
          - por cada subcarpeta se busca dentro; si aparece, se antepone
            el nombre de la subcarpeta a la ruta
        """
        # CASO BASE: una hoja no tiene nada dentro donde buscar
        if not isinstance(sistema, dict):
            return None

        for clave, contenido in sistema.items():
            if isinstance(contenido, dict):
                # CASO RECURSIVO: buscar dentro de la subcarpeta
                ruta = ExploradorRecursivo.buscar_archivo(contenido, nombre)
                if ruta is not None:
                    return clave + "/" + ruta
            elif clave == nombre:
                # CASO BASE: archivo encontrado
                return clave

        # CASO BASE: no está en esta carpeta ni en sus subcarpetas
        return None

    @staticmethod
    def contar_archivos(sistema):
        """Cantidad total de archivos (las carpetas no cuentan).

        CASOS BASE:
          - una hoja (archivo) cuenta como 1
          - una carpeta vacía suma 0
        CASO RECURSIVO:
          - una carpeta suma los archivos de cada uno de sus elementos
        """
        # CASO BASE: es un archivo
        if not isinstance(sistema, dict):
            return 1

        total = 0
        for contenido in sistema.values():
            # CASO RECURSIVO: sumar lo que hay en cada elemento
            total = total + ExploradorRecursivo.contar_archivos(contenido)
        return total

    @staticmethod
    def calcular_tamano(sistema):
        """Extra: tamaño total en KB de todos los archivos.

        CASO BASE: un archivo se convierte a KB ('2mb' -> 2048).
        CASO RECURSIVO: una carpeta suma el tamaño de su contenido.
        """
        # CASO BASE: es un archivo, ej. "10kb"
        if not isinstance(sistema, dict):
            numero = sistema[:-2]
            unidad = sistema[-2:].lower()
            factor = ExploradorRecursivo.UNIDADES.get(unidad)
            if factor is None:
                raise ValueError("Tamaño no válido: " + sistema)
            return float(numero) * factor

        total = 0
        for contenido in sistema.values():
            # CASO RECURSIVO
            total = total + ExploradorRecursivo.calcular_tamano(contenido)
        return total


def main():
    sistema_archivos = {
        "Documentos": {
            "apuntes.txt": "10kb",
            "fotos": {
                "vacaciones.png": "2mb",
                "perro.jpg": "1mb"
            }
        },
        "sistema.dll": "500kb"
    }

    print("=== EXPLORADOR DE DIRECTORIOS ===\n")
    ExploradorRecursivo.imprimir_arbol(sistema_archivos)

    total = ExploradorRecursivo.contar_archivos(sistema_archivos)
    tamano = ExploradorRecursivo.calcular_tamano(sistema_archivos)
    print("\nTotal de archivos:", total)
    print("Tamaño total:", f"{tamano:.1f}", "KB")

    while True:
        nombre = input("\nArchivo a buscar (o 'salir'): ")
        if nombre == "salir":
            break

        ruta = ExploradorRecursivo.buscar_archivo(sistema_archivos, nombre)
        if ruta is None:
            print("No se encontró", nombre)
        else:
            print("Ruta:", ruta)


if __name__ == "__main__":
    main()
