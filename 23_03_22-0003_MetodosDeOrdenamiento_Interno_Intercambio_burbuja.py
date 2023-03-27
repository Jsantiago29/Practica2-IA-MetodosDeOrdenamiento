# Jaime Santiago Garci­a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> Intercambio o borbuja

import random

def intercambio(lista):
    n = len(lista)
    # Este ciclo se ejecuta n veces para asegurarse de que todos los elementos hayan sido comparados
    for i in range(n):
        # Este ciclo compara cada par de elementos adyacentes y los intercambia si están en el orden equivocado
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Generar una lista de números aleatorios
lista = [random.randint(1, 1000) for _ in range(100)]

# Imprimir la lista original
print("Lista original:")
print(lista)

# Ordenar la lista usando el método de intercambio
lista_ordenada = intercambio(lista)

# Imprimir la lista ordenada
print("Lista ordenada:")
print(lista_ordenada)
