# Jaime Santiago Garcia - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Externos  --->  Polyphase sort.

import random

# Función para ordenar un arreglo utilizando el método Polyphase sort
def polyphase_sort(arr):
    
    # Función auxiliar para mezclar dos segmentos ordenados
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    
    # Dividir el arreglo en bloques de tamaño especificado y ordenarlos
    k = 4
    blocks = [sorted(arr[i:i+k]) for i in range(0, len(arr), k)]
    
    # Mezclar bloques adyacentes utilizando el método Polyphase sort
    n = len(blocks)
    while n > 1:
        if n % 2 == 0:
            starts = list(range(0, n, 2))
            stops = list(range(2, n+1, 2))
            stops[-1] = n
        else:
            starts = [0] + list(range(1, n, 2))
            stops = list(range(1, n+1, 2))
            stops[-1] = n
            
        merged_blocks = []
        for i, j in zip(starts, stops):
            merged_blocks.append(merge(blocks[i], blocks[j-1]))
        blocks = merged_blocks
        n = len(blocks)
    
    # Devolver el arreglo ordenado
    return blocks[0]

# Crear un arreglo de 100 números aleatorios entre 1 y 100
arr = [random.randint(1, 1000) for i in range(100)]

# Imprimir el arreglo desordenado
print("Arreglo original:", arr)

# Ordenar el arreglo utilizando el método Polyphase sort
sorted_arr = polyphase_sort(arr)

# Imprimir el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
