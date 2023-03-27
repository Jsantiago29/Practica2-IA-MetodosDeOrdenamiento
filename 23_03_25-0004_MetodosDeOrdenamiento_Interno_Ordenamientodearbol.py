# Jaime Santiago Garci­a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> Ordenamiento de arbol

import random

def heapsort(lista):

    n = len(lista)

    # Construir un árbol heap a partir de la lista
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Extraer los elementos del árbol heap uno por uno y colocarlos en la lista ordenada
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

    return lista

def heapify(lista, n, i):
    """
    Convierte una sublista de la lista dada en un árbol heap, comenzando desde el nodo i.
    """
    # Inicializar el nodo más grande como el nodo raíz
    maximo = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # Si el hijo izquierdo es más grande que la raíz, entonces actualizar el nodo más grande
    if izquierda < n and lista[izquierda] > lista[maximo]:
        maximo = izquierda

    # Si el hijo derecho es más grande que el nodo más grande hasta ahora, entonces actualizar el nodo más grande
    if derecha < n and lista[derecha] > lista[maximo]:
        maximo = derecha

    # Si el nodo más grande no es la raíz, entonces intercambiar la raíz y el nodo más grande, y seguir heapificando
    if maximo != i:
        lista[i], lista[maximo] = lista[maximo], lista[i]
        heapify(lista, n, maximo)

# Generar una lista de números aleatorios
lista = [random.randint(1, 1000) for _ in range(100)]

# Imprimir la lista original
print("Lista original:")
print(lista)

# Ordenar la lista usando el método de ordenamiento de árbol
lista_ordenada = heapsort(lista)

# Imprimir la lista ordenada
print("Lista ordenada:")
print(lista_ordenada)

