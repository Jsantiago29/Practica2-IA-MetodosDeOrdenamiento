# Jaime Santiago Garcia - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Externos  --->  Distribution of initial runs.

import random

# Función para ordenar un arreglo utilizando el método Distribution of initial runs
def distribution_of_initial_runs(arr):
    
    # Función auxiliar para mezclar dos bloques ordenados
    def merge_blocks(left, right):
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
    
    # Determinar el tamaño de los bloques iniciales y el número de bloques
    b = int(len(arr[0]) ** 0.5)
    
    # Dividir el arreglo en bloques iniciales y ordenarlos
    blocks = [sorted(arr[0][i:i+b]) for i in range(0, len(arr[0]), b)]
    
    # Concatenar bloques ordenados
    sorted_arr = []
    for block in blocks:
        sorted_arr += block
    
    # Mezclar bloques adyacentes hasta que quede un solo bloque
    while len(blocks) > 1:
        start = 0
        merged_blocks = []
        while start < len(blocks):
            left = blocks[start]
            right = blocks[start + 1] if start + 1 < len(blocks) else []
            merged_blocks.append(merge_blocks(left, right))
            start += 2
        blocks = merged_blocks
        
        # Concatenar bloques ordenados
        sorted_arr = []
        for block in blocks:
            sorted_arr += block
    
    # Devolver el arreglo ordenado
    return sorted_arr

# Crear un arreglo de 100 números aleatorios entre 1 y 100
arr = [random.randint(1, 1000) for i in range(100)]

# Imprimir el arreglo desordenado
print("Arreglo original:", arr)

# Ordenar el arreglo utilizando el método Distribution of initial runs
sorted_arr = distribution_of_initial_runs([arr])

# Imprimir el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
