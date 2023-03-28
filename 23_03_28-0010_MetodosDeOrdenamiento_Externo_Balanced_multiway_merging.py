# Jaime Santiago Garcia - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Externos  --->  Balanced multiway merging.
import random

# Función para ordenar un arreglo utilizando el método Balanced multiway merging
def balanced_multiway_merge_sort(arr):
    
    # Función auxiliar para dividir el arreglo en segmentos de tamaño especificado
    def split(arr, size):
        return [arr[i:i+size] for i in range(0, len(arr), size)]
    
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
    
    # Dividir el arreglo en segmentos de tamaño k y ordenarlos
    k = 3
    segments = split(arr, k)
    for i in range(len(segments)):
        segments[i] = sorted(segments[i])
    
    # Mezclar segmentos adyacentes de dos en dos
    while len(segments) > 1:
        i = 0
        while i < len(segments) - 1:
            segments[i] = merge(segments[i], segments[i+1])
            del segments[i+1]
            i += 1
    
    # Devolver el arreglo ordenado
    return segments[0]

# Crear un arreglo de 100 números aleatorios entre 1 y 1000
arr = [random.randint(1, 1000) for i in range(100)]

# Imprimir el arreglo desordenado
print("Arreglo original:", arr)

# Ordenar el arreglo utilizando el método Balanced multiway merging
sorted_arr = balanced_multiway_merge_sort(arr)

# Imprimir el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
