# Jaime Santiago Garci­a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> Quicksort

import random

def quicksort(lista):

    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) < 2:
        return lista

    # Seleccionar un elemento pivot aleatorio de la lista
    pivot = random.choice(lista)

    # Dividir la lista en dos sub-listas: elementos menores que el pivot y elementos mayores que el pivot
    menores = [elem for elem in lista if elem < pivot]
    iguales = [elem for elem in lista if elem == pivot]
    mayores = [elem for elem in lista if elem > pivot]

    # Aplicar recursivamente QuickSort a las sub-listas de menores y mayores, y luego combinar las tres listas
    return quicksort(menores) + iguales + quicksort(mayores)

# Generar una lista de 1000 números aleatorios
lista = [random.randint(1, 1000) for _ in range(100)]

# Imprimir la lista original
print("Lista original:")
print(lista)

# Ordenar la lista usando el algoritmo de ordenamiento QuickSort
lista_ordenada = quicksort(lista)

# Imprimir la lista ordenada
print("Lista ordenada:")
print(lista_ordenada)
