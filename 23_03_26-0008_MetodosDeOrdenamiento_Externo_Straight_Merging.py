# Jaime Santiago Garcia - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Externos  ---> Straight merging

import random

# Generamos una lista de números aleatorios entre 1 y 1000
lista_numeros = [random.randint(1, 1000) for i in range(100)]

# Función para dividir la lista en dos mitades
def dividir_lista(lista):
    mitad = len(lista) // 2
    return lista[:mitad], lista[mitad:]

# Función para fusionar dos listas ordenadas en una sola lista ordenada
def fusionar_listas(lista1, lista2):
    indice1 = indice2 = 0
    lista_fusionada = []
    while indice1 < len(lista1) and indice2 < len(lista2):
        if lista1[indice1] < lista2[indice2]:
            lista_fusionada.append(lista1[indice1])
            indice1 += 1
        else:
            lista_fusionada.append(lista2[indice2])
            indice2 += 1
    lista_fusionada.extend(lista1[indice1:])
    lista_fusionada.extend(lista2[indice2:])
    return lista_fusionada

# Función principal de ordenamiento de Straight Merging
def straight_merging_sort(lista):
    if len(lista) <= 1:
        return lista
    lista1, lista2 = dividir_lista(lista)
    lista1_ordenada = straight_merging_sort(lista1)
    lista2_ordenada = straight_merging_sort(lista2)
    return fusionar_listas(lista1_ordenada, lista2_ordenada)

# Ordenamos la lista utilizando el método de Straight Merging
lista_ordenada = straight_merging_sort(lista_numeros)

# Imprimimos la lista original y la lista ordenada
print("Lista original: ", lista_numeros)
print("Lista ordenada: ", lista_ordenada)
