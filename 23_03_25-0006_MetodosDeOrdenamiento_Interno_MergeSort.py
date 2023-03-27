# Jaime Santiago Garci­a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> MergeSort

import random

# Generamos una lista de números aleatorios entre 1 y 1000
lista_numeros = [random.randint(1, 1000) for i in range(100)]

# Función de MergeSort que toma una lista como entrada y devuelve la lista ordenada
def merge_sort(lista):
    # Si la lista tiene un elemento o menos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en dos partes
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    
    # Recursivamente ordenamos cada una de las partes
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)
    
    # Mezclamos las dos partes ordenadas en una sola lista ordenada
    return merge(izquierda_ordenada, derecha_ordenada)

# Función auxiliar que mezcla dos listas ordenadas en una sola lista ordenada
def merge(izquierda, derecha):
    lista_ordenada = []
    i, j = 0, 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j += 1
    
    # Agregamos los elementos restantes de ambas listas
    while i < len(izquierda):
        lista_ordenada.append(izquierda[i])
        i += 1
    while j < len(derecha):
        lista_ordenada.append(derecha[j])
        j += 1
    
    return lista_ordenada

# Imprimimos la lista original
print("Lista original:")
print(lista_numeros)

# Ordenamos la lista usando MergeSort
lista_ordenada = merge_sort(lista_numeros)

# Imprimimos la lista ordenada
print("Lista ordenada:")
print(lista_ordenada)
