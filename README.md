# Unidad 7: Recursividad

Soluciones de la tarea de la Unidad 7, escritas en Python. Cada ejercicio
está en su propio archivo dentro de la carpeta `Tarea/` y se ejecuta por
separado.

## Estructura

```
U7_recursividad/
├── README.md
├── .gitignore
└── Tarea/
    ├── MultiplicacionRusa.py
    ├── ConteoVocales.py
    ├── ImprimirPatron.py
    ├── Caminos.py
    └── FlattenList.py
```

## Ejercicios

| Archivo | Ejercicio | Idea | Tiempo | Espacio (pila) |
|---|---|---|---|---|
| `MultiplicacionRusa.py` | Multiplicación rusa (sin `*`) | Se duplica `a` con `a + a`, se divide `b` entre 2 y se acumula `a` cuando `b` es impar | O(log b) | O(log b) |
| `ConteoVocales.py` | Conteo de vocales | Se revisa el primer carácter y se recorta el texto | O(n²) por los slices | O(n²) por los slices |
| `ImprimirPatron.py` | Patrón de asteriscos | Se imprimen primero las filas anteriores y luego la fila `n` | O(n²) | O(n) |
| `Caminos.py` | Caminos en un tablero N x M | Desde (0,0) bajando o yendo a la derecha, con memoización | O(N·M) | O(N·M) |
| `FlattenList.py` | Aplanar lista anidada | Se separa el primer elemento del resto de la lista | O(n²) por los slices | O(n) |

Cada archivo tiene comentados el caso base y el caso recursivo.

## Requisitos

Python 3.8 o superior. No necesita librerías externas.

## Cómo ejecutarlos

```bash
cd Tarea
python MultiplicacionRusa.py
python ConteoVocales.py
python ImprimirPatron.py
python Caminos.py
python FlattenList.py
```

## Ejemplos de ejecución

**MultiplicacionRusa.py**
```
Ingrese el primer número: 13
Ingrese el segundo número: 5
Resultado: 65
```

**ConteoVocales.py**
```
Ingrese un texto: Programación
Cantidad de vocales: 5
```

**ImprimirPatron.py**
```
Ingrese un número: 3
*
**
***
```

**Caminos.py**
```
Ingrese la cantidad de filas: 3
Ingrese la cantidad de columnas: 3
Cantidad de caminos: 6
```

**FlattenList.py**
```
Lista plana: [1, 2, 3, 4, 5]
```

## Subir el proyecto a GitHub

```bash
cd U7_recursividad
git init
git add .
git commit -m "Tarea Unidad 7: Recursividad"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/U7_recursividad.git
git push -u origin main
```
