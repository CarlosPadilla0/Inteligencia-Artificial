# Proyecto 1: Puzzle 8

## Descripción
Este proyecto implementa el juego del Puzzle 8, un rompecabezas deslizante que consiste en un tablero de 3x3 con fichas numeradas del 1 al 8 y un espacio vacío. El objetivo del juego es ordenar las fichas en secuencia numérica moviendo las fichas adyacentes al espacio vacío.

## Características
- Interfaz gráfica para jugar el Puzzle 8.
resolver el puzzle automáticamente. A continuación, se describen los algoritmos utilizados:


### Distancia de Manhattan
La distancia de Manhattan es una heurística utilizada en el algoritmo de Búsqueda A*. Calcula la suma de las distancias horizontales y verticales desde cada ficha hasta su posición objetivo. Esta heurística es admisible, lo que significa que nunca sobreestima el costo de llegar a la solución, ayudando a encontrar la solución óptima de manera eficiente.
- Posibilidad de personalizar el estado inicial del tablero.

### Búsqueda A*
El algoritmo de Búsqueda A* utiliza una función heurística para guiar la búsqueda hacia la solución de manera más eficiente. Combina las ventajas de BFS y DFS, encontrando soluciones óptimas con un uso moderado de memoria y tiempo de procesamiento.resolver el puzzle automáticamente.
- Posibilidad de personalizar el estado inicial del tablero.

## Uso
Para ejecutar el juego, utiliza el siguiente comando:
```bash
python main.py
```

## Algoritmos de Búsqueda
Este proyecto implementa varios algoritmos de búsqueda para resolver el Puzzle 8:
- Búsqueda en Anchura (BFS)
- Búsqueda en Profundidad (DFS)
- Búsqueda A*

